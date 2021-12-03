import os

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
print(Fore.RED + '''
            ███████╗ ██████╗ ██╗   ██╗
            ██╔════╝██╔════╝ ╚██╗ ██╔╝
            █████╗  ██║  ███╗ ╚████╔╝ 
            ██╔══╝  ██║   ██║  ╚██╔╝  
            ███████╗╚██████╔╝   ██║   
            ╚══════╝ ╚═════╝    ╚═╝   
    ''' + Fore.GREEN)
print("")

email = ''
password = ''
with open('EmailAndPassword.txt', "r") as emailAndPassword:
    # read file content
    email = emailAndPassword.readline().strip()
    password = emailAndPassword.readline().strip()
    # print file contents
print(email)
print(password)
with open('phoneNumbers.txt', "r") as phoneNo:
    phones = phoneNo.readlines()

phonesList = []
for phone in phones:
    phonesList.append(phone.strip())

cnt = ''
with open('country.txt', "r") as Country:
    cnt = Country.readline().strip()

print(cnt)

options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--window-size=100x100")
# options.add_argument("--headless")
options.add_argument("--log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--silent")
driver = webdriver.Chrome('../chromedriver.exe', chrome_options=options)
driver.set_window_size(50, 50)
driver.get(
    'https://www.amazon.com.br/ap/signin?openid.pape.max_auth_age=43200&openid.return_to=https%3A%2F%2Fadvertising.amazon.com.br%2Fam%2FmanagerAccounts%2Fcreate%3Ffbclid%3DIwAR2GZMuVDi7gRaZWpGhKEn2GlUgAhV4KEiePnP9Nws-M5AWRCfFOCkDdpdM&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_bt_desktop_br&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&fbclid=IwAR0AO9tgHdz5SZeNoscB2_iYkdo_DMAOMp7d2JHhqKh7SW7ujZO7eOLjLpA')



emailID = 'ap_email'
WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id(emailID)).send_keys(email)
passwordID = 'ap_password'
WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id(passwordID)).send_keys(password)
signinBtnID = 'signInSubmit'
nextclick = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id(signinBtnID))
driver.execute_script("arguments[0].click();", nextclick)

sleep(5)


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

# ---------------------

nav1 = '/html/body/div[1]/div[2]/div/div/nav/a[4]'
nav = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(nav1))
driver.execute_script("arguments[0].click();", nav)

help = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/a'
nav = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(help))
driver.execute_script("arguments[0].click();", nav)

nav1 = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/a'
nav = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(nav1))
driver.execute_script("arguments[0].click();", nav)

while (len(phonesList) > 0):

    try:

        print('************Phone*************')
        print(phonesList[0])
        print('************Phone*************')

        # driver.get('https://advertising.amazon.com.br/contactus?entityId=ENTITY3M583YH3D2S98')

        comboBox1 = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/label/button'
        ch1 = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(comboBox1))
        driver.execute_script("arguments[0].click();", ch1)
        thrdChoice = '/html/body/div[1]/div[3]/div[2]/div[2]/div/div/button[3]'
        ch1 = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(thrdChoice))
        driver.execute_script("arguments[0].click();", ch1)
        sleep(2)
        comboBox2 = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/label/button'
        ch1 = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(comboBox2))
        driver.execute_script("arguments[0].click();", ch1)
        firstChoice = '/html/body/div[1]/div[3]/div[2]/div[2]/div/div/button'
        ch1 = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(firstChoice))
        driver.execute_script("arguments[0].click();", ch1)

        telphoneBtn = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[3]/div/div/div/button[2]'
        ch1 = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(telphoneBtn))
        driver.execute_script("arguments[0].click();", ch1)

        engilishBtn = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[3]/div/div/div/button[3]'
        ch1 = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(engilishBtn))
        driver.execute_script("arguments[0].click();", ch1)

        # -----------------------------------------------------
        subject = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[3]/div[2]/div/div/div/div[1]/div/div/input'
        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(subject)).send_keys(genRand())
        description = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[3]/div[2]/div/div/div/div[2]/div/div/textarea'
        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(description)).send_keys(genRand())

        country = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[3]/div[2]/div/div/div/div[4]/div/label/button'
        ch1 = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(country))
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

        country1 = '/html/body/div[1]/div[3]/div[2]/div[2]/div/div/button[' + str(mp[cnt]) + ']'
        print(country1)
        ch1 = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(country1))
        driver.execute_script("arguments[0].click();", ch1)

        phone = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[3]/div[2]/div/div/div/div[5]/div[1]/div[2]/div/div/input'
        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(phone)).send_keys(phonesList.pop(0))
        print(len(phonesList))

        Ext = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[3]/div[2]/div/div/div/div[5]/div[1]/div[3]/div/div/input'
        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(Ext)).send_keys('1,1,1,1,1,1,1,1,1,1')

        endcall = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div/button'
        i = 0

        while (i < 400):  # الرقم ده عشان تزود مدة الضغط
            try:
                requestPhoneCall = '/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div[3]/div[2]/div/div/div/div[5]/div[2]/button'
                ch1 = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(requestPhoneCall))
                driver.execute_script("arguments[0].click();", ch1)
                i += 1
            except:
                break

        sleep(2)

        driver.get(driver.current_url)

    except:
        sleep(5000)
        pass

sleep(3)
driver.quit()




