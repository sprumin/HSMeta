from bs4 import BeautifulSoup

import requests
import json


def get_parser(url):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    return soup


def get_rank():
    html = get_parser("https://www.hearthstudy.com/")
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


def run():
    bot_data = {
        "tiers": get_rank(),
    }

    print(bot_data)

if __name__ == "__main__":
    run()
