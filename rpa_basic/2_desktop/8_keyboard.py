import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0] #메모장 1개 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("NadoCoding", interval=0.25)
# pyautogui.write("나도코딩")

# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"], interval=0.25)
# t e s t순서대로 적고 왼쪽2번,오른쪽 1번 l a 순서대로 적고 엔터

# 특수 문자
# shift 4 > $
# pyautogui.keyDown("shift") # shift 키를 누른 상태에서
# pyautogui.press("4") # 4 입력
# pyautogui.keyUp("shift") # shift 떄기

# 조합키(hot key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") # press("a")
# pyautogui.keyUp("ctrl")

# 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# ctrl > alt> shift>a> 다시 역순으로 때기
# pyautogui.hotkey("ctrl", "a")

import pyperclip # pip install pyperclip 클립보드!
# pyperclip.copy("나도코딩") # 나도코딩 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl", "v")

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("나도코딩")

# 자동화 프로그램 종료
# win : ctrl + alt + del
# mac : cmd + shift + option + q
