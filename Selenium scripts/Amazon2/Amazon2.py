import os

import pip
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

clear = lambda: os.system('cls')

clear()
from selenium import webdriver

clear()
from time import sleep

clear()
import random

clear()

clear()
from colorama import Fore

clear()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time
clear()

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])



def run(email):

    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--window-size=100x100")
    # options.add_argument("--headless")
    options.add_argument("--log-level=3")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--silent")

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    #driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
    driver.set_window_size(500, 500)

    url=websit
    clear()

    print(url)

    driver.get(url)

    #---- Login ---- ---- Login ---- ---- Login ---- ---- Login ---- ---- Login ---- ---- Login ----
    emailID = 'ap_email'
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.ID,value=emailID)).send_keys(email)
    passwordID = 'ap_password'
    time.sleep(3)
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.ID,value=passwordID)).send_keys(email+'\n')

    print(Fore.RED + '''
                    ███████╗ ██████╗ ██╗   ██╗
                    ██╔════╝██╔════╝ ╚██╗ ██╔╝
                    █████╗  ██║  ███╗ ╚████╔╝ 
                    ██╔══╝  ██║   ██║  ╚██╔╝  
                    ███████╗╚██████╔╝   ██║   
                    ╚══════╝ ╚═════╝    ╚═╝   
            ''' + Fore.GREEN)
    print("")

    problemID = 'cu-select-secondNode'
    WebDriverWait(driver, 4).until(
        lambda driver: driver.find_element(by=By.XPATH,value="//select[@id='cu-select-secondNode']")).send_keys(problem)
    telephoBtn = '.cu-contact-channel-btn-prim-enabled'


    t = WebDriverWait(driver, 4).until(lambda driver: driver.find_elements(by=By.CSS_SELECTOR,value=telephoBtn))[0]
    driver.execute_script("arguments[0].click();", t)

    countryClass = '.c2c-country'
    xx = WebDriverWait(driver, 6).until(lambda driver: driver.find_elements(by=By.CSS_SELECTOR,value=countryClass))[0]
    xx.send_keys(cntry)

    extID = '.c2c-extension'
    WebDriverWait(driver, 3).until(lambda driver: driver.find_elements(by=By.CSS_SELECTOR,value=extID))[0].send_keys('1,1,1,1,1,1,1,1,1,1')
    clear()
    counter=0
    while counter < 14:
        phoneToUse = random.randint(0, len(phonesList) - 1)
        phoneID='.c2c-yournumber-singlefield'
        WebDriverWait(driver, 20).until(lambda driver: driver.find_elements(by=By.CSS_SELECTOR,value=phoneID))[0].send_keys(phonesList[phoneToUse])
        callBtn='.btn-prim-med'
        t = WebDriverWait(driver, 4).until(lambda driver: driver.find_elements(by=By.CSS_SELECTOR,value=callBtn))[0]
        driver.execute_script("arguments[0].click();", t)
        sleep(5)
        print('************Phone called*************')
        print('phone: ' + phonesList[phoneToUse] + '-- email: ' + email)
        phoneID = '.c2c-yournumber-singlefield'
        WebDriverWait(driver, 20).until(lambda driver: driver.find_elements(by=By.CSS_SELECTOR,value=phoneID))[0].clear()
    driver.quit()
    driver.close()

if __name__ == "__main__":

    install('webdriver-manager')

    emails = []
    password = ''
    i = 1
    file = open('EmailAndPassword.txt')
    content = file.readlines()
    password = content[0]
    websit=''
    for i in range(1,len(content)):
        emails.append(content[i].strip())

    print(emails)
    print(password)
    with open('website.txt', "r") as website:
        websit = website.readline().strip()

    with open('phoneNumbers.txt', "r") as phoneNo:
        phones = phoneNo.readlines()


    phonesList = []
    for phone in phones:
        phonesList.append(phone.strip())

    cntry = ''
    with open('country.txt', "r") as Country:
        cntry = Country.readline().strip()
    print(cntry)
    problem = ''
    with open('problemType.txt', "r") as pr:
        problem = pr.readline().strip()
    print(problem)
    # creating thread
    t = []
    for email in emails:
        run(email)
        #t.append(threading.Thread(target=run, args=(email,)))
    #for th in t:
    #    th.start()
    #for th in t:
    #    th.join()

    print("Done!")