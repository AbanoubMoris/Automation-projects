import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def run(phones):
    options = webdriver.ChromeOptions()
    #options.add_argument("disable-infobars")
    #options.add_argument("--disable-extensions")
    #options.add_argument("--window-size=100x100")
    # options.add_argument("--headless")
    #options.add_argument("--log-level=3")
    #options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #options.add_argument("--silent")


    options.add_experimental_option("--debuggerAddress", "127.0.0.1:1549")
    options.add_argument("--user-data-dir=C:\\Users\\abano\Desktop\\New folder\\Google\\GoogleData")

    driver = webdriver.Chrome("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", options=options)
    driver.get('https://accounts.google.com/signin')

    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('identifierId')).send_keys(emails[0])
    nextclick = WebDriverWait(driver, 20).until(
        lambda driver: driver.find_element_by_class_name('VfPpkd-LgbsSe-OWXEXe-k8QpJ'))
    driver.execute_script("arguments[0].click();", nextclick)
    sleep(1.2)
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_name('password')).send_keys(password)
    nextclick = WebDriverWait(driver, 20).until(
        lambda driver: driver.find_element_by_class_name('VfPpkd-LgbsSe-OWXEXe-k8QpJ'))
    driver.execute_script("arguments[0].click();", nextclick)
    sleep(1.2)
    '''Co'''
    '''WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('lastName')).send_keys(genRand(4))
    createNewAccLabel = WebDriverWait(driver, 20).until(lambda driver: driver.find_elements_by_class_name('VfPpkd-LgbsSe-OWXEXe-dgl2Hf'))[0]
    driver.execute_script("arguments[0].click();", createNewAccLabel)
    sleep(1)
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('username')).send_keys(genRand(9))
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('lastName')).send_keys(genRand(4))
    createNewAccLabel = WebDriverWait(driver, 20).until(lambda driver: driver.find_elements_by_class_name('VfPpkd-LgbsSe-OWXEXe-dgl2Hf'))[0]
    driver.execute_script("arguments[0].click();", createNewAccLabel)
    sleep(1)
    
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('lastName')).send_keys(genRand(4))
    createNewAccLabel = WebDriverWait(driver, 20).until(lambda driver: driver.find_elements_by_class_name('VfPpkd-LgbsSe-OWXEXe-dgl2Hf'))[0]
    driver.execute_script("arguments[0].click();", createNewAccLabel)
    sleep(1)
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('username')).send_keys(genRand(9))
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_name('ConfirmPasswd')).send_keys('12345Moh')
                                                                                               
    
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('phoneNumberId')).send_keys(genRand(9))
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('username')).send_keys(genRand(9))
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_name('ConfirmPasswd')).send_keys('12345Moh')
                                                                                               
    
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('phoneNumberId')).send_keys(genRand(9))
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_name('ConfirmPasswd')).send_keys('12345Moh')
    
    
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('phoneNumberId')).send_keys(genRand(9))'''
    '''Co'''
    # driver.get('https://myaccount.google.com/signinoptions/two-step-verification/enroll-welcome?gar=1')
    driver.get(
        'https://accounts.google.com/signin/v2/challenge/pwd?continue=https%3A%2F%2Fmyaccount.google.com%2Fsigninoptions%2Ftwo-step-verification%2Fenroll%3Fgar%3D1&service=accountsettings&osid=1&rart=ANgoxccu-IUASPU5O6sSCRBzNmTTKsG2SIH4-qMq5x_jZzX74EZkMJAcWPYZlDQNNGZ1SQ_JVS4LhWGdHAcJxfRBgc5s_VwI8A&TL=AM3QAYaEsokhgX0XYKRJZbjSY4fz2WmzM17p2vZU0PgrejuYIDbFJ7Kisq-O4ZlS&flowName=GlifWebSignIn&cid=1&flowEntry=ServiceLogin')
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_name('password')).send_keys(password)
    nextclick = WebDriverWait(driver, 20).until(
        lambda driver: driver.find_element_by_class_name('VfPpkd-LgbsSe-OWXEXe-k8QpJ'))
    driver.execute_script("arguments[0].click();", nextclick)
    sleep(1.2)
    chooseCall = WebDriverWait(driver, 20).until(lambda driver: driver.find_elements_by_class_name('SCWude'))[1]
    driver.execute_script("arguments[0].click();", chooseCall)
    sleep(1.2)
    '''Co'''
    '''WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('lastName')).send_keys(genRand(4))
    createNewAccLabel = WebDriverWait(driver, 20).until(lambda driver: driver.find_elements_by_class_name('VfPpkd-LgbsSe-OWXEXe-dgl2Hf'))[0]
    driver.execute_script("arguments[0].click();", createNewAccLabel)
    sleep(1)
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('username')).send_keys(genRand(9))
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_name('ConfirmPasswd')).send_keys('12345Moh')
    
    
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('phoneNumberId')).send_keys(genRand(9))'''
    '''Co'''
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_class_name('whsOnd')).send_keys(phones[0])
    sleep(2)
    nextclick = WebDriverWait(driver, 20).until(lambda driver: driver.find_elements_by_class_name('CwaK9'))[1]
    driver.execute_script("arguments[0].click();", nextclick)

    sleep(10000)

    '''Co'''
    '''WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('lastName')).send_keys(genRand(4))
    createNewAccLabel = WebDriverWait(driver, 20).until(lambda driver: driver.find_elements_by_class_name('VfPpkd-LgbsSe-OWXEXe-dgl2Hf'))[0]
    driver.execute_script("arguments[0].click();", createNewAccLabel)
    sleep(1)
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('lastName')).send_keys(genRand(4))
    createNewAccLabel = WebDriverWait(driver, 20).until(lambda driver: driver.find_elements_by_class_name('VfPpkd-LgbsSe-OWXEXe-dgl2Hf'))[0]
    driver.execute_script("arguments[0].click();", createNewAccLabel)
    sleep(1)
    
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('lastName')).send_keys(genRand(4))
    createNewAccLabel = WebDriverWait(driver, 20).until(lambda driver: driver.find_elements_by_class_name('VfPpkd-LgbsSe-OWXEXe-dgl2Hf'))[0]
    driver.execute_script("arguments[0].click();", createNewAccLabel)
    sleep(1)
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('username')).send_keys(genRand(9))
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_name('ConfirmPasswd')).send_keys('12345Moh')
                                                                                               
    
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('phoneNumberId')).send_keys(genRand(9))
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('username')).send_keys(genRand(9))
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_name('ConfirmPasswd')).send_keys('12345Moh')
                                                                                               
    
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('phoneNumberId')).send_keys(genRand(9))
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('lastName')).send_keys(genRand(4))
    createNewAccLabel = WebDriverWait(driver, 20).until(lambda driver: driver.find_elements_by_class_name('VfPpkd-LgbsSe-OWXEXe-dgl2Hf'))[0]
    driver.execute_script("arguments[0].click();", createNewAccLabel)
    sleep(1)
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('username')).send_keys(genRand(9))
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_name('ConfirmPasswd')).send_keys('12345Moh')
                                                                                               
    
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('phoneNumberId')).send_keys(genRand(9))
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('username')).send_keys(genRand(9))
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_name('ConfirmPasswd')).send_keys('12345Moh')
                                                                                               
    
    
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('phoneNumberId')).send_keys(genRand(9))'''
    '''Co'''



if __name__ == "__main__":

    with open('Numbers.txt', "r") as phoneNo:
        phones = phoneNo.readlines()

    phonesList = []
    for phone in phones:
        phonesList.append(phone.strip())

    print(phonesList)



    emails = []
    password = ''
    i = 1
    file = open('EmailAndPasswordGoogle.txt')
    content = file.readlines()
    password = content[0]
    websit=''
    for i in range(1,len(content)):
        emails.append(content[i].strip())

    print(emails)
    print(password)
    run(phonesList)

    '''
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


    print("Done!")'''
