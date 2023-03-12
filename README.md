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
