# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 23:39:38 2016

@author: Utkarsh Rastogi
"""

import os

def main():
    
    #get username
    username = os.environ.get( "USERNAME" )        
    file_path = "C:\Users\\" + username + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    file_name = "bing wallpaper.bat"    
    
    complete_name = os.path.join(file_path, file_name)
     
    # delete only if file exists 
    if os.path.exists(complete_name):
        os.remove(complete_name)
        print "Service is removed from startup services successfully."

if __name__ == "__main__":
    main()
