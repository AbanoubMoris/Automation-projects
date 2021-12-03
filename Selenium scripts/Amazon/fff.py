import os
import sys
import threading
import time
from telnetlib import EC

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

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




def run(email):

    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--window-size=100x100")
    # options.add_argument("--headless")
    options.add_argument("--log-level=3")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--silent")
    driver = webdriver.Chrome('../chromedriver.exe', chrome_options=options)
    driver.set_window_size(500, 500)#حجم الشاشة

    url=websit
    print(url)
    japan=False
    if url.find('japan')>0:
        japan=True
    import re
    lang=''
    if not japan:
        lang = re.search('https://advertising.amazon.(.*)/am', url)
        lang=lang.group(1)

    phone_Button=''
    subject=''
    description=''
    countryButton=''
    phone_number=''
    Ext=''
    callButton=''
    countryClass='.SelectOption-sc-19adxfa-0'
    phone_Button = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[3]/div/div/div/div/button[2]'
    classNameForSubjectAndphonNumberArea='.InputFormGroup__styledInput-sc-17ihzsp-0'
    descriptionClass='.TextAreaFormGroup__styledTextArea-sc-zcfzrb-2'
    callButtonClass='.Button__StyledButton-sc-1jjgdfp-0'

    if lang=='fr':
        subject='/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[4]/div[2]/div/div/div/div[1]/div/div/input'
        description='/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[4]/div[2]/div/div/div/div[2]/div/div/textarea'
        countryButton='/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[4]/div[2]/div/div/div/div[4]/div/label/button'
        phone_number='/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[4]/div[2]/div/div/div/div[5]/div[1]/div[2]/div/div/input'
        Ext='/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[4]/div[2]/div/div/div/div[5]/div[1]/div[3]/div/div/input'
        callButton='/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[4]/div[2]/div/div/div/div[5]/div[2]/button'

    elif japan or lang=='de' or lang=='it' or lang=='nl' or lang=='ae' or lang=='sg' or lang=='mx' or lang=='es' or lang=='co.uk' or lang=='mx' or lang=='sg':
        subject='/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[3]/div[2]/div/div/div/div[1]/div/div/input'
        description='/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[3]/div[2]/div/div/div/div[2]/div/div/textarea'
        countryButton='/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[3]/div[2]/div/div/div/div[4]/div/label/button'
        phone_number='/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[3]/div[2]/div/div/div/div[5]/div[1]/div[2]/div/div/input'
        Ext='/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[3]/div[2]/div/div/div/div[5]/div[1]/div[3]/div/div/input'
        callButton='/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[3]/div[2]/div/div/div/div[5]/div[2]/button'

    print(lang)


    driver.get(url)

    emailID = 'ap_email'
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id(emailID)).send_keys(email)
    passwordID = 'ap_password'
    time.sleep(3)

    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id(passwordID)).send_keys(password+'\n')


    def genRand():
        random_string = ''
        for _ in range(15):
            # Considering only upper and lowercase letters
            random_integer = random.randint(97, 97 + 26 - 1)
            flip_bit = random.randint(0, 1)
            # Convert to lowercase if the flip bit is on
            random_integer = random_integer - 32 if flip_bit == 1 else random_integer
            # Keep appending random characters using chr(x)
            random_string += (chr(random_integer))

        return random_string


    try:
        nameRandom = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/div/input'
        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(nameRandom)).send_keys(genRand())
    except:
        skip = 'ap-account-fixup-phone-skip-link'
        nextclick = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id(skip))
        driver.execute_script("arguments[0].click();", nextclick)
        nameRandom = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/div/input'
        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(nameRandom)).send_keys(genRand())

    AgencyID = 'select-master-account-type-Agency'
    AgencyBtn = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id(AgencyID))
    driver.execute_script("arguments[0].click();", AgencyBtn)

    nextBtn = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div[3]/button[2]'
    nextclick = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(nextBtn))
    driver.execute_script("arguments[0].click();", nextclick)
    time.sleep(3)
    # ---------------------
    get_url = driver.current_url
    EntityID = get_url[get_url.find('entityId'):]
    print(get_url)

    #'https://advertising.amazon.nl/help?ref_=AAC_gnav_support_center&entityId=ENTITY3GJCV9JSFEXI8'
    if not japan:
        driver.get('https://advertising.amazon.'+ lang +'/help?ref_=AAC_gnav_support_center&'+EntityID)
        sleep(2)
        #'https://advertising.amazon.com.br/help?ref_=AAC_gnav_support_center&entityId=ENTITY2MODFL7XJR29H#GWVZ7SU4A82USB3A'
        driver.get('https://advertising.amazon.'+lang+'/help?ref_=AAC_gnav_support_center&'+EntityID+'#GWVZ7SU4A82USB3A')
        print("HERE")
    else:
        #driver.get('https://advertising-japan.amazon.com/help?ref_=AAC_gnav_support_center&' + EntityID)
        #sleep(2)
        driver.get(
            'https://advertising-japan.amazon.com/help?ref_=AAC_gnav_support_center&' + EntityID + '#GWVZ7SU4A82USB3A')
        print("HERE")


    ConstactUSFooter = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/a'
    nav = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(ConstactUSFooter))
    driver.execute_script("arguments[0].click();", nav)

    counter=0
    while (counter < 14):



        counter+=1

        try:
            sleep(1.2)
            # driver.get('https://advertising.amazon.com.br/contactus?entityId=ENTITY3M583YH3D2S98')

            comboSelector(driver,phone_Button)

            #English
            try:
                engilishBtn = '.lang-button'
                ch1 = WebDriverWait(driver, 2).until(lambda driver: driver.find_element_by_css_selector(engilishBtn))
                driver.execute_script("arguments[0].click();", ch1)
            except:
                sleep(10000)
                pass


            # -----------------------------------------------------

            print(subject)
            #WebDriverWait(driver, 1).until(lambda driver: driver.find_element_by_xpath(subject)).send_keys(genRand())
            WebDriverWait(driver, 4).\
                until(lambda driver: driver.find_elements_by_css_selector(classNameForSubjectAndphonNumberArea))[0].send_keys(genRand())

            #WebDriverWait(driver, 4).until(lambda driver: driver.find_element_by_xpath(description)).send_keys(genRand())
            WebDriverWait(driver, 4). \
                until(lambda driver: driver.find_elements_by_css_selector(descriptionClass))[0].send_keys(genRand())

            ch1 = WebDriverWait(driver, 4).until(lambda driver: driver.find_elements_by_css_selector('.country-dropdown'))[0]
            driver.execute_script("arguments[0].click();", ch1)
            sleep(2)

            mp = {'Andorra': 1,
                  'Angola': 2,
                  'Australia': 3,
                  'Austria': 4,
                  'Bahamas': 5,
                  'Bahrain': 6,
                  'Belgium': 7,
                  'Brazil': 8,
                  'Cambodia': 9,
                  'Canada': 10,
                  'Chile': 11,
                  'China': 12,
                  'Colombia': 13,
                  'Costa Rica': 14,
                  'Cyprus': 15,
                  'Czech Republic': 16,
                  'Denmark': 17,
                  'Equatorial Guinea': 18,
                  'Finland': 19,
                  'France': 20,
                  'Germany': 21,
                  'Guam': 22,
                  'Guernsey': 23,
                  'Hong Kong': 24,
                  'Hungary': 25,
                  'Iceland': 26,
                  'India': 27,
                  'Iran': 28,
                  'Iraq': 29,
                  'Ireland': 30,
                  'Isle Of Man': 31,
                  'Israel': 32,
                  'Italy': 33,
                  'Japan': 34,
                  'Jordan': 35,
                  'Luxembourg': 36,
                  'Macao': 37,
                  'Malaysia': 38,
                  'Malta': 39,
                  'Mauritius': 40,
                  'Mexico': 41,
                  'Mongolia': 42,
                  'Nepal': 43,
                  'Netherlands': 44,
                  'New Zealand': 45,
                  'Nicaragua': 46,
                  'Norway': 47,
                  'Palestine': 48,
                  'Panama': 49,
                  'Paraguay': 50,
                  'Peru': 51,
                  'Poland': 52,
                  'Portugal': 53,
                  'Puerto Rico': 54,
                  'Qatar': 55,
                  'Romania': 56,
                  'Russia': 57,
                  'Singapore': 58,
                  'Slovakia': 59,
                  'South Africa': 60,
                  'South Korea': 61,
                  'Spain': 62,
                  'Sri Lanka': 63,
                  'Sweden': 64,
                  'Switzerland': 65,
                  'Taiwan': 66,
                  'Thailand': 67,
                  'Turkey': 68,
                  'U.S. Virgin Islands': 69,
                  'United Kingdom': 70,
                  'United States': 71,
                  'Uruguay': 72,
                  'Vatican': 73,
                  'Venezuela': 74
                  }

            try:

                sleep(1.2)

                xx = WebDriverWait(driver, 4).until(lambda driver: driver.find_element_by_css_selector(countryClass+"[value='"+cnt+"']"))
                print(xx)
                driver.execute_script("arguments[0].click();", xx)
            except:
                print("Erorrrr")
                sleep(10000)
                pass

            phoneToUse = random.randint(0,len(phonesList)-1)

            try:
                WebDriverWait(driver, 3). \
                    until(lambda driver: driver.find_elements_by_css_selector(classNameForSubjectAndphonNumberArea))[
                    5].send_keys('1,1,1,1,1,1,1,1,1,1')
                WebDriverWait(driver, 3). \
                    until(lambda driver: driver.find_elements_by_css_selector(classNameForSubjectAndphonNumberArea))[
                    4].send_keys(phonesList[phoneToUse])
            except:
                WebDriverWait(driver, 3). \
                    until(lambda driver: driver.find_elements_by_css_selector(classNameForSubjectAndphonNumberArea))[
                    4].send_keys('1,1,1,1,1,1,1,1,1,1')
                WebDriverWait(driver, 3). \
                    until(lambda driver: driver.find_elements_by_css_selector(classNameForSubjectAndphonNumberArea))[
                    3].send_keys(phonesList[phoneToUse])



            print('************Phone*************')
            print('phone: ' + phonesList[phoneToUse] + '-- email: ' + email)
            print('************Phone*************')



            i = 0

            while (i < 400):  # الرقم ده عشان تزود مدة الضغط
                try:

                    ch1 = WebDriverWait(driver, 4).until(lambda driver: driver.find_elements_by_css_selector(callButtonClass))[3]
                    driver.execute_script("arguments[0].click();", ch1)
                    i += 1
                except:

                    sleep(10000)
                    break

            sleep(4)

            driver.get(driver.current_url)

        except:
            sleep(10000)
            driver.get(driver.current_url)
            pass



def comboSelector(driver,phone_button):
    comboBox1 = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/label/button'
    ch1 = WebDriverWait(driver, 4).until(lambda driver: driver.find_element_by_xpath(comboBox1))
    driver.execute_script("arguments[0].click();", ch1)
    thrdChoice = '/html/body/div[1]/div[3]/div[2]/div[2]/div/div/button[3]'
    ch1 = WebDriverWait(driver, 4).until(lambda driver: driver.find_element_by_xpath(thrdChoice))
    driver.execute_script("arguments[0].click();", ch1)
    sleep(2)
    comboBox2 = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/label/button'
    ch1 = WebDriverWait(driver, 4).until(lambda driver: driver.find_element_by_xpath(comboBox2))
    driver.execute_script("arguments[0].click();", ch1)
    firstChoice = '/html/body/div[1]/div[3]/div[2]/div[2]/div/div/button'
    ch1 = WebDriverWait(driver, 4).until(lambda driver: driver.find_element_by_xpath(firstChoice))
    driver.execute_script("arguments[0].click();", ch1)
    # ---------------------------------
    sleep(1.2)

    try:
        ch1 = WebDriverWait(driver, 4).until(lambda driver: driver.find_element_by_xpath(phone_button))
        driver.execute_script("arguments[0].click();", ch1)
    except:
        ch1 = WebDriverWait(driver, 4).until(lambda driver: driver.find_element_by_xpath(phone_button))
        driver.execute_script("arguments[0].click();", ch1)



if __name__ == "__main__":
    emails = []
    password = ''
    i = 1
    '''with open('EmailAndPassword.txt', "r") as emailAndPassword:
        # read file content
        password = emailAndPassword.readline(0).strip()
        emails = emailAndPassword.readline(i).strip()
        i+=1'''
    # print file contents
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

    cnt = ''
    with open('country.txt', "r") as Country:
        cnt = Country.readline().strip()

    print(cnt)
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