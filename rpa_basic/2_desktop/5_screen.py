import pyautogui
# 스샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") #파일로 저장

# pyautogui.mouseInfo()
# 974,14 33,139,211 #218BD3


pixel = pyautogui.pixel(974, 14)
print(pixel)

# print(pyautogui.pixelMatchesColor(974, 14, (33,139,211)))
# print(pyautogui.pixelMatchesColor(974, 14, pixel))
print(pyautogui.pixelMatchesColor(974, 14, (33,139,233)))