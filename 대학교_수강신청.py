from selenium import webdriver # 셀레니움과 웹드라이버 부르는 모듈함수 
import time
# import telepot  


driver = webdriver.Chrome('D:\/chromedriver.exe') # 제어하기 위해 변수 선언
url = "https://uportal.catholic.ac.kr/sso/jsp/sso/ip/login_form.jsp" # 이동할 링크주소를 변수에 저장
driver.get(url) # 해당 링크로 이동


# # 텔레그램 메세지 알림
# token = '**************' # 봇 제어 API
# my_user_id = '*********' # 사용자 
# bot = telepot.Bot(token) # 봇의 정체성안 token 을 집어넣어줌



# ID

xpath = "//input[@id='userId']" # 입력(검색)버튼, // input[@id='srch']에다가 "" 로감싸야함
input_search = driver.find_element_by_xpath(xpath)
input_search.send_keys("***********") # id 입력


# passwd

xpath2 = "//input[@id='password']" # 입력(검색)버튼, // input[@id='srch']에다가 "" 로감싸야함
input_search = driver.find_element_by_xpath(xpath2)
input_search.send_keys("***********") # pwd 입력


# 로그인 클릭
xpath3 = "//button[@class='n-form']" # x 버튼, //button[@class='closeBtn']에다가 "" 로감싸야함
login = driver.find_element_by_xpath(xpath3) # driver 즉,chrome으로 요소를 찾아서 x창을 끈다.
login.click() # 변수명.click() 클릭하는 소스


# 바로 수강신청_학생(성심) 이동
time.sleep(1)
url2 = "https://uportal.catholic.ac.kr/stw/scsr/scoo/scooLessonApplicationStudentReg.do"
driver.get(url2)


# 해당 개설전공 전체로 수정
xpath4 = "/html/body/div[1]/div[1]/main/section[2]/div[1]/ul/li[2]/label/select"
time.sleep(1)
all_select = driver.find_element_by_xpath(xpath4)
all_select.click() # click() 함수는 클릭함.
driver.execute_script("window.scrollTo(0,10000)") # ★ 아래로 스크룰바 쫙 내림 y가 세로내리는길이 +10000은 밑 / -10000 맨 위


# full xpath 사용 (개설전공 - 전체(full xpath))
xpath5 = "/html/body/div[1]/div[1]/main/section[2]/div[1]/ul/li[2]/label/select/option[1]"
driver.find_element_by_xpath(xpath5).click() # click() 함수는 클릭함.




# 교과목명 검색 입력
xpath6 = "/html/body/div[1]/div[1]/main/section[2]/div[1]/ul/li[5]/label/input"
subject = driver.find_element_by_xpath(xpath6)
subject.click() 
subject.send_keys("과목명 입력") 


# 조회버튼 클릭
xpath7 = "/html/body/div[1]/div[1]/main/section[2]/div[1]/ul/li[6]/button"
driver.find_element_by_xpath(xpath7).click() # click() 함수는 클릭함.

        

### 숫자값을 text로  긁어오는 과정

# 제대로 출력됨 41 제한인원
##xpath9 = driver.find_element_by_xpath("//div[@class='ucups-reg-app-table-flow']/table[@class='ucups-reg-app-table']/tbody[@id='jsrSchedGrid']/tr[2]/td[9]") # 수강신청인원 41
##print(xpath9.text)


## 제대로 출력됨 41 수강신청인원
##xpath10 = driver.find_element_by_xpath("//div[@class='ucups-reg-app-table-flow']/table[@class='ucups-reg-app-table']/tbody[@id='jsrSchedGrid']/tr[2]/td[8]") # 제한인원 41
##print(xpath10.text)

#time.sleep(초) 이란?
# 시간 지연을 넉넉히 줘야 값을 받아오기전에 제대로 수행
# 기다리는 시간이 길어질수록: 정확한 동작을 보장하지만 실행속도가 느려짐
# 기다리는 시간이 짧아질수록: 실행속도가 빨라지지만, 네트워크 상태가 안좋으면 망할 수 있음



# ★★★★수강신청 매크로 과목마다 수정법★★★★★
# ★★★★ 해당하는 분반에 수강신청 버튼 full xpath 수정 해야함★★★★
# ★★★★ 조회시 tr은 첫번 째, tr[2]는 두번째 뜨는것을 의미함 , 이것도 수정해줘야함★★★★



count = 1
while True :
    # 조회버튼 클릭
    xpath7 = "/html/body/div[1]/div[1]/main/section[2]/div[1]/ul/li[6]/button"
    driver.find_element_by_xpath(xpath7).click() # click() 함수는 클릭함.

    time.sleep(1)


    # 제한인원 수 비교
    
    xpath9 = driver.find_element_by_xpath("//div[@class='ucups-reg-app-table-flow']/table[@class='ucups-reg-app-table']/tbody[@id='jsrSchedGrid']/tr[1]/td[9]") # 수강신청인원 41

    # 수강신청인원 비교
    xpath10 = driver.find_element_by_xpath("//div[@class='ucups-reg-app-table-flow']/table[@class='ucups-reg-app-table']/tbody[@id='jsrSchedGrid']/tr[1]/td[8]") # 제한인원 41



    add_subject = "/html/body/div[1]/div[1]/main/section[2]/div[2]/div/table/tbody/tr[1]/td[13]/button" # 수강신청  
    check = "/html/body/div[2]/section/div/div/div[3]/div/div/ul/li/button" # 수강신청 후 확인

    print("★현재 시도횟수★ :",count)
    print("현재 제한 인원:",xpath9.text)
    print("현재 수강신청인원:",xpath10.text)
    print("=" * 25)    
    count+= 1
    
    if xpath9.text != xpath10.text :
        #수강신청 후 종료
        driver.find_element_by_xpath(add_subject).click()

        # 수강신청 후 확인 버튼 클릭
        time.sleep(1)
        driver.find_element_by_xpath(check).click()

        # # 텔레그램 성공메세지   
        # bot.sendMessage(my_user_id, "수강신청 성공했습니다!") 
        break