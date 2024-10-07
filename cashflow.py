from flask import Flask, request, render_template_string, send_from_directory

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import time
import os
import webbrowser
from threading import Timer

app = Flask(__name__)

image_folder = "cashflow_images"
display_folder = "display"
html_file = os.path.abspath("display/cashflow.html")

def maintain_last_five_images(folder):
    files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.png')]
    
    files.sort(key=os.path.getctime)
    
    if len(files) > 4:
        for file_to_remove in files[:-4]:
            os.remove(file_to_remove)
            print(f"Deleted old image: {file_to_remove}")

def plot_graph(config_dict, annotations_dict):
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    if not os.path.exists(display_folder):
        os.makedirs(display_folder)


    min_period = min(map(int, config_dict.keys()))
    max_period = max(map(int, config_dict.keys()))

    for i in range(min_period, max_period + 1):
        if str(i) not in config_dict:
            config_dict[str(i)] = 0

    periods = list(config_dict.keys())
    cashflows = list(config_dict.values())

    fig, ax = plt.subplots(figsize=(8, 6))

    for period, cashflow in zip(periods, cashflows):
        ax.arrow(int(period), 0, 0, cashflow, head_width=0, head_length=0, fc='black', ec='black')
        ax.annotate('', xy=(int(period), cashflow), xytext=(int(period), 0),
                    arrowprops=dict(facecolor='black', shrink=0, width=1, headwidth=5, headlength=5))
        
        text_to_display = annotations_dict.get(period, f'${cashflow}')
        
        ax.text(int(period), cashflow + (4 if cashflow >= 0 else -8), text_to_display, 
                ha='center', va='bottom' if cashflow >= 0 else 'top')

    plt.xlabel('Period')
    plt.ylabel('Cash Flow')
    plt.xticks(range(min_period, max_period + 1))
    plt.axhline(0, color='black', linewidth=0.5)

    plt.xlim(min_period - 1, max_period + 1)
    plt.grid(True, axis='x', linestyle='--')

    ax.yaxis.set_ticks([])

    maintain_last_five_images(image_folder)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    image_path = os.path.join(image_folder, f"cashflow_{timestamp}.png")
    
    plt.savefig(f"{display_folder}/cashflow.png")
    plt.savefig(image_path)
    plt.close()


@app.route('/', methods=['GET', 'POST'])
def get_user_input():
    if request.method == 'POST':
        try:
            dict1_str = request.form.get('dict1')
            dict2_str = request.form.get('dict2')
            
            dict1 = dict(pair.strip().split(',') for pair in dict1_str.splitlines() if pair)
            dict2 = dict(pair.strip().split(',', 1) for pair in dict2_str.splitlines() if pair)
            
            dict1 = {k.strip(): int(v.strip()) for k, v in dict1.items()}
            dict2 = {k.strip(): v.strip() for k, v in dict2.items()}

            plot_graph(dict1, dict2)
            return render_template_string(TEMPLATE, message="Graph plotted successfully.", image_url="/display/cashflow.png")
        except ValueError:
            return render_template_string(TEMPLATE, error="Invalid format. Please enter key value pairs on new lines, separated by commas.")
        except Exception as e:
            return render_template_string(TEMPLATE, error=str(e))
    return render_template_string(TEMPLATE)

@app.route(f'/{display_folder}/<path:filename>')
def display_image(filename):
    return send_from_directory(f'{display_folder}', filename)

TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Cashflow Diagrams</title>
    <style>
      .container {
        display: flex;
        padding-left: 50px;
      }
      .info-container {
        flex: 1;
        padding-right: 10px;
      }
      .form-container {
        flex: 1;
        padding-left: 10px;
      }
      .image-container {
        flex: 1;
        padding-left: 10px;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="info-container">
        <h2>Usage</h2>
        <h3>Data</h3>
        <ul>
          <li>The Data box accepts comma-separated pairs of period, value. For example: 1, 100 </li>
          <li>The value determines how long the arrow will be.</li>
          <li>Different pairs on separate lines</li>
          <li>The order of the numbers in a pair matters - first item in a pair is the period, second is the value </li>
          <li>Order of the separate lines do not matter, you can have the entry for period 0 after the entry for period 1 and it'll be the same.</li>
          <li>The second item in the pair stands for the value, but more fundamentally it's just the size of the arrow. So if you don't want the sizes of arrows to be proportional to the value, you can pick any values you want in the Data box and provide the annotations you like. More details on annotations below</li>
        </ul>
        <h3>Annotations</h3>
        <ul>
          <li>By default, each arrow is annotated with its value</li> 
          <li>If you want to change that, you can use the annotations dialog box</li>
          <li>The Annotations box accepts comma-separated pairs of period, annotation. For example: 1, blah </li>
          <li>Different pairs on separate lines</li>
          <li>The order of the numbers in a pair matters - first item in a pair is the period, second is the annotation </li>
          <li>Order of the separate lines do not matter, you can have the entry for period 0 after the entry for period 1 and it'll be the same.</li>
          <li>Annotations replace the amount value on top of the arrow</li>
        </ul>
        <h3>Offline access</h3>
        <ul>
          <li>The most recently generated diagram is stored in the display folder</li>
          <li>The last 5 diagrams are timestamped and saved in cashflow_images folder</li>
        </ul>
        <h3>Notes</h3>
        <p>
        Make sure you press Ctrl+C in the terminal that you started this webpage with.<br><br>
        This webpage is merely a frontend for a local web server (hosted at <a href = http://127.0.0.1:5000>http://127.0.0.1:5000</a>)<br>
        To shut down the backend once you're done so it doesn't run in the background, you need to press Ctrl+C to kill the process. Ignore errors you might see on the console window.<br><br>
        This feature will possibly be added later.
        </p>
      </div>
      <div class="form-container">
        <h1>Cashflow Diagram</h1>
        <form method="post">
          <label for="dict1">Data</label><br>
          <textarea id="dict1" name="dict1" rows="20" cols="50">{{ request.form.get('dict1', '') }}</textarea><br><br>
          <label for="dict2">Annotations</label><br>
          <textarea id="dict2" name="dict2" rows="20" cols="50">{{ request.form.get('dict2', '') }}</textarea><br><br>
          <input type="submit" value="Plot Graph">
        </form>
        <br>
        {% if error %}
        <div style="color: red;">Error: {{ error }}</div>
        {% endif %}
        {% if message %}
        <div style="color: green;">{{ message }}</div>
        {% endif %}
      </div>
      <div class="image-container">
        {% if message %}
        <img src="{{ image_url }}" alt="Cashflow Chart">
        {% endif %}
      </div>
    </div>
  </body>
</html>
"""

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True)