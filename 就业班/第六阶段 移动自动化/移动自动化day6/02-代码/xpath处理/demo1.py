
from appium import webdriver
from selenium.webdriver.common.by import By


def sys_find_element(by, value):
    print(by)
    print(value)

    # 如果by是xpath 那么value必须是//*[@inde='0']

def find_element(loc):
    loc_by = loc[0]
    loc_value = loc[1]

    if loc_by == By.XPATH:
        loc_value = make_xpath_with_feature(loc_value)


    sys_find_element(loc_by, loc_value)

def make_xpath_with_feature(a):
    # xxxxx
    # xxxx
    return "//[a  sxxx ]"


def main():
    search_button = By.ID, "@idandroid/tile"
    # back_button = By.XPATH, "//*[xxxxxxx]"
    back_button = By.XPATH, "text,0"

    find_element(search_button)




if __name__ == '__main__':
    main()


