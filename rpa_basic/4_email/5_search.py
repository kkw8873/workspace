from imap_tools import MailBox
from account import *

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")
# mailbox.logout() with쓰면 이거 필요없음


with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    #전체 메일 다 가져오기
    # for msg in mailbox.fetch(limit=5, reverse=True): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 읽지 않은 메일만 가져오기
    # for msg in mailbox.fetch('(UNSEEN)', limit=5): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정인이 보낸 메일 가져오기
    # for msg in mailbox.fetch('(FROM kyu8873@gmail.com)', limit=3, reverse=True): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 어떤 글자를 포함하는 메일(제목, 본문)
    # for msg in mailbox.fetch('(TEXT "test mail")', limit=5): 
    #     print("[{}] {}".format(msg.from_, msg.subject))
    
    # 어떤 글자를 포함하는 메일(제목만)
    # for msg in mailbox.fetch('(SUBJECT "test mail")', limit=5):
    #     print("[{}] {}".format(msg.from_, msg.subject))
    
    # 한글을 쓰면 오류나서 이렇게 가져와야함
    # for msg in mailbox.fetch(limit=5, reverse=True): 
    #     if "테스트" in msg.subject:
    #         print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 날짜 이후의 메일
    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)', reverse=True, limit=5): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 날짜에 온 메일
    # for msg in mailbox.fetch('(ON 07-Nov-2020)', limit=5): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # # 2가지 이상의 조건을 모두 만족하는 메일
    # for msg in mailbox.fetch('(ON 08-Feb-2022 SUBJECT "test mail")', reverse=True): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 2가지 이상의 조건중 하나라도 만족하는 메일
    for msg in mailbox.fetch('(OR ON 08-Feb-2022 SUBJECT "test mail")', reverse=True): 
        print("[{}] {}".format(msg.from_, msg.subject))
       
    
    
    
    