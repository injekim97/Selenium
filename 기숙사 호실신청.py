from selenium import webdriver # 셀레니움과 웹드라이버 부르는 모듈함수 
import time
import telepot
import pyautogui

### 고클린으로 최적화한후에 약 14~16초 내 모든것 완료 ###

driver = webdriver.Chrome('D:\/chromedriver.exe') # 제어하기 위해 변수 선언
url = "https://uportal.catholic.ac.kr/sso/jsp/sso/ip/login_form.jsp" # 이동할 링크주소를 변수에 저장

### 창의 해상도 크기 최대화 (전체화면) ###
driver.maximize_window()

# 창의해상도 값 지정가능
# driver.set_window_size(1920, 1080)

driver.get(url) # 해당 링크로 이동


# 텔레그램 메세지 알림
token = '1211388523:AAEK4XTUYDY3dvk6z***********' # 봇 제어 API
my_user_id = '("********")' # 사용자 
bot = telepot.Bot(token) # 봇의 정체성안 token 을 집어넣어줌



# ID

xpath = "//input[@id='userId']" # 입력(검색)버튼, // input[@id='srch']에다가 "" 로감싸야함
input_search = driver.find_element_by_xpath(xpath)
input_search.send_keys("********") # id 입력


# passwd

xpath2 = "//input[@id='password']" # 입력(검색)버튼, // input[@id='srch']에다가 "" 로감싸야함
input_search = driver.find_element_by_xpath(xpath2)
input_search.send_keys("********") # pwd 입력


# 로그인 클릭
xpath3 = "//button[@class='n-form']" # x 버튼, //button[@class='closeBtn']에다가 "" 로감싸야함
login = driver.find_element_by_xpath(xpath3) # driver 즉,chrome으로 요소를 찾아서 x창을 끈다.
login.click() # 변수명.click() 클릭하는 소스



# 바로 호실신청페이지로 이동
time.sleep(1)
url2 = "https://uportal.catholic.ac.kr/stw/scew/sswf/sswfRoomSelection.do"
driver.get(url2)



# 현재 마우스 위치의 (x, y)좌표 반환
pyautogui.position() 
x, y = pyautogui.position()
print("x={0},y={1}".format(x,y)) 

time.sleep(1)

### 호실선택 층 부분 선택 ###
pyautogui.click(x=468, y=762)

### 선택시 스크롤을 6층으로 지정하여 클릭###
pyautogui.click(x=448, y=856)

# 선택시 스크롤을 7층으로 지정함
#pyautogui.click(x=446, y=886)

# 선택시 스크롤을 8층으로 지정함
#pyautogui.click(x=447, y=907)




 ###################--------------------------------------------------#############################
### 기숙사 몇인실 선택 ###
pyautogui.click(x=1057, y=759)

### 선택시 스크롤을 3인실 지정하여 클릭###
pyautogui.click(x=1086, y=834)

# 선택시 스크롤을 4인실 지정 
#pyautogui.click(x=1097, y=856)


###################--------------------------------------------------#############################
# ★해상도 전체화면으로 설정하여 사용X  ★ 
#마우스 왼쪽 버튼을 누르고 드래그하기 (해당방배정을 위한 스크롤)
#pyautogui.click(x=575, y=999)
#pyautogui.dragTo(800,999,duration=0.2) 0.2초동안 눌러서 오른쪽으로 스크롤

# 현재 마우스 위치의 (x, y)좌표 반환
pyautogui.position() 
x, y = pyautogui.position()
print("x={0},y={1}".format(x,y)) 

### 호실 스크롤 선택 ###
pyautogui.click(x=1691, y=760)

### 호실 신청 : 629호 선택###
pyautogui.click(x=1170, y=623)



### 호실 신청 버튼 클릭
pyautogui.click(x=1851, y=705)

### 호실 신청 버튼 클릭시 팝업창 클릭
pyautogui.click(x=1084, y=639)

# 텔레그램 성공메세지   
bot.sendMessage(my_user_id, "기숙사 호실신청 성공했습니다!")


