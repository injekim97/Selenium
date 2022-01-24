# 마스크 알리미 매크로
# 명령어 지연시간은 import time 으로 부름 
# 사이트마다 지연시간이 있기 때문에 그에 해당하는 것에 지연시간을 주면 됨


from selenium import webdriver # 셀레니움과 웹드라이버 부르는 모듈함수 
import time

driver = webdriver.Chrome('F:/파이썬 셀레니옴 저장 장소/chromedriver.exe') # 제어하기 위해 변수 선언


#time.sleep(2) # 2초 지연시간

url = 'https://mask-nearby.com/' #link 주소를 집어넣기위해 url 사용
driver.get(url) #get으로 주소링크에 들어감
time.sleep(2)



# HTML <button class = "closeBtn"> # 차례대로 태그 , 속성 , 속성값임  </button>
# 태그 가리키기 //태그[@속성='속성값'] ex) //button[@class='closeBtn']
# button [@class="closeBtn"]
xpath = "//button[@class='closeBtn']" # x 버튼, //button[@class='closeBtn']에다가 "" 로감싸야함
closeBtn = driver.find_element_by_xpath(xpath) # driver 즉,chrome으로 요소를 찾아서 x창을 끈다.
closeBtn.click() # 변수명.click() 클릭하는 소스
#time.sleep(2)



# input속성을 통해 id로 하면 잡기 쉬움 => id 속성이 있다면 그것을 기준으로 하는게 좋음
# id로 기준치 잡아야함
xpath2 = "//input[@id='srch']" # 입력(검색)버튼, // input[@id='srch']에다가 "" 로감싸야함
input_search = driver.find_element_by_xpath(xpath2)
input_search.send_keys("역곡역") # 변수명.send_keys("입력할 장소")
#time.sleep(2)

# 돋보기 즉 검색하는건 img(이미지) 태그를 감싸고 있는 버튼으로 해야함.
# 상위에 button data 로 되어있으며 , id 값으로 기준하는게 매우좋음
xpath3 = "//button[@id='search-btn']" # x 버튼, //button[@class='closeBtn']에다가 "" 로감싸야함
search_bin = driver.find_element_by_xpath(xpath3) # driver 즉,chrome으로 요소를 찾아서 x창을 끈다.
search_bin.click() # 변수명.click() 클릭하는 소스
