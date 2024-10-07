# Cashflow Diagrams README

This is a tool to easily generate neatly formatted cashflow diagrams. Much easier than using a software like draw.io.

## Requirements

Miniconda [https://docs.anaconda.com/miniconda/#quick-command-line-install]

Once you've installed it, run ```conda --version``` to make sure your terminal can access this program. You may proceed to the setup stage once this command displays whatever conda version you've installed.

### Windows 

The suggested route is using Powershell. You may have to do a one-time setup to allow Powershell to find the conda program.

Once you install this open the Anaconda Prompt (installed with miniconda) and run this command:
```
conda init powershell
```

Then you can open a powershell terminal (if you already had one open, you may need to close and reopen it) and verify using ```conda --version``` that your terminal can pick up the conda program.

### Mac

Sadly, the internet might be of more help.

(to be filled out after some more testing. I don't have a Mac so the internet might be of more help - but all we really want to accomplish is to make sure the terminal can find your conda program from any directory.)

If you're running into problems with any part of the setup, drop me an email (vishnuv@seas.upenn.edu), and I might be able to help you find the information you need to set it up.

## Setup

### Windows

1. Clone/download the repository
2. Open a powershell terminal in the directory that has the setup.ps1 script
3. Run the setup script using ```.\setup.ps1```

### Mac

1. Clone/download the repository
2. Open a bash terminal in the directory that has the setup.sh script
3. Run the setup script using ```sh setup.sh```

## Usage

Open a terminal into the same folder that has the .ps1 or .sh scripts. You can control this tool from that terminal.

### Windows

1. Run this command in a powershell terminal:
   ```
   .\run.ps1
   ```
2. A webpage should open automatically with two text boxes and instructions on how to enter data
3. Press the "Plot graph" button
4. When you are done, press Ctrl+C in the terminal you had open.

### Mac

1. Run this command in the terminal:
   ```
   sh run.sh
   ```
2. A webpage should open automatically with two text boxes and instructions on how to enter data
3. Press the "Plot graph" button
4. When you are done, press Ctrl+C in the terminal you had open.

## Examples

### #1
![img1](https://github.com/user-attachments/assets/f3e1e6c2-be09-4a80-a88f-433a2e7cec12)

### #2
![img2](https://github.com/user-attachments/assets/784a9b01-300b-48a3-a5bb-c48ccddac226)

### #3
![img3](https://github.com/user-attachments/assets/b3101ccd-82f1-4f8a-bf9a-9aa3a6f4c49b)

### #4
![img4](https://github.com/user-attachments/assets/06b0eaec-5c65-4659-b6cb-e318f41b0144)
