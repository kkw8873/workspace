from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

txt= Text(root, width=30, height=5) # 얘는 여러줄 엔터 쌉가능
txt.pack()
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30) # 얘는 한줄 (ex:로그인 엔터불가능)
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    #내용 출력
    print(txt.get("1.0", END)) # 1 : 첫번쨰 라인, 0 : 0번째 컬럼 위치
    print(e.get())


    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)



btn = Button(root, text="클릭", command=btncmd)
btn.pack()







root.mainloop()