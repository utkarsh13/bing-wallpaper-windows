# bing-wallpaper-windows
It is a python script that sets the daily Bing picture as a Desktop Wallpaper on Windows.
It adds a service to startup which automatically runs the script on system startup.

### Language used:
The script is made using python 2.7

### List of libraries used:
* bs4 (BeautifulSoup)
* requests
* urllib

### How to use:
#### To set desktop background if you dont want to use startup service.
Open the command prompt and run getBingWallpaper.py.
```
cd (path of directory where files are present)
python getBingWallpaper.py
```
#### To add startup service.
Open the command prompt and type following commands.
```
cd (path of directory where files are present)
python addStartupService.py
```
#### To remove startup service.
Open the command prompt and type following commands.
```
cd (path of directory where files are present)
python removeStartupService.py
```

### Testing:
The program is successfully tested in Windows 8.
