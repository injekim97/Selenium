# WEB 고속버스터미널 표 티켓팅 매크로_제작

from selenium.webdriver.common.keys import Keys # ★★★ENTER 기능 모듈함수
from selenium import webdriver # 셀레니움과 웹드라이버 부르는 모듈함수 
import time

driver = webdriver.Chrome('F:/파이썬 셀레니옴 저장 장소/chromedriver.exe') # 제어하기 위해 변수 선언

url = "https://www.kobus.co.kr/mrs/rotinf.do" # 이동할 링크주소를 변수에 저장

driver.get(url) # 해당 링크로 이동


# 팝업창 끄기 위한 다른소스 구현
time.sleep(1) # 너무 빠르면 창이 렉걸려서 시간지연 필수
xpath = "//button[@class='remodal-cancel']"
closeBtn = driver.find_element_by_xpath(xpath)
closeBtn.click()



# xpath2 = 출발지 
xpath2 ="//span[@class='empty_txt']"
start_terminal = driver.find_element_by_xpath(xpath2)
start_terminal.click()


# xpath3 = 터미널/지역 이름을 검색하세요
xpath3 ="//input[@id='terminalSearch']"
start_terminal2 = driver.find_element_by_xpath(xpath3) #해당위치를 찾음
start_terminal2.click() # 클릭

driver.find_element_by_xpath(xpath3).send_keys("출발지")
driver.find_element_by_xpath(xpath3).send_keys(Keys.RETURN) # ★★ENTER(엔터기능)



# xpath4 = 도착지

xpath4 ="//input[@id='terminalSearch']"
end_terminal2 = driver.find_element_by_xpath(xpath4) #해당위치를 찾음
end_terminal2.click() # 클릭

driver.find_element_by_xpath(xpath4).send_keys("도착지")
driver.find_element_by_xpath(xpath4).send_keys(Keys.RETURN) # ★★ENTER(엔터기능)






# 가는날 달력 버튼 누르기
xpath5 ="//img[@class='ui-datepicker-trigger']"
time.sleep(1) # 너무 빠르면 창이 렉걸려서 시간지연 필수
driver.find_element_by_xpath(xpath5).click() # click() 함수는 클릭함.



# 달력 클릭해서 날짜 누르기

xpath6 ="/html/body/div[4]/table/tbody/tr[5]/td[1]" # xpath 풀버전 사용
time.sleep(1) # 너무 빠르면 창이 렉걸려서 시간지연 필수
driver.find_element_by_xpath(xpath6).click() # click() 함수는 클릭함.


# 조회하기 버튼 누르기

xpath7 = "/html/body/div[1]/div[4]/div[2]/div[4]/div[1]/div/div/p/button" # xpath 풀버전 ㅏㅅ용
driver.find_element_by_xpath(xpath7).click() # click() 함수는 클릭함.
time.sleep(1) # 너무 빠르면 창이 렉걸려서 시간지연 필수

#승차권 예메에 따른 취소수수료 내용에 동의하십니까? 팝업창이 아니라 경고창임
# Alert(경고창) 으로 처리해야 함. https://dejavuqa.tistory.com/272 << 참고

# alert(경고) 창의 '확인'을 클릭합니다.
alert = driver.switch_to.alert
alert.accept() #경고창 확인 클릭
#time.sleep(2)



# 고속버스 시간 10시10분  예매

xpath8 = "/html/body/div[1]/div[4]/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/p[3]/a/span[1]" # 10:10 분 차
driver.find_element_by_xpath(xpath8).click() # click() 함수는 클릭함.


# alert(경고) 창의 '확인'을 클릭합니다.
alert = driver.switch_to.alert
alert.accept() #경고창 확인 클릭


# alert(경고) 창의 '확인'을 클릭합니다.
time.sleep(1)
alert = driver.switch_to.alert
alert.accept() #경고창 확인 클릭


# "예매하실 매수를 먼저 선택하신 후 좌석을 선택해 주세요". 경고창 확인 클릭
xpath9 = "/html/body/div[1]/div[4]/div[2]/div[3]/div/div[1]/div[2]/span/a"
driver.find_element_by_xpath(xpath9).click() # click() 함수는 클릭함.


# 매수(사람 몇명 인지?) 선택
# ★★★ 여기서는 xpath가 먹히지않아 selector을 이용해서 씀
# ★★★ 변수명 = driver.find_element_by_css_selector("해당 selector 복붙하기")

# 사람 일반 1명 추가 버튼임
btn_add = driver.find_element_by_css_selector("#seatChcPage > div > div.compare_wrap > div.detailBox > div.detailBox_body > div.ticketBox > ul > li:nth-child(1) > div > div > ul > li:nth-child(1) > button")
btn_add.click() # 클릭

 
# 좌석선택
# ★★★★★ xpath ="//태그[@속성='속성값'] 형태 ★★★★★

# 03이 3번을 뜻함
xpath10 ="//label[@for='seatNum_28_20']" # 28번 좌석중 3번선택   ★★★★★ xpath ="//태그[@속성='속성값'] 형태 ★★★★★
driver.find_element_by_xpath(xpath10).click() # click() 함수는 클릭함.



# 좌석선택 완료
xpath11 = driver.find_element_by_css_selector("#satsChcCfmBtn") #selector 이용
xpath11.click()



# -----------------------------------------------------------------------------------------------------------

# 로그인 화면중에 팝업창 뜸 => 팝업창으로 화면 이동

time.sleep(1)

# ID (아이디)

xpath12 = "//input[@id='usrId']" # 입력(검색)버튼, // input[@id='srch']에다가 "" 로감싸야함
input_search = driver.find_element_by_xpath(xpath12)
input_search.send_keys("아이디") # id 입력


# passwd (비밀번호)

xpath13 = "//input[@id='usrPwd']" # 입력(검색)버튼, // input[@id='srch']에다가 "" 로감싸야함
input_search = driver.find_element_by_xpath(xpath13)
input_search.send_keys("비번") # pwd 입력


# 로그인 클릭
xpath14 = "//button[@id='btn_confirm']" # x 버튼, //button[@class='closeBtn']에다가 "" 로감싸야함
login = driver.find_element_by_xpath(xpath14) # driver 즉,chrome으로 요소를 찾아서 x창을 끈다.
login.click() # 변수명.click() 클릭하는 소스


# --------------------------------------------------------------------------------------------------------------
### ★★★ 여기서는 xpath가 먹히지않아 selector을 이용해서 씀
# 아래스크룰바 기능 driver.execute_script("window.scrollTo(0,10000)") # ★ 아래로 스크룰바 쫙 내림 y가 세로내리는길이 +10000은 밑 / -10000 맨 위

# 전체약관 클릭
time.sleep(1) #너무빠르면 실행이 멈춰서 천천히 해줘야함
xpath15 = driver.find_element_by_css_selector("#stplCfmPymFrm > div.page.page_payment.depth3 > div:nth-child(2) > p > span > label")
xpath15.click() # 클릭

# 카드 선택
time.sleep(1) #너무빠르면 실행이 멈춰서 천천히 해줘야함
xpath16 = driver.find_element_by_css_selector("#cardKindList > div > div.selectric > p")
xpath16.click() # 클릭



driver.execute_script("window.scrollTo(0,10000)") # ★ 아래로 스크룰바 쫙 내림 y가 세로내리는길이 +10000은 밑 / -10000 맨 위
time.sleep(1) #너무빠르면 실행이 멈춰서 천천히 해줘야함

# full xpath 사용 (농협)
xpath17 = "/html/body/div[1]/div[4]/div[2]/form[1]/div[4]/div[8]/div[1]/div[1]/div[2]/div/div/div[3]/div/ul/li[8]"
driver.find_element_by_xpath(xpath17).click() # click() 함수는 클릭함.


# 카드 번호
# ★★★★★ 무조건 xpath는 input에 id로 받아야 제대로 인식된다 ★★★★★

# 카드번호 첫번째 자리
xpath18 = "//input[@id='cardNum1']"
driver.find_element_by_xpath(xpath18).click() # click() 함수는 클릭함.

input_search = driver.find_element_by_xpath(xpath18)
input_search.send_keys("****") 

# 카드번호 두 번째 자리
xpath18_2 = "//input[@id='cardNum2']"
driver.find_element_by_xpath(xpath18_2).click() # click() 함수는 클릭함.

input_search = driver.find_element_by_xpath(xpath18_2)
input_search.send_keys("****") 


# 카드번호 세 번째 자리
xpath18_3 = "//input[@id='cardNum3']"
driver.find_element_by_xpath(xpath18_3).click() # click() 함수는 클릭함.

input_search = driver.find_element_by_xpath(xpath18_3)
input_search.send_keys("****") 


# 카드번호 네 번째 자리
xpath18_4 = "//input[@id='cardNum4']"
driver.find_element_by_xpath(xpath18_4).click() # click() 함수는 클릭함.

input_search = driver.find_element_by_xpath(xpath18_4)
input_search.send_keys("****") 






# 유효기간 월(Month) 2자리 입력
# ★★★★★ 안되서 full xpath 사용 ★★★★★
# ★★ xpath 안되면 full xpath 이래도 안되면 selector 사용 ★★


xpath19 = "/html/body/div[1]/div[4]/div[2]/form[1]/div[4]/div[8]/div[1]/div[1]/div[4]/div[1]/span/input"
driver.find_element_by_xpath(xpath19).click() # click() 함수는 클릭함.

input_search = driver.find_element_by_xpath(xpath19) # 입력하기 위한 저장변수
input_search.send_keys("**")  # 입력 값

# 유효기간 년(year) 2자리 입력
xpath20 = "/html/body/div[1]/div[4]/div[2]/form[1]/div[4]/div[8]/div[1]/div[1]/div[4]/div[2]/span/input"
driver.find_element_by_xpath(xpath19).click() # click() 함수는 클릭함.

input_search = driver.find_element_by_xpath(xpath20) # 입력하기 위한 저장변수
input_search.send_keys("**")  # 입력 값



# 카드 비밀번호 앞 2자리 입력
xpath21 = "/html/body/div[1]/div[4]/div[2]/form[1]/div[4]/div[8]/div[1]/div[1]/div[5]/span/input"
driver.find_element_by_xpath(xpath21).click() # click() 함수는 클릭함.

input_search = driver.find_element_by_xpath(xpath21) # 입력하기 위한 저장변수
input_search.send_keys("**")  # 입력 값



# 생년월일 8자리 입력
xpath22 = "/html/body/div[1]/div[4]/div[2]/form[1]/div[4]/div[8]/div[1]/div[1]/div[6]/span/input"
driver.find_element_by_xpath(xpath22).click() # click() 함수는 클릭함.

input_search = driver.find_element_by_xpath(xpath22) # 입력하기 위한 저장변수
input_search.send_keys("********")  # 입력 값

# 결제하기 버튼 클릭
xpath23 = "//button[@id='stplCfmBtn']"
PayBtn = driver.find_element_by_xpath(xpath23)
PayBtn.click()


#  "결제하시겠습니까?" alert(경고)창의 '확인'을 클릭합니다.
alert = driver.switch_to.alert
alert.accept() #경고창 확인 클릭