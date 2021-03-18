from time import sleep
from selenium import webdriver


URL = ''

driver = webdriver.Edge('C:\\msedgedriver.exe')

driver.get(url=URL)
#driver.implicitly_wait(17)
print ("hi wesdhy ! 30초 이내로 로그인 하십시오. 30초 후 거래 매크로가 시작되요!")
sleep(30)


while True:
    try:
        content = driver.find_element_by_css_selector('a.buy')
        content.click()
        break
    except:
        
        driver.get(url=URL)
        sleep(1)
        


print ("주문페이지 로드를 완료 했습니다.")
while True:
    try:
        content2 = driver.find_element_by_id('DeliveryRideo_T').click()
        print ("배송 설정을 완료 했습니다.(일반택배.)")
        break
    except:
        print ("error")
        
        



while True:
    try:
        content3 = driver.find_element_by_css_selector('#global_form > div.cartWrap > div.cartContent > div:nth-child(181) > div.cont.deliBx > table > tbody > tr:nth-child(1) > td.t_tit.paymentTab > ul > li:nth-child(2) > label > input').click()
        print ("입금설정 완료 했습니다.(무통장입금)")
        break
    except:
        print ("error")
        
        



while True:
    try:
        content4 = driver.find_element_by_id('BankName').click()
        print ("은행셀렉")
        break
    except:
        print ("error")
        




while True:
    try:
        content5 = driver.find_element_by_css_selector('#BankNameSelector > li:nth-child(5) > a').click()
        print ("은행선택이 완료 되었습니다 (우리은행)")
        break
    except:
        print ("error")
        



while True:
    try:
        content6 = driver.find_element_by_css_selector('#PaymentContents > div > div.boxArea > ul > li:nth-child(4) > div.boxCont > ul > label:nth-child(4) > input').click()
        print ("영수증 방식 설정 완료(현금영수증)")
        break
    except:
        print ("error")
        



while True:
    try:
        content7 = driver.find_element_by_css_selector('#global_form > div.cartWrap > div.cartContent > div:nth-child(181) > div.cont.deliBx > table > tbody > tr:nth-child(1) > td.t_userInfo > div.btmpaybtnBox > a').click()
        print ("결제완료 ")
        break
    except:
        print ("error")