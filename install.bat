@echo off
cls
color 5
echo [INSTALLER] Beginning installation of requirements.
timeout 1 >null
pip install -r requirements.txt
echo [INSTALLER] Installed all requirements, deleting file and starting odur x.
timeout 1 >null
start main.py
del %0
