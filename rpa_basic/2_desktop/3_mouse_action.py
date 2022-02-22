import pyautogui

# pyautogui.sleep(3) #3초 대기 1024, 19
# print(pyautogui.position())

# pyautogui.click(1024, 17, duration=1) # 1초동안 좌표로 이동후 클릭
# pyautogui.click()
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks=500)

# pyautogui.moveTo(200,200)
# pyautogui.mouseDown() # 마우스 누른 상태
# pyautogui.moveTo(300, 300)
# pyautogui.mouseUp() # 마우스 땐 상태

pyautogui.sleep(3) #3초 대기 1024, 19
# pyautogui.rightClick()
# pyautogui.middleClick()

#print(pyautogui.position())
# pyautogui.moveTo(938, 410)
# # pyautogui.drag(100, 0) # 현재위치 기준으로 드래그
# pyautogui.drag(100, 0, duration=0.25) # 너무 빠른 동작으로 drag 수행이 안될때는 duration 사용!
# pyautogui.dragTo(1338, 410, duration=0.25) # 절대 좌표 기준으로 드래그

pyautogui.scroll(-800) # 위 방향으로 300만큼 스크롤 -300 이면 아래방향으로 스크롤