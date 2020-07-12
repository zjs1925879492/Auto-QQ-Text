import time
from pynput.mouse import Controller as msctrl
from pynput.mouse import Button
from pynput.keyboard import Controller
ms=msctrl()
def kb(text):           #控制键盘的函数
    keyboard=Controller()
    keyboard.type(text)
def main(times,sntns):        #主函数
    for emmm in range(times):
        kb(sntns+str(emmm))
        #kb(sntns)
        ms.press(Button.left)
        ms.release(Button.left)
        time.sleep(0.05)   #间隔时间
    return 'Done!'
times=int(input('输入次数'))
sntns=input('输入文字。5秒后开始发送，请把鼠标移到‘发送’键上！')
time.sleep(5)
main(times,'జ్ఞ ా رً ॣ'+sntns)             #特殊字符发到QQ群里别人看不见，悄无声息刷龙王
input('完成！回车退出')

'''
资料来自https://www.bilibili.com/video/BV137411B7Ty
更多欢乐加QQ群https://jq.qq.com/?_wv=1027&k=JGIrfbS4                        
'''