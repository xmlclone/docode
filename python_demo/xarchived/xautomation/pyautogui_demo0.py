"""
pip install pyautogui
pip install opencv-python
pip install pillow

https://pypi.org/project/PyAutoGUI/
https://github.com/asweigart/pyautogui/blob/master/docs/simplified-chinese.ipynb
"""


import pyautogui


# # 屏幕大小
# print(f'{pyautogui.size()=}')
# # 当前鼠标位置
# print(f'{pyautogui.position()=}')

# # 移动到指定的位置后单击(屏幕左上角是0,0)，下面的位置大概就是windows徽标的位置
# pyautogui.moveTo(10, pyautogui.size().height - 10)
# pyautogui.click()

# # 输入内容，每个字符的输入之间会间隔0.25s
# pyautogui.typewrite('Hello, world!', interval=0.25)

# # 模拟按键
# pyautogui.press('esc')

# # 慢慢的移动过去，大概耗时3s
# pyautogui.moveTo(1800, 500, duration=3)


# # 下面是一个模拟打开文本文件的一些操作
# pyautogui.moveTo(138, 30)
# pyautogui.doubleClick()
# pyautogui.typewrite('hello, world!', interval=0.25)
# pyautogui.press('esc')
# pyautogui.keyDown('shift')
# pyautogui.press(['left', 'left', 'left', 'left'], interval=0.25)
# pyautogui.keyUp('shift')
# pyautogui.hotkey('ctrl', 'c')
# pyautogui.hotkey('ctrl', 'v')


# 根据图片定位屏幕内容
loc = pyautogui.locateOnScreen('1.png', confidence=0.6)
print(f'{loc=}')
x, y = pyautogui.center(loc)
pyautogui.doubleClick(x, y)