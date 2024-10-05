import os
import webbrowser
import time
import matplotlib.pyplot as plt
from config import config, annotations

image_folder = "cashflow_images"

def maintain_last_five_images(folder):
    files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.png')]
    
    files.sort(key=os.path.getctime)
    
    if len(files) > 4:
        for file_to_remove in files[:-4]:
            os.remove(file_to_remove)
            print(f"Deleted old image: {file_to_remove}")

if __name__ == "__main__":

    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    min_period = min(map(int, config.keys()))
    max_period = max(map(int, config.keys()))
    min_value = min(map(int, config.values()))
    max_value = max(map(int, config.values()))

    for i in range(min_period, max_period + 1):
        if str(i) not in config:
            config[str(i)] = 0

    periods = list(config.keys())
    cashflows = list(config.values())

    fig, ax = plt.subplots(figsize=(8, 6))

    for period, cashflow in zip(periods, cashflows):
        ax.arrow(int(period), 0, 0, cashflow, head_width=0, head_length=0, fc='black', ec='black')
        ax.annotate('', xy=(int(period), cashflow), xytext=(int(period), 0),
                    arrowprops=dict(facecolor='black', shrink=0, width=1, headwidth=5, headlength=5))
        
        text_to_display = annotations.get(period, f'${cashflow}')
        
        ax.text(int(period), cashflow + (4 if cashflow >= 0 else -8), text_to_display, 
                ha='center', va='bottom' if cashflow >= 0 else 'top')

    plt.xlabel('Period')
    plt.ylabel('Cash Flow')
    plt.title('Cash Flow Diagram')
    plt.xticks(range(min_period, max_period + 1))
    plt.axhline(0, color='black', linewidth=0.5)

    plt.grid(True, axis='x', linestyle='--')

    plt.xlim(min_period - 1, max_period + 1)
    plt.ylim(min_value - 50, max_value + 50)

    ax.yaxis.set_ticks([])

    maintain_last_five_images(image_folder)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    image_path = os.path.join(image_folder, f"cashflow_{timestamp}.png")
    
    plt.savefig("display/cashflow.png")
    plt.savefig(image_path)
    html_file = os.path.abspath("display/cashflow.html")
    webbrowser.open(f"file://{html_file}")
    
    # Uncomment this to use matplotlib's default viewer
    # plt.show()
