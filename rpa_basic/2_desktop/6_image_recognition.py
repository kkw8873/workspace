import pyautogui
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# debug = pyautogui.locateOnScreen("debug.png")
# pyautogui.moveTo(debug)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration=0.25)

# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)

# debug = pyautogui.locateOnScreen("debug.png")
# pyautogui.moveTo(debug)

# 속도 개선
# 1. GrayScale

# debug = pyautogui.locateOnScreen("debug.png", grayscale=True)
# pyautogui.moveTo(debug)

# 2. 범위 지정
# debug = pyautogui.locateOnScreen("debug.png", region=(1014, 762, 1281 - 1014, 818 - 762))
# pyautogui.moveTo(debug)

# 3. 정확도 조정
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.9) # 90%
# pyautogui.moveTo(run_btn)


# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
#file_menu_notedpad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notedpad:
#     pyautogui.click(file_menu_notedpad)
# else:
#     print("발견 실패")
# while file_menu_notedpad is None:
#     file_menu_notedpad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")

# pyautogui.click(file_menu_notedpad)
# 2. 일정 시간동안 기다리기
import time
import sys

# timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정
# file_menu_notedpad = None
# while file_menu_notedpad is None:
#     file_menu_notedpad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout: # 지정한 10초 초과하면
#         print("시간 종료")
#         sys.exit()
def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target




def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found({img_file}) Terminate program.")
        sys.exit()

# pyautogui.click(file_menu_notedpad)

my_click("file_menu_notepad.png", 2)
