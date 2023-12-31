# Setup guide
### 1. 
To get started, you'll need to make sure that C++ is installed. Next, you'll want to have anaconda. You can download this from [here](https://www.anaconda.com/download#windows)

### 2. Open VS Code
Use CTRL + SHIFT + P to open the settings

### 3. Python: Select Interpreter
Search for “Select Interpreter” and click on the “Python: Select Interpreter” option. If you have previously used the environment or interpreter it will probably appear in the palette drop-down.


### 4. To use Anaconda with VSC
 you can also change the workspace settings so your project uses the Anaconda tools. To do this open the VSC settings and (CTRL + SHIFT + P) and type “settings”. Then select “Open Workspace Settings (JSON). This will create a new directory (.vscode) and an empty JSON file (settings.json) in your code directory.
Edit settings.json by adding these lines of code.
```
{
    "python.pythonPath": "C:\\Users\\<your-user-nameL\\anaconda3\\envs\\<your-conda-env>\\python.exe",
    "python.terminal.activateEnvironment": true,
    "terminal.integrated.shell.windows": "C:\\Windows\\System32\\cmd.exe",
}
```
### 5. setting up venv and install rasa
```
conda create --name NAME python==3.8
conda activate NAME

python -m pip uninstall pip
python -m ensurepip
python -m pip install -U pip
pip install rasa
```
