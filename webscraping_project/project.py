import re
import requests
from bs4 import BeautifulSoup

# [오늘의 날씨]
# 흐림, 어제보다 OO° 높아요
# 현재 OO℃ (최저 OO° / 최고 OO°)
# 오전 강수확률 OO% / 오후 강수확률 OO%

# 미세먼지 보통
# 초미세먼지 보통
# 자외선 좋음

def create_sup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status
    soup = BeautifulSoup(res.text, "lxml")
    return soup 




def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EC%95%88%EC%96%91%EC%8B%9C+%EB%82%A0%EC%94%A8&oquery=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EC%95%88%EC%96%91%EB%82%A0%EC%94%A8&tqi=hQ6BWwprvmsssBuhPLCssssssbd-180891"
    res = requests.get(url)
    res.raise_for_status
    soup = BeautifulSoup(res.text, "lxml")
    # 흐림, 어제보다 OO° 높아요
    cast = soup.find("p", attrs={"class":"summary"}).get_text()
    # 현재 OO℃ (최저 OO° / 최고 OO°)
    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().strip()

    # today = soup.find("li", attrs={"class":"week_item today"})
    min_temp = soup.find("span", attrs={"class":"lowest"}).get_text()
    max_temp = soup.find("span", attrs={"class":"highest"}).get_text()

    # 오전 강수확률 OO% / 오후 강수확률 OO%
    moning_rain_rate = soup.find_all("span", attrs={"class":"weather_left"})[0].get_text().strip()
    afternoon_rain_rate = soup.find_all("span", attrs={"class":"weather_left"})[1].get_text().strip()

    # 미세먼지 보통
    # 초미세먼지 보통
    #soup.find("ul", attrs={"class":"today_chart_list"}, text=["미세먼지", "초미세먼지"]).get_text().strip() 텍스트가 미세먼지거나 초미세먼지를 싹다 리턴
    #soup.find("ul", attrs={"class":"today_chart_list", "li" = "~~~"}).get_text().strip() 모든 조건에 해당하는 값 리턴
    #soup.find("ul", attrs={"class":["today_chart_list","hi"]}).get_text().strip()
    #위의 3형식처럼 쓸수있음 되게 많이 쓸뜻 알아둘것!
    dust = soup.find("ul", attrs={"class":"today_chart_list"})
    pm10 = dust.find_all("li")[0].get_text().strip()
    pm25 = dust.find_all("li")[1].get_text().strip()




     # 출력
    print(f"{cast}")
    print(f"{curr_temp}({min_temp} / {max_temp})".ljust(2))
    print(f"{moning_rain_rate} / {afternoon_rain_rate}")
    print()
    print(pm10)
    print(pm25)
    print()



def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://www.yonhapnewstv.co.kr/news/headline"
    soup  = create_sup(url)
    news_list = soup.find("ul", attrs={"class":"article article-headLine02"}).find_all("li", limit=3)
    for idx, news in enumerate(news_list):
        title = news.find("strong").get_text().strip()
        link = "https://www.yonhapnewstv.co.kr/" + news.find("a")["href"]
        # print("{}. {}".format(idx+1, title))
        print(f"{idx+1}. {title}")
        print("  (링크: {})".format(link))
        print()

def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup  = create_sup(url)
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)
    for idx, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1 # img 태그가 있으면 1번째 a태그의 정보를 사용


        title = news.find_all("a")[a_idx].get_text().strip()
        link = news.find("a")["href"]
        print(f"{idx+1}. {title}")
        print("  (링크: {})".format(link))
        print()

def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_lec/lec_study/lec_I_others_english&keywd=haceng_submain_lnb_lec_I_others_english&logger_kw=haceng_submain_lnb_lec_I_others_english"
    soup = create_sup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]: # 8문장이 있다고 가정할 때, index기준4~7까지 잘라서 가져옴
        print(sentence.get_text().strip())
    
    print()
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]: # 8문장이 있다고 가정할 때, index기준0~3까지 잘라서 가져옴
        print(sentence.get_text().strip())
        




if __name__ == "__main__": #외부에서 모듈쓰는지 직접쓰는지 구분할수있음
    scrape_weather() # 오늘의 날씨 정보 가져오기
    #scrape_headline_news() #연합뉴스 헤드라인 뉴스 정보 가져오기
    #scrape_it_news() #네이버 IT 뉴스 정보 가져오기
    #scrape_english() # 오늘의 영어 회화 가져오기
    

