from bs4 import BeautifulSoup
from selenium import webdriver

import datetime
import json
import requests


def _bs4(url):
    """ BeautifulSoup 만을 이용한 크롤링 """
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    return soup


def _selenium(url, _class=None, subject=None):
    """ Selenium과 BeautifulSoup를 이용한 크롤링 """
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('disable-gpu')

    driver = webdriver.Chrome("C:/Users/sprumin/chromedriver.exe", chrome_options=options)
    driver.get(url)

    if _class:
        target = driver.find_elements_by_class_name(_class)

        if subject == "Frequency":
            target[0].click()
        elif subject == "odds":
            target[1].click()
        else:
            return "Subject is None"

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


def get_frequency():
    """ 주요 덱 분포도 """
    find_attr_html = _selenium("https://www.hearthstudy.com/live")
    distibution_dict = dict()

    target_class = find_attr_html.find("div", attrs={"id": "fchart"}).find_all("rect", attrs={"class": "c3-event-rect"})
    target_class_num = target_class[len(target_class) - 1]['class'][2]

    html = _selenium("https://www.hearthstudy.com/live", str(target_class_num), "Frequency")
    name = html.find("div", attrs={"class": "c3-tooltip-container"}).find_all("td", attrs={"class": "name"})
    frequency = html.find("div", attrs={"class": "c3-tooltip-container"}).find_all("td", attrs={"class": "value"})

    if len(name) != len(frequency):
        distibution_dict.update({"Error": "Invalid Data"})
    else:
        for i in range(len(name)):
            distibution_dict.update({name[i].text: frequency[i].text})

    return distibution_dict


def get_win_rates():
    html = _bs4("https://hearthstudy.com/stats")
    rates_dict = dict()

    decks = [
        value.text for value in html.find_all("span", attrs={"class": "kometa"})
    ]
    rates = [
        value.text for value in html.find_all("div", attrs={"class": "transform-right"})
    ]

    if len(decks) != len(rates):
        rates_dict.update({"Error": "Invalid Data"})
    else:
        for i in range(len(decks)):
            rates_dict.update({decks[i]: rates[i]})

    return rates_dict


def run():
    """ 각 데이터들을 json형태로 저장 """
    _datetimenow = datetime.datetime.now()
    _datetime = _datetimenow.strftime("%Y-%m-%d")
    _day = _datetimenow.strftime("%d")

    crawl_data = {
        "date": _datetime,
        "tiers": get_rank(),
        "frequency": get_frequency(),
        "win_rates": get_win_rates(),
    }

    with open('Hearthstone/{}.json'.format(_datetime), 'w', encoding="utf-8") as make_file:
                    json.dump(crawl_data, make_file, ensure_ascii=False, indent="\t")
"""
    while True:
        _tmonth = datetime.datetime.now().strftime("%d")
        if not _tmonth == _day:
            try:
                with open('Hearthstone/{}.json'.format(_datetime), 'w', encoding="utf-8") as make_file:
                    json.dump(crawl_data, make_file, ensure_ascii=False, indent="\t")
            except Exception as e:
                with open('Hearthstone/{}.txt'.format(_datetime), 'w') as make_file:
                    make_file.write(e)
"""

if __name__ == "__main__":
    run()
