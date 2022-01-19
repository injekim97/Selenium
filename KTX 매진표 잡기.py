# 지퍼로 합칠려면 컨트롤 + n


from selenium import webdriver # 셀레니움과 웹드라이버 부르는 모듈함수 
driver = webdriver.Chrome('F:/파이썬 셀레니옴 저장 장소/chromedriver.exe') # 제어하기 위해 변수 선언

url = "http://www.letskorail.com/#" # 이동할 링크주소를 변수에 저장

driver.get(url) # 해당 링크로 이동

# 팝업창 해결할려면 switch_to.window를 이용해야함. driver.switch_to.window(변수명[팝업창[0] 인덱싱번호])


# print(driver.window_handles) 로 몇번째 창이 팝업창이고 뛰울려고 하는 창인지 확인
# 위의 소스 실행시 ['CDwindow-71926F24B2F61C3E1550AB1E92FE5915', 'CDwindow-4FBAE170B833F48309DE796123698661']
# 리스트로 나와있어서 슬라이싱[0],[1],[2] 로 선택해서 해당 원하고자 하는 창을 끄면됨

driver.switch_to.window(driver.window_handles[1]) # 해당 팝업창을 끔

driver.close() # 창을 닫는 소스 driver.close() 해당 팝업창으로 이동후에 창을 끔


# 이동하는 것은 해당 인덱스 번호를 switch_to.window(이동하고자하는 변수명[인덱스])
driver.switch_to.window(driver.window_handles[0]) # 원하는 창으로 이동함



# 변수명(xpath) = "" 안에 이것은  //input[@id='txtGoStart'] 크롬 F12 켜서 //input[@id='id값'] 에 "" 하면 됨
# xpath = 출발역 , # clear()를 통해 서울서울 방지
xpath ="//input[@id='txtGoStart']"
driver.find_element_by_xpath(xpath).clear() # clear() 통해 서울만 입력되게끔 함
driver.find_element_by_xpath(xpath).send_keys("서울")


# xpath = 도착역 , # clear()를 통해 서울서울 방지
xpath2 ="//input[@id='txtGoEnd']"
driver.find_element_by_xpath(xpath2).clear() # clear() 통해 서울만 입력되게끔 함
driver.find_element_by_xpath(xpath2).send_keys("창원\n") #\n 하면 엔터기능임

# driver.find_element_by_xpath 는 가장 제일 근접한 소스를 사용함
# xpath3 ="//img[@alt='달력']"에 있는 //img[@alt='달력'] 를 사용 



# 출발일 달력누르기
xpath3 ="//img[@alt='달력']" #처음으로 img를 사용함
driver.find_element_by_xpath(xpath3).click() # click() 함수는 클릭함.



# 달력은 팝업창으로 뜨기 떄문에 F12를 눌러 클릭

driver.switch_to.window(driver.window_handles[1]) # 팝업창 뜨기 때문에 이걸로  달력창 넘겨야함

xpath4 ="//span[@id='d20200624']" 
driver.find_element_by_xpath(xpath4).click() # click() 함수는 클릭함.




# 시간 클릭 
driver.switch_to.window(driver.window_handles[0]) # 시간은 버튼을 눌러 쭉 스크룰을 내려야하기 떄문에 창 이동해야함

xpath5 ="//select[@id='time']" 
driver.find_element_by_xpath(xpath5).click() # click() 함수는 클릭함.
driver.find_element_by_xpath(xpath5).send_keys("20") # send_keys("20")는 20으로 입력



# 승차권 예매 클릭 
xpath6 ="//img[@alt='승차권예매']" 
driver.find_element_by_xpath(xpath6).click() # click() 함수는 클릭함.



# ex) 태그는 img , 속성은 alt ="예약하기"
# 태그와 속성이 같으면 XPATH 풀버전으로 사용해야함
# xpath 풀버전으로 사용한 것


# 이것을 다 쓰면 태그 속성 겹쳐도 사용할 수 있음
# 둘다 매진이여서 일반실은 매진 유아는 예매로 했음



# 일반실 => 매진 인 상황
# /html/body/div[1]/div[3]/div/div[1]/form[1]/div/div[4]/table[1]/tbody/tr[1]/td[6]/img

# 다음차 일반실 예약 되는 상황

# /html/body/div[1]/div[3]/div/div[1]/form[1]/div/div[4]/table[1]/tbody/tr[2]/td[6]/a[1]/img


# // 두개의 의미는 html에 어떠한 것들도 사용 가능하다.
# tbody 까지 지우면 됨


# ★★★★★ 매진이라는 글자를 얻기 위해서는 get_attribute('alt') 를 사용해야함
# 그러면 일반실 매진 소스에다가 유아 예약하기 소스를 넣으면 됨
# 아래 두 소스는 이해하기 쉽게 주석처리함 해당소스는 밑에소스임



##xpath7 = "//tbody/tr[1]/td[6]//img" # 축약한 일반실 매진 소스
##driver.find_element_by_xpath(xpath7).get_attribute('alt')



xpath7 = "//tbody/tr[2]/td[6]/a[1]/img" # 축약한 일반실 예약
yy = driver.find_element_by_xpath(xpath7).get_attribute('alt') # 여기서 alt는 예약하기임

while True: # 무한루프 반복

    if yy == '예약하기':
        driver.find_element_by_xpath(xpath7).click()
        break

else :
    driver.refresh() # refresh()는 새로고침 즉 계속 반복을 의미













