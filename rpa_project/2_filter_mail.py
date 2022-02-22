import mailbox
import smtplib
from imap_tools import MailBox
from account import *

applicant_list = []



with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1
    for msg in mailbox.fetch('(SENTSINCE 08-Feb-2022)'): # 2022년 2월 8일 이후로 온 메일 조회
        if "파이썬 특강" in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            print(f"순번 : {index} 닉네임 : {nickname} 전화번호 : {phone}")
            applicant_list.append((msg, index, nickname, phone))
            index += 1

# for applicant in applicant_list:
#     print(applicant)