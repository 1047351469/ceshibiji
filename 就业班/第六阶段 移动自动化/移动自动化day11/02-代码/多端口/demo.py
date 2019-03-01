import threading

from selenium.webdriver.common.by import By

from base_driver import init_driver
from base_action import BaseAction
from login_page import LoginPage


def do(port):
    driver = init_driver(port)
    login_page = LoginPage(driver)
    if "4723" == port:
        login_page.click((By.XPATH, "text,更多"))
    else:
        login_page.click((By.XPATH, "text,WLA"))


def main():
    ports = ["4723", "4725"]

    for i in ports:
        threading.Thread(target=do, args=(i,)).start()

    # for i in ports:
    #     driver = init_driver(i)
    #     login_page = LoginPage(driver)
    #     login_page.click((By.XPATH, "text,更多"))


if __name__ == '__main__':
    main()








# def do(port):
#     driver = init_driver(port)
#     action = BaseAction(driver)
#
#     action.click((By.XPATH, "text,更多"))



# def main():
#     ports = ["4723", "4725"]
#     th_list = list()
#     for i in ports:
#         th = threading.Thread(target=do, args=(i,))
#         th.start()
#         th_list.append(th)