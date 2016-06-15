# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 23:07:01 2016

@author: Utkarsh Rastogi
"""

import getBingWallpaper
import os
import inspect

def main():
    #get username
    username = os.environ.get( "USERNAME" )        
    file_path = "C:\Users\\" + username + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    file_name = "bing wallpaper.bat"
 
    #joining file_path and file_name
    complete_name = os.path.join(file_path, file_name)
    
    #opening file
    bat_file = open(complete_name,"w")
    
    #location of current directory
    cur_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    
    to_write = '''
    cd %s
    python getBingWallpaper.py
    exit
    ''' %cur_dir
    
    #writing to file
    bat_file.write(to_write)
    bat_file.close()
    
    print "Service is added to startup services successfully."
    
    #setting bing wallpaper as desktop background
    getBingWallpaper.main()

if __name__ == "__main__":
    main()
