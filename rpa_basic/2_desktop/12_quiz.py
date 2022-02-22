import pyautogui
import pyperclip

pyautogui.hotkey("win", "r")
pyautogui.write(["mspaint", "enter"], interval=0.25)
#pyautogui.press("enter") # 엔터키 입력

windows = pyautogui.getWindowsWithTitle("그림판")[0]
if windows.isMaximized == False:
    windows.maximize() 

pyautogui.sleep(1)
text = pyautogui.locateOnScreen("text.png") # text.png.left -200 , text.png.top + 200 등 상대좌표설정가능
pyautogui.click(text, duration=0.3)

pyautogui.click(400, 300, duration=0.3)

pyperclip.copy("참 잘했어요")
pyautogui.hotkey("ctrl", "v")

# 5초 대기
pyautogui.sleep(5)
# 프로그램 종료
windows.close()
pyautogui.sleep(0.3)
pyautogui.press("n") # 저장 안 함 

# 내가한거
# ex = pyautogui.locateOnScreen("ex.png")
# pyautogui.click(ex)
# not_save = pyautogui.locateOnScreen("not_save.png")
# pyautogui.click(not_save)
        
