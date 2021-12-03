import os
import sys
import threading
import time
from telnetlib import EC

from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from werkzeug.user_agent import UserAgent

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

clear()


#**********************-----------------***********************---------------*******************--------
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

import undetected_chromedriver.v2 as uc


def run(email):

    options  = webdriver.ChromeOptions()
    import pathlib

    #scriptDirectory = pathlib.Path().absolute()
    #options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")

    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--window-size=100x100")
    # options.add_argument("--headless")
    options.add_argument("--log-level=3")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")

    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--silent")

    driver = webdriver.Chrome(executable_path='../chromedriver.exe', chrome_options=options)



    driver.get("https://addmefast.com/free_points/tiktok_followers")
    sleep(20)

    WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_css_selector('.email')).send_keys(email)
    WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_css_selector('.password')).send_keys(password+'\n')
    #login = WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_name('login_button'))
    #driver.execute_script("arguments[0].click();", login)



    driver.get('https://addmefast.com/free_points/reddit_members')

    # storing the current window handle to get back to dashbord
    main_page = driver.current_window_handle
    sleep(3)

    while(1):


        followPath = '/html/body/div[2]/div[2]/div[3]/div/div/div[2]/form/div/div[3]/div/div/div/div/div/center[2]/a'
        follow = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(followPath))
        driver.execute_script("arguments[0].click();", follow)

        sleep(5)

        # changing the handles to access login page
        for handle in driver.window_handles:
            if handle != main_page:
                tiktok = handle


        # change the control to signin page
        driver.switch_to.window(tiktok)

        #click join redit
        tikLogin = '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/button'
        lgn = WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_xpath(tikLogin))
        driver.execute_script("arguments[0].click();", lgn)
        sleep(5)

        try:
            driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

            WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_id('loginUsername')).send_keys(
                'AbanoubMoris14')
            WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_id('loginPassword')).send_keys(
                '44525616Baba')
            loginclass = '.AnimatedForm__submitButton'
            login = WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_css_selector(loginclass))
            driver.execute_script("arguments[0].click();", login)
            sleep(2)

            print(driver.current_url)
            sleep(2)

            # click join redit
            tikLogin = '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/button'
            lgn = WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_xpath(tikLogin))
            driver.execute_script("arguments[0].click();", lgn)
            sleep(5)
        except:
            pass

        driver.close()

        # change control to main page
        driver.switch_to.window(main_page)
        print(driver.current_url)
        sleep(10)




if __name__ == "__main__":


    emails = []
    password = ''
    i = 1

    # print file contents
    file = open('AddMeFastAccounts.txt')
    content = file.readlines()
    password = content[0]
    websit=''
    for i in range(1,len(content)):
        emails.append(content[i].strip())

    print(emails)
    print(password)


    # creating thread
    t = []
    for email in emails:
        #run(email)
        t.append(threading.Thread(target=run, args=(email,)))
    for th in t:
        th.start()
    for th in t:
        th.join()


    print("Done!")