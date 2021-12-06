import os
import shutil
import threading

import pip
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

clear = lambda: os.system('cls')

clear()
from selenium import webdriver

clear()
from time import sleep, time

clear()
import random
from bs4 import BeautifulSoup as bs

clear()

clear()
from colorama import Fore

clear()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

clear()


def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])


def send_data(driver, selector, data):
    WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR, value=selector)).send_keys(
        data)


def select_data(driver, selector, data):
    while (1):
        try:
            WebDriverWait(Select, 20).until(
                lambda Select: Select(driver.find_element(by=By.CSS_SELECTOR, value=selector))).select_by_value(data)
            break
        except:
            sleep(0.3)
            continue


def sendTelegram(api_key, channel_id, text):
    requests.get(f"https://api.telegram.org/bot{api_key}/sendMessage?chat_id={channel_id}&text={text}")


def run(national_id, first_name, second_name, third_name, nick_name, government, markz, village, address, disability,
        marital_status, job, phone, centers, filename):
    global date, time, center_name, value
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--window-size=100x100")
    options.add_argument("--headless")
    options.add_argument("--log-level=3")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--silent")

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=options)
    driver.set_window_size(1000, 1000)

    url = 'http://pod.mohp.gov.eg/register'
    clear()

    print(url)
    while (1):
        driver.get(url)

        centers_url = f"http://pod.mohp.gov.eg/apps/lookups/centers.php?lk_governments={government}&major_dismed={disability}&dhxr1638710690607=1"
        r = requests.get(centers_url).content
        bs_content = bs(r, "lxml")

        centers = []
        for center in bs_content.findAll("item", ):
            if center['value'] == "": continue
            center_id = center['value']
            center_name = center['label']

            center_dic = {
                'center_id': center_id,
                'center_name': center_name
            }
            centers.append(center_dic)
        if len(centers) == 0:  # no dates available
            sleep(random.uniform(settings['min_refresh_time'], settings['max_refresh_time']))
            continue

        nationalID = "input[name='national_id']"
        send_data(driver, nationalID, national_id)

        firstname = "input[name='name_1']"
        send_data(driver, firstname, first_name)

        secondname = "input[name='name_2']"
        send_data(driver, secondname, second_name)

        thirdname = "input[name='name_3']"
        send_data(driver, thirdname, third_name)

        nickName = "input[name='name_4']"
        send_data(driver, nickName, nick_name)

        gov = "select[name='govt_code']"
        select_data(driver, gov, government)

        markzz = "select[name='mark_code']"
        select_data(driver, markzz, markz)

        vill_ = "select[name='vill_code']"
        select_data(driver, vill_, village)

        address_ = "input[name='benf_address']"
        send_data(driver, address_, address)

        disability_ = "select[name='major_dismed']"
        select_data(driver, disability_, disability)

        Ok_btn = ".dhtmlx_popup_button"
        WebDriverWait(driver, 20).until(
            lambda driver: driver.find_element(by=By.CSS_SELECTOR, value=Ok_btn)).click()

        social_rel = "select[name='social_rel']"
        select_data(driver, social_rel, marital_status)

        job_ = "input[name='benf_job']"
        send_data(driver, job_, job)

        phone_ = "input[name='benf_tel']"
        send_data(driver, phone_, phone)

        center_name = ''
        for center in centers:
            center_sel = "select[name='center_id']"
            select_data(driver, center_sel, center['center_id'])
            center_name = center['center_name']

            center_date = "select[name='fk_centerschd_id']"
            date = ''
            while (1):
                try:
                    dates = WebDriverWait(Select, 20).until(
                        lambda Select: Select(driver.find_element(by=By.CSS_SELECTOR, value=center_date))).options
                    if len(dates) == 0: continue
                    for i in range(1, len(dates)):
                        WebDriverWait(Select, 20).until(
                            lambda Select: Select(
                                driver.find_element(by=By.CSS_SELECTOR, value=center_date))).select_by_index(i)
                        date = dates[i].text
                        break
                    break
                except:
                    sleep(0.3)
                    continue

            visit_time = "select[name='visit_time']"
            # select_data(driver, visit_time, "01")
            time = ''
            while (1):
                try:
                    times = WebDriverWait(Select, 20).until(
                        lambda Select: Select(driver.find_element(by=By.CSS_SELECTOR, value=visit_time))).options
                    if len(times) == 0: continue
                    for i in range(0, len(times)):
                        WebDriverWait(Select, 20).until(
                            lambda Select: Select(
                                driver.find_element(by=By.CSS_SELECTOR, value=visit_time))).select_by_index(i)
                        time = times[i].text

                        break
                    break
                except:
                    sleep(0.3)
                    continue
            break

        i = 0
        while (1):
            try:
                save_btn = ".dhxform_btn_filler"
                WebDriverWait(driver, 20).until(
                    lambda driver: driver.find_element(by=By.CSS_SELECTOR, value=save_btn)).click()
            except:
                sleep(1)
                i += 1
                try:
                    if (i > 1):
                        value = WebDriverWait(driver, 0.3).until(
                            lambda driver: driver.find_element(by=By.CSS_SELECTOR,
                                                               value='.dhtmlx_popup_text span')).text
                        print(value)
                        # sleep(500)
                except:
                    pass

                if i > 2:
                    break
                continue

        if value == "يرجى التأكد من البيانات المدخلة":
            shutil.move(filename, filename.replace('cases', 'wrong_cases'))
            break
        elif value == "الرقم القومي مسجل مسبقا":
            shutil.move(filename, filename.replace('cases', 'reserved'))
            break
        else:
            break
        # reserved

    print(center_name, date, time)
    s = value + "\n" + national_id + "\n" + center_name + "\n" + date + "\n" + time
    sendTelegram(settings['bot_api'], settings['channel_id'], s)

    print(th.name)
    driver.quit()
    driver.close()



def read_cases():
    data = []
    global bs_content
    path = 'cases'
    for filename in os.listdir(path):
        if not filename.endswith('.xml'): continue
        fullname = os.path.join(path, filename)

        # Read the XML files
        with open(fullname, "rb") as file:
            content = file.read()
            bs_content = bs(content, "lxml")
        dic = {"national_id": (bs_content.find("item", {"variable": "national_id"})['value']),
               "first_name": (bs_content.find("item", {"variable": "first_name"})['value']),
               "second_name": (bs_content.find("item", {"variable": "second_name"})['value']),
               "third_name": (bs_content.find("item", {"variable": "third_name"})['value']),
               "nick_name": (bs_content.find("item", {"variable": "nick_name"})['value']),
               "government": (bs_content.find("item", {"variable": "government"})['value']),
               "address": (bs_content.find("item", {"variable": "address"})['value']),
               "markz": (bs_content.find("item", {"variable": "markz"})['value']),
               "village": (bs_content.find("item", {"variable": "village"})['value']),
               "disability": (bs_content.find("item", {"variable": "disability"})['value']),
               "marital_status": (bs_content.find("item", {"variable": "marital_status"})['value']),
               "job": (bs_content.find("item", {"variable": "job"})['value']),
               "phone": (bs_content.find("item", {"variable": "phone"})['value']),
               "filename": fullname,
               }

        data.append(dic)
    return data


def read_settings():
    with open('settings.xml', "rb") as file:
        content = file.read()
        bs_content = bs(content, "lxml")
        dic = {"mode": float(bs_content.find("item", {"variable": "mode"})['value']),
               "min_open_time": float(bs_content.find("item", {"variable": "min_open_time"})['value']),
               "max_open_time": float(bs_content.find("item", {"variable": "max_open_time"})['value']),
               "min_refresh_time": float(bs_content.find("item", {"variable": "min_refresh_time"})['value']),
               "max_refresh_time": float(bs_content.find("item", {"variable": "max_refresh_time"})['value']),
               "bot_api": (bs_content.find("item", {"variable": "bot_api"})['value']),
               "channel_id": (bs_content.find("item", {"variable": "channel_id"})['value']),
               }

    return dic


if __name__ == "__main__":

    # install('webdriver-manager')
    # install('colorama')
    # install('lxml')
    # install('bs4')
    clear()

    data = read_cases()
    settings = read_settings()
    print(settings)

    print()

    t = []
    for case in data:
        print(case['government'])
        centers_url = f"http://pod.mohp.gov.eg/apps/lookups/centers.php?lk_governments={case['government']}&major_dismed={case['disability']}&dhxr1638710690607=1"
        r = requests.get(centers_url).content
        bs_content = bs(r, "lxml")

        centers = []
        for center in bs_content.findAll("item", ):
            if center['value'] == "": continue
            center_id = center['value']
            center_name = center['label']

            center_dic = {
                'center_id': center_id,
                'center_name': center_name
            }
            centers.append(center_dic)
            # print(center_id,center_name)
        # if len(centers)==0: #no dates available
        #    continue
        print(case['national_id'])

        t.append(threading.Thread(target=run, args=(
            case['national_id'], case['first_name'], case['second_name'], case['third_name'], case['nick_name'],
            case['government'], case['markz'], case['village'], case['address'],
            case['disability'], case['marital_status'], case['job'], case['phone'], centers, case['filename'])))

    for th in t:
        sleep(random.uniform(settings['min_open_time'], settings['max_open_time']))
        th.start()
    xx = 5
    for th in t:
        th.name=xx
        xx+=1
        th.join()

    print("Done!")
