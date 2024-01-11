@echo on


:: Define the path to your virtual environment's activate script
set "virtualEnvPath=venv\Scripts\activate"

:: Define the path to your Python script
set "pythonScriptPath=win.py"

:: Activate the virtual environment and run the Python script
call "%virtualEnvPath%" && python "%pythonScriptPath%"
