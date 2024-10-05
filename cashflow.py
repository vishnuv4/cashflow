import matplotlib.pyplot as plt
from config import config, annotations

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
plt.ylabel('Cash Flow Diagram')
plt.title('Cash Flow')
plt.xticks(range(min_period, max_period + 1))  # Ensure all periods are marked on the x-axis
plt.axhline(0, color='black', linewidth=0.5)

plt.grid(True, axis='both', linestyle='--')

plt.savefig("cashflow.png")
plt.show()
