import win32gui
import win32con
import win32clipboard as w
import time
import datetime
while True:
  time_now = datetime.datetime.now()
  if time_now == "0:41:10":
    # 发送的消息
    msg = "测试代码"
    # 窗口名字
    name = "Nothing"
    # 将测试消息复制到剪切板中
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
    w.CloseClipboard()
    # 获取窗口句柄
    handle = win32gui.FindWindow(None, name)
    # while 1==1:
    if 1 == 1:
        # 填充消息
        win32gui.SendMessage(handle, 770, 0, 0)
        # 回车发送消息
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)