# 크레벅스 상품 자동업데이트

from selenium import webdriver # 셀레니움과 웹드라이버 부르는 모듈함수 
#from random import *
import time

#random_num = randint(3,7) # 랜덤 시간 지연


driver = webdriver.Chrome('D:\/chromedriver.exe') # 제어하기 위해 변수 선언

url = "https://www.crebugs.com/member/login.php" # 이동할 링크주소를 변수에 저장

driver.get(url) # 해당 링크로 이동`


# ID

xpath = "//input[@placeholder='E-mail']" # 입력(검색)버튼, // input[@id='srch']에다가 "" 로감싸야함
input_search = driver.find_element_by_xpath(xpath)
input_search.send_keys("******@naver.com") # id 입력


# passwd

xpath2 = "//input[@placeholder='Password']" # 입력(검색)버튼, // input[@id='srch']에다가 "" 로감싸야함
input_search = driver.find_element_by_xpath(xpath2)
input_search.send_keys("***********") # pwd 입력


# 로그인 클릭
xpath3 = "//input[@class='btn_login']" # x 버튼, //button[@class='closeBtn']에다가 "" 로감싸야함
login = driver.find_element_by_xpath(xpath3) # driver 즉,chrome으로 요소를 찾아서 x창을 끈다.
login.click() # 변수명.click() 클릭하는 소스


# 조금 지연해줘야 인식됨.
time.sleep(1)

# 고승률마티보장(닉네임) = 마이페이지 클릭
xpath4 = "/html/body/div[1]/header/div/div/div/div[3]/a/strong"
driver.find_element_by_xpath(xpath4).click()


# 판매관리 클릭.
xpath5 = "/html/body/div[1]/div[2]/div[1]/nav/div[3]/div"
driver.find_element_by_xpath(xpath5).click()


# 재능 등록/관리  클릭.
xpath6 = "/html/body/div[1]/div/div[1]/nav/div[3]/ul/li[1]/a"
driver.find_element_by_xpath(xpath6).click()


# 여기서 무한루프
while True :
        
    # 재능관리에서 판매 -> 중지 진행버튼
    xpath7 = "/html/body/div[1]/div/div[2]/ul/li/div[2]/div[1]/div/a[2]"
    driver.find_element_by_xpath(xpath7).click()


    # 팝업창 종료
    #  "판매상태가 변경되었습니다" alert(경고)창의 '확인'을 클릭합니다.
    time.sleep(1)
    #print(random_num)
    alert = driver.switch_to.alert
    alert.accept() #경고창 확인 클릭