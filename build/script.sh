#!/bin/bash

echo *** Step 1 ***
echo Install dependencies and build
function install_dep_ubuntu() {
    sudo apt install -y python3-venv 
}
function install_dep_rh {
    sudo yum install -y python3-venv 
}
if [ install_dep_ubuntu 2> /dev/null ]; then
    install_dep_rh
fi
pip install -r requirements.txt


echo *** Step 2 ***
echo Start Python Virtual ENV
python3 -m venv .
source bin/activate


echo *** Step 3 ***
echo Run app as background daemon with no hang-ups (not tied to a terminal session)
nohup python.exe -u ./app.py &


echo *** Step 4 ***
echo Test with test data
cp test_data.csv monitor/