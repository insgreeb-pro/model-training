@echo off

set version=3.7.4
set main=training_model_rf_ann.py

curl -O https://bootstrap.pypa.io/get-pip.py

@REM PYTHON 32bit
curl -O https://www.python.org/ftp/python/%version%/python-%version%-embed-win32.zip

mkdir py32
tar -xf python-%version%-embed-win32.zip -C py32
copy *.py py32
copy requirements.txt py32

cd py32
python get-pip.py
for %%f IN (.\*._pth) DO @echo import site>> %%f
python -m pip install -r requirements.txt
cd ..

@REM PYTHON 64bit
curl -O https://www.python.org/ftp/python/%version%/python-%version%-embed-amd64.zip

mkdir py64
tar -xf python-%version%-embed-amd64.zip -C py64
copy *.py py64
copy requirements.txt py64

cd py64
python get-pip.py

for %%f IN (.\*._pth) DO (@echo import site>> %%f)
python -m pip install -r requirements.txt
cd ..

@REM cleaning
del python-%version%-embed-win32.zip
del python-%version%-embed-amd64.zip
del get-pip.py

@REM Runner
copy %main% app.py
@echo @echo off>>run32.cmd
@echo @echo off>>run64.cmd
@echo @echo off>>run.cmd

@echo color 0a>>run32.cmd
@echo color 0a>>run64.cmd
@echo color 0a>>run.cmd

@echo type assets\figlet.txt>>run32.cmd
@echo type assets\figlet.txt>>run64.cmd
@echo type assets\figlet.txt>>run.cmd

@echo py32\python app.py>>run32.cmd
@echo py64\python app.py>>run64.cmd
@echo python app.py>>run.cmd

@echo pause>>run32.cmd
@echo pause>>run64.cmd
@echo pause>>run.cmd
