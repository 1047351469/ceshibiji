from selenium.webdriver.common.by import By


class DisplayPage:

    # 显示按钮
    display_button = By.XPATH, "//*[contains(@text,'显示')]"
    # 搜索按钮
    search_button = By.ID, "com.android.settings:id/search"
    # 搜索框
    input_text_view = By.ID, "android:id/search_src_text"
    # 返回按钮
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self, driver):
        self.driver = driver
        # 点击显示 (init 里面可以去写已经确定的这个模块所有的前置功能)
        self.click_display()

    def click_display(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.driver.find_element(self.display_button[0], self.display_button[1]).click()
        self.find_element(self.display_button).click()

    def click_search(self):
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        self.find_element(self.search_button).click()

    def input_text(self, text):
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys(text)
        self.find_element(self.input_text_view).send_keys(text)

    def click_text_view(self):
        self.driver.find_element(self.input_text_view).click()

    def click_back(self):
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        self.find_element(self.back_button).click()

    def find_element(self, loc):
        return self.driver.find_element(loc[0], loc[1])