# Setup guide
To get started, you'll need to make sure that C++ is installed.
Next, you'll want to have anaconda. You can download this from [here](https://www.anaconda.com/download#windows)

Open VS Code
Use CTRL + SHIFT + P to open the settings
Search for “Select Interpreter” and click on the “Python: Select Interpreter” option (see image below). If you have previously used the environment or interpreter it will probably appear in the palette drop-down.
![alt text]([http://url/to/img.png](https://opensourceoptions.com/wp-content/uploads/2022/02/select_interp.png?ezimgfmt=ng:webp/ngcb1))

To use Anaconda with VSC you can also change the workspace settings so your project uses the Anaconda tools. To do this open the VSC settings and (CTRL + SHIFT + P) and type “settings”. Then select “Open Workspace Settings (JSON). This will create a new directory (.vscode) and an empty JSON file (settings.json) in your code directory.
Edit settings.json by adding these lines of code.
```
{
    "python.pythonPath": "C:\\Users\\<your-user-nameL\\anaconda3\\envs\\<your-conda-env>\\python.exe",
    "python.terminal.activateEnvironment": true,
    "terminal.integrated.shell.windows": "C:\\Windows\\System32\\cmd.exe",
}
```
