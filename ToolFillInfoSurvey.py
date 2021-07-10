import time
import datetime
import pytz
import json

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

G_DATA = {}
G_BROWSER = webdriver.Chrome()
# ==================================================================================================
#     MAIN                                                                                        #
# ==================================================================================================


def main():
    global G_DATA
    G_DATA = read_json("config.json")

    navigate_to_page(G_DATA["URL_VIEW_FORM"])
    for action in G_DATA["ACTIONS"]:
        if action["TYPE"] == "TEXT_BOX":
            fill_text_box(action)
        elif action["TYPE"] == "RADIO_BUTTON":
            fill_radio_button(action)

# ==================================================================================================
#     FUNCTION                                                                                    #
# ==================================================================================================


def get_datetime_today():
    tz = pytz.timezone('Asia/Ho_Chi_Minh')
    date_time_now_vn = datetime.datetime.now(tz)
    return date_time_now_vn.strftime("%m/%d/%Y")


def read_json(path_file):
    with open(path_file, encoding='utf-8') as json_file:
        fixed_json = ''.join(
            line for line in json_file if not line.lstrip().startswith('//'))
        data = json.loads(fixed_json)
    return data


def fill_text_box(action):
    xpathElement = G_DATA["LOCATOR"]["TEXT_BOX"] % (action["DESCRIPTION"])
    elem = WebDriverWait(G_BROWSER, 10).until(
        EC.visibility_of(G_BROWSER.find_element_by_xpath(xpathElement)))
    elem.send_keys(action["INPUT_DATA"] if action["INPUT_DATA"]
                   != "today" else get_datetime_today())


def fill_radio_button(action):
    xpathElement = G_DATA["LOCATOR"]["RADIO_BUTTON"] % (
        action["DESCRIPTION"], action["INPUT_DATA"])
    elem = WebDriverWait(G_BROWSER, 10).until(
        EC.visibility_of(G_BROWSER.find_element_by_xpath(xpathElement)))
    elem.click()


def navigate_to_page(page):
    G_BROWSER.get(page)
    time.sleep(5)


if __name__ == "__main__":
    main()
