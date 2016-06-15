# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:00:03 2016

@author: Utkarsh Rastogi
"""

import ctypes
import win32con
 
def setWallpaper(path):
    # This code is based on the following two links
    # http://mail.python.org/pipermail/python-win32/2005-January/002893.html
    # http://code.activestate.com/recipes/435877-change-the-wallpaper-under-windows/
    cs = ctypes.c_buffer(path)
    ctypes.windll.user32.SystemParametersInfoA(win32con.SPI_SETDESKWALLPAPER, 0, cs, 0)
 
if __name__ == "__main__":
    path = r'C:\Users\Utkarsh Rastogi\Pictures\pic.jpg'
    setWallpaper(path)