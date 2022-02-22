import time
import keyboard
from PIL import ImageGrab
def screenshot():
    # 2020년 6월 1일 10시 20분 30초 - > _20200601_102030
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time)) # img_20200601_102030.png


keyboard.add_hotkey("F9", screenshot) # 사용자가 F9 키를 누르면 스크린 샷 저장
# keyboard.add_hotkey("a", screenshot) a 가능
# keyboard.add_hotkey("ctrl+shift+S", screenshot) 여러개의 키를 한꺼번에 누르는것도 가능

keyboard.wait("esc") # 사용자가 esc를 누를 때 까지 프로그램 수행

# # 이건 pyautogui 로 해본거
# import pyautogui

# def shot():
#     cur_time = time.strftime("_%Y%m%d_%H%M%S")
#     img = pyautogui.screenshot()
#     img.save("screenshot{}.png".format(cur_time)) #파일로 저장

# keyboard.add_hotkey("F1", shot)

# keyboard.wait("esc")