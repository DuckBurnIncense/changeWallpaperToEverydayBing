import urllib.request
import win32api
import win32con
import win32gui
from os import path
from os import mkdir
import json
from PIL import Image

#设置temp路径
tempPath = "C:\\Temp\\"
#判断temp路径是否存在, 如不存在则创建
if(path.exists(tempPath) != True):
    mkdir(tempPath)
#下载图片
response = urllib.request.urlopen("https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN")
jsonByte = str(response.read().decode('utf-8'))
jsonData = json.loads(jsonByte)
imageSavePath = tempPath + "bgImage.jpg"
imageUrl = "https://cn.bing.com/" + jsonData['images'][0]['url']
urllib.request.urlretrieve(imageUrl, imageSavePath)
#再打开->保存(我也不知道为啥要这么做, 但不这么做就报错:
#pywintypes.error: (0, 'SystemParametersInfo', 'No error message is available')
img = Image.open(imageSavePath)
img.save(imageSavePath)
#设置壁纸
regKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
win32api.RegSetValueEx(regKey,"WallpaperStyle", 0, win32con.REG_SZ, "2")
win32api.RegSetValueEx(regKey, "TileWallpaper", 0, win32con.REG_SZ, "0")
win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, imageSavePath, win32con.SPIF_SENDWININICHANGE)
#成功
print("success")
