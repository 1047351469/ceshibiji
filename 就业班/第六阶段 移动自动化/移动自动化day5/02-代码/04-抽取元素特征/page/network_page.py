from selenium.webdriver.common.by import By


class NetworkPage:

    # 更多按钮
    more_button = By.XPATH, "//*[contains(@text,'更多')]"
    # 移动网络
    network_button= By.XPATH, "//*[contains(@text,'移动网络')]"
    # 首选网络类型
    first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    # 2g按钮
    network_2g_button = By.XPATH, "//*[contains(@text,'2G')]"
    # 3g按钮
    network_3g_button = By.XPATH, "//*[contains(@text,'3G')]"

    def __init__(self, driver):
        self.driver = driver

    def click_more(self):
        self.find_element(self.more_button).click()

    def click_network(self):
        self.find_element(self.network_button).click()

    def click_first_network(self):
        self.find_element(self.first_network_button).click()

    def click_2g(self):
        self.find_element(self.network_2g_button).click()

    def click_3g(self):
        self.find_element(self.network_3g_button).click()

    def find_element(self, loc):
        return self.driver.find_element(loc[0], loc[1])