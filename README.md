# PandasGUI Packaging
This repo briefly introduces how one can build a standalone spreadsheet app [PandasGUI](https://github.com/adamerose/PandasGUI), which is a Python package designed by [Adam Rose](https://github.com/adamerose).


# Install PandasGUI
## For Windows and Linux users
It's pretty simple. Just install it using pip.
```shell
pip install pandasgui
```
For more information, please refer to the author's [repo](https://github.com/adamerose/PandasGUI#installation)


# For AppleSilicon Macs
1. Install dependencies from conda-forge
```shell
conda install -c conda-forge pandas PyQt PyQtWebEngine plotly wordcloud setuptools appdirs ipython pyarrow astor typing-extensions openpyxl
```

2. Install other dependencies using pip
```shell
pip install pynput
pip install qtstylish --no-deps
```

3. Install the latest PandasGUI from the master branch
```shell
pip install git+https://github.com/adamerose/pandasgui.git --no-deps
```


# Install PyInstaller
For Mac users, installing PyInstaller from conda-forge is recommended
```shell
conda install -c conda-forge PyInstaller
```

For Windows and Linux users, it's ok to use pip
```shell
pip install PyInstaller
```
or
```shell
conda install PyInstaller
```


# Building the executable
Once you have installed all the dependencies above, you can build the standalone app by running the "build.py" script.
```shell
python build.py
```
That's all. Now the app should be created in the "dist" folder with the name "PandasGUIbyAdamRose".
