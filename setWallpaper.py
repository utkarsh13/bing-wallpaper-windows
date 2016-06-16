# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:00:03 2016

@author: Utkarsh Rastogi
"""

import os
 
def setWallpaper(path):
    cmd = 'REG ADD \"HKCU\Control Panel\Desktop\" /v Wallpaper /t REG_SZ /d \"%s\" /f' %path
    os.system(cmd)
    os.system('rundll32.exe user32.dll, UpdatePerUserSystemParameters')
    return
 
if __name__ == "__main__":
    path = r'C:\Users\Utkarsh Rastogi\Pictures\pic.jpg'
    setWallpaper(path)
