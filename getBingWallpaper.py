# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 21:51:51 2016

@author: Utkarsh Rastogi
"""

from setWallpaper import setWallpaper
from bs4 import BeautifulSoup
import requests
import datetime
import urllib
import os
from time import sleep

bing_path = 'http://www.bing.com'
bing_url = 'http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=ru-RU'

def main():
    
    try:
        #extracting url of bing image 
        req = requests.get(bing_url)
        soup = BeautifulSoup(req.text,'lxml')
        soup_url = soup.find('url').text
        url = bing_path + soup_url
    except:
        print "Connection Error. Check your connection and try again."
        sleep(5)
        exit()
    
    #extracting time and setting name of bing image
    time = datetime.datetime.now()
    wp_name = 'bing ' + time.strftime('%d-%m-%y') + '.jpg'
    
    #setting target directory as a folder in desktop
    username = os.environ.get( "USERNAME" )
    target_dir = 'C:\Users\\' + username + '\Desktop\\bing\\'
    
    #creating target directory if not present
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    pic_path = target_dir + wp_name

    try:
        print "Downloading Bing Wallpaper."
        #downloading image to set path
        urllib.urlretrieve(url, pic_path)
        print "Setting Bing Wallpaper as Desktop Background."
        #setting downloaded pic as wallpaper
        setWallpaper(pic_path)
        print "Desktop Backgroung is set."
    except:
        print "Unable to retrieve Bing image."
        sleep(5)
        exit()

if __name__ == "__main__":
    main()
