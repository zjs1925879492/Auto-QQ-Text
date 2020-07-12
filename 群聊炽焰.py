#依赖于pywin32库，请记得pip install pywin32

import time
import win32clipboard as w 
import win32gui,win32con

def setText(aString):
    '''将要发送的文字复制的函数'''
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

def send_Mess(hwnd):
    '''粘贴并回车发送的函数'''
    win32gui.PostMessage(hwnd,win32con.WM_PASTE, 0, 0)
    time.sleep(0.3)
    win32gui.PostMessage(hwnd,win32con.WM_KEYDOWN,win32con.VK_RETURN,0)  
    win32gui.PostMessage(hwnd,win32con.WM_KEYUP,win32con.VK_RETURN,0)

windowtitle = '生产龙王无限公司'        #窗口标题，修改成你QQ群聊的名字（注意！！！打开多个聊天窗口时标题会变成xx等x个会话，会导致错误）
hwnd = win32gui.FindWindow(None, windowtitle)         #按窗口标题寻找窗口句柄
while True:
    if hwnd>0:
        print('找到%s'%windowtitle)
        now= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))            #此条信息发送的时间
        setText('定时发送信息（维持群聊炽焰） 测试时间：'+now)
        #定时发送信息（维持群聊炽焰） 测试时间：xxxx-xx-xx xx：xx
        send_Mess(hwnd)
        time.sleep(600)       #等待600秒，即10分钟，可自定义时间，也可调短刷龙王
    else:
        print('没找到%s'%windowtitle)

'''
hwnd_title = dict()
def get_all_hwnd(hwnd,mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd:win32gui.GetWindowText(hwnd)})
win32gui.EnumWindows(get_all_hwnd, 0)
   
for h,t in hwnd_title.items():
    if t is not "":
        print(h, t)
'''
#如果你仍然没有成功获得窗口句柄，可以使用此段代码打印出当前所有窗口标题名与句柄
#强烈推荐配合挂机宝使用，安利一个挂机宝平台3.5元一个月1314qq.top，资料来自https://www.bilibili.com/video/av370733049，更多欢乐请加QQ群https://jq.qq.com/?_wv=1027&k=JGIrfbS4                        