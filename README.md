# Bidnamics Coding Challenge

** Version 1.0.0 **

Application responsible for monitoring a directory for new CSV files. Each file will get monitored & processed and output file will get generated based on the timestamp.

# How to use

Python virtual environment
Install requirements
App starter: app.py
Monitored dir: monitor

# Get started

pip install -r requirements.txt
sudo apt install -y python3-venv # for Ubuntu
sudo yum install -y python3-venv # for RedHat
python3 -m venv .
source bin/activate
nohup python.exe -u .\app.py & # run as background daemon
cp test_data.csv monitor/

# How it works

File System event handler is observed by an instance of the Observer class. A callback function “on_created” will get executed on new files only, and the function will begin the read process.

The read function is responsible for reading the CSV data and calculating the ROAS to create a file based on the timestamp.

The script will first check if the directory path exists. Once the file is created, the write function will append the CSV data onto the new file.

# Issues
