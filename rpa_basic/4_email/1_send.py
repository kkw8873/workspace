import smtplib
from account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # 연결이 잘 수립되는지 확인
    smtp.starttls() # 모든 내용 암호화되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인


    subject = "test mail" # 메일 제목
    body = "mail body" # 메일 본문

    msg = f"Subject: {subject}\n{body}"
    # 발신자,수신사,정해진 형식의 메세지
    smtp.sendmail(EMAIL_ADDRESS, "kyu8873@gmail.com", msg)

