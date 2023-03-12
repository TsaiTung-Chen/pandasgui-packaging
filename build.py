#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 23:52:26 2023

@author: tungchentsai
"""

import os
import platform
from PyInstaller.__main__ import run


ROOT = os.path.realpath(os.getcwd())
PLATFORM = platform.system()

icon_path = os.path.join(ROOT, r"icon.icns")

if PLATFORM == 'Darwin':  # macOS
    sep = r":"
    qt_conf_src_path = os.path.join(
        ROOT,
        "Qt Configs",
        "Mac",
        "qt.conf"
    )
elif PLATFORM == 'Windows':  # not tested yet
    sep = r";"
    qt_conf_src_path = os.path.join(
        ROOT,
        "Qt Configs",
        "Others",
        "qt.conf"
    )
else:  # not tested yet
    sep = r":"
    qt_conf_src_path = os.path.join(
        ROOT,
        "Qt Configs",
        "Others",
        "qt.conf"
    )


run([
    r"run.py",
    '--hidden-import', 'PyQt5.QtPrintSupport',
    '--hidden-import', 'qtstylish.compiled.qtstylish_rc',
    '--hidden-import', 'openpyxl.cell._writer',
    '--collect-data', 'pandasgui',
    '--collect-data', 'PyQt5',
    '--collect-data', 'qtstylish',
    '--add-data', f"{qt_conf_src_path}{sep}.",
    '--specpath', "./build",
    '--clean',
    '--name', 'PandasGUIbyAdamRose',
    '--noconsole',
    '--icon', icon_path
])

