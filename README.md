# 将桌面壁纸改为bing每日一图

**使用方法:** 直接下载并双击运行"changeWallpaperToEverydayBing.exe"

## 以下是源码说明:

**用到的库:**

urllib.request   (似乎py自带)

pywin32

json  (似乎py自带)

PIL

**用到的库的安装方法:**

```
pip install pywin32

pip install Pillow
```

**为什么要用到pillow**

我也不知道, 但不再次保存就会报如下错误

```
Traceback (most recent call last):
  File "C:\Users\DuckBurnIncense\Desktop\changeWallpaperToEverydayBing.py", line 30, in <module>
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, imageSavePath, win32con.SPIF_SENDWININICHANGE)
pywintypes.error: (0, 'SystemParametersInfo', 'No error message is available')
```

<del>看网上说图片必须是bmp格式?</del>

**编译说明:**

有个很离谱的兼容性问题,

win10/11编译的exe无法在win7上运行, 各种报dll丢失.

(所以我得在10上写好代码, 扔7虚拟机里编译(但有时10可以正常跑的程序, 7就不行, 如上面的pillow, 用不用pillow 10都不报错, 但7必须用, 否则就报错))

**编译方法:**

```
pip install pyinstaller

pyinstaller -F -w "C:\Users\DuckBurnIncense\Desktop\changeWallpaperToEverydayBing.py"
```

