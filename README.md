# Cashflow Diagrams README

This is a tool to easily generate neatly formatted cashflow diagrams. Much easier than using a software like draw.io.

## Requirements

Uses Python and matplotlib. Requires Python 3.10.

Important note: If you're using an older version of python, you may run into set up issues (you can check by running ```python --version``` in a terminal). You can proceed with the setup and try seeing what it says, but if it doesn't work you can try installing python from here: [https://www.python.org/downloads/release/python-3100/]. I'll soon update this to work with conda and then there should be no cross-platform issues - it did work fine with conda on a Mac when we tested it.

If you're running into problems, with setup or using it, drop me an email (vishnuv@seas.upenn.edu).

## Setup

1. Clone/download the repository
2. For Windows:
   1. Open a powershell terminal in this directory
   2. Run the setup script using ```.\setup.ps1```
3. For Mac:
   1. Open a bash terminal in this directory
   2. Run the setup script using ```sh setup.sh```

## Usage

Open a terminal into the same folder that has the .ps1 or .sh scripts. You can control this tool from that terminal.

1. Start the application
   1. Windows: ```.\run``` in powershell
   2. Mac: ```sh run.sh``` in Terminal
2. A webpage should open automatically with two text boxes
3. Enter the periods and amounts in the first text box, separated by commas
    1. There should only be one pair separated by commas on each line.
2. By default, the arrows are annotated by the cash amounts. If you want to override that for any period, add it to the second text box in the same format.
4. Press the "Plot graph" button
5. When you run the script,
   - The most recent image is saved as ```display/cashflow.png```
   - The last 5 images generated are timestamped and saved in the ```cashflow_images/``` folder
   - You don't need to create these folders, if it doesn't find the folder the script will create that automatically
6. When you are done, press Ctrl+C in the terminal you had open.

## Examples

### #1
![img1](https://github.com/user-attachments/assets/f3e1e6c2-be09-4a80-a88f-433a2e7cec12)

### #2
![img2](https://github.com/user-attachments/assets/784a9b01-300b-48a3-a5bb-c48ccddac226)

### #3
![img3](https://github.com/user-attachments/assets/b3101ccd-82f1-4f8a-bf9a-9aa3a6f4c49b)

### #4
![img4](https://github.com/user-attachments/assets/06b0eaec-5c65-4659-b6cb-e318f41b0144)
