import os
import random
import re
from time import sleep

import requests
from requests_html import HTMLSession

from bs4 import BeautifulSoup as bs


def send_data():
    global secure_token
    try:
        session = HTMLSession()
        response = session.get(url)
        rx = response.html.find("#content_div")[0].text
        secure_token = \
        re.search(r'secure_token\",\&\#13; label: \"\",&#13; validate: \"NotEmpty\",\&#13; required: true,'
                  r'\&#13; style: \"text-align:left\",\&#13; inputWidth: 250\,\&#13; value: \"([\w]+)"', rx).groups()[0]
        data["1638744617506_secure_token"] = secure_token
        r = session.post("http://pod.mohp.gov.eg/apps/register/register_dp.php?editing=true", data).text
        return r

    except requests.exceptions.RequestException as e:
        print(e)

def read_cases():
    cases = []
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

        cases.append(dic)
    return cases
if __name__ == "__main__":
    url = "http://pod.mohp.gov.eg/register"


    for case in read_cases():
        centers_url = f"http://pod.mohp.gov.eg/apps/lookups/centers.php?lk_governments={case['government']}&major_dismed={case['disability']}&dhxr1638710690607=1"
        r = requests.get(centers_url).content
        bs_content = bs(r, "lxml")

        centers = []
        for center in bs_content.findAll("item", ):
            if center['value'] == "": continue
            center_id = center['value']
            center_name = center['label']

            shedule_url = f"http://pod.mohp.gov.eg/apps/lookups/centers_visit.php?fk_center_id={center_id}&major_dismed={case['disability']}&dhxr1638750893905=1"
            r2 = requests.get(shedule_url).content
            bs_content2 = bs(r2, "lxml")

            for date in bs_content2.findAll("item", ):
                if date['value'] == "": continue
                date_id = date['value']
                date_name = date['label']

                time_url = f"http://pod.mohp.gov.eg/apps/lookups/time_centers.php?center_id={date_id}&dhxr1638751507402=1"
                r3 = requests.get(time_url).content
                bs_content3 = bs(r3, "lxml")

                for time in bs_content3.findAll("item", ):
                    if time['value'] == "": continue
                    time_id = time['value']
                    time_name = time['label']

                    print(center_id,date_id,time_id)

                    data = {
                        "1638744617506_national_id": case['national_id'],
                        "1638744617506_name_1": case['first_name'],
                        "1638744617506_name_2": case['second_name'],
                        "1638744617506_name_3": case['third_name'],
                        "1638744617506_name_4":case['nick_name'],
                        "1638744617506_benf_age": "24",
                        "1638744617506_benf_gender": "1",
                        "1638744617506_govt_code": case['government'],
                        "1638744617506_mark_code": case['markz'],
                        "1638744617506_vill_code": case['village'],
                        "1638744617506_benf_address": case['address'],
                        "1638744617506_major_dismed": case['disability'],
                        "1638744617506_social_rel": case['marital_status'],
                        "1638744617506_benf_job": case['job'],
                        "1638744617506_benf_tel": case['phone'],
                        "1638744617506_center_id": center_id,
                        "1638744617506_fk_centerschd_id": date_id,
                        "1638744617506_visit_time": time_id,
                        #"1638744617506_secure_token": secure_token,
                        "1638744617506_!nativeeditor_status": "inserted",
                        "ids": "1638744617506"
                    }
                    if 'الرقم القومي مسجل مسبقا' in send_data():
                        print(1)
