from bs4 import BeautifulSoup
from selenium import webdriver

import requests
import json
import time


def _bs4(url):
    """ BeautifulSoup 만을 이용한 크롤링 """
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    return soup


def _selenium(url, _class=None):
    """ Selenium과 BeautifulSoup를 이용한 크롤링 """
    driver = webdriver.Chrome("C:/Users/sprumin/chromedriver.exe")
    driver.get(url)

    if _class:
        print("class", _class)
        target = driver.find_element_by_class_name(_class)
        target.click()

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    return soup


def get_rank():
    """ 덱 티어 및 티어 별 랭킹을 보여줌 """
    html = _bs4("https://www.hearthstudy.com/")
    tiers = dict()

    for tier in range(1, 5):
        sub_tiers = dict()
        data = [
            value.text for value in html.find("div", {"id": "siderank{}".format(tier)})
            .find_all("span", attrs={"class", "kometa"})
        ]
        for rank in range(len(data)):
            sub_tiers.update({rank + 1: data[rank]})

        tiers.update({"{} Tiers".format(tier): sub_tiers})

    return tiers


def get_distribution():
    """ 주요 덱 분포도 """
    find_attr_html = _selenium("https://www.hearthstudy.com/live")
    distibution_dict = dict()

    target_class = find_attr_html.find("div", attrs={"id": "fchart"}).find_all("rect", attrs={"class": "c3-event-rect"})
    target_class_num = target_class[len(target_class) - 1]['class'][2]

    html = _selenium("https://www.hearthstudy.com/live", str(target_class_num))
    name = html.find("div", attrs={"class": "c3-tooltip-container"}).find_all("td", attrs={"class": "name"})
    distribution = html.find("div", attrs={"class": "c3-tooltip-container"}).find_all("td", attrs={"class": "value"})

    if len(name) != len(distribution):
        distibution_dict.update({"Error": "Invalid Data"})
    else:
        for i in range(len(name)):
            distibution_dict.update({name[i].text: distribution[i].text})

    return distibution_dict


def get_odds():
    """ 주요 덱 승률 """
    html = _selenium("https://www.hearthstudy.com/live")
    return html


def run():
    """ 각 데이터들을 json형태로 저장 """
    bot_data = {
        "tiers": get_rank(),
        "share": get_distribution(),
    }

    print(bot_data)

if __name__ == "__main__":
    run()
