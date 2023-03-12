# PandasGUI Packaging
This repo briefly introduces how one can build a standalone spreadsheet app [PandasGUI](https://github.com/adamerose/PandasGUI), which is a Python package designed by [Adam Rose](https://github.com/adamerose).

# How to Install PandasGUI on Windows and Linux
It's pretty simple. Just install it using pip.
```shell
pip install pandasgui
```
For more information, please refer to the author's [repo](https://github.com/adamerose/PandasGUI#installation)


# How to Install PandasGUI on AppleSilicon Macs (The Order Matters)

1. Install dependencies from conda-forge
```shell
conda install pandas PyQt PyQtWebEngine plotly wordcloud setuptools appdirs ipython pyarrow astor typing-extensions openpyxl
```

2. Install dependencies using pip
```shell
pip install pynput
pip install qtstylish --no-deps
```

3. Install PandasGUI from the master branch
```shell
pip install git+https://github.com/adamerose/pandasgui.git --no-deps
```

# Building the executable
Once you have installed all the dependencies above, you can build the standalone app by running the "build.py" script.
```shell
python build.py
```
That's all. Now the app should be created in the "dist" folder with the name "PandasGUIbyAdamRose".
