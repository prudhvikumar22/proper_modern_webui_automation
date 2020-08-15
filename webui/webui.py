try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.action_chains import ActionChains
    import os
    import time
except Exception as e:
    print("Module might be missing, See the message----> ", e)

TIME_TO_WAIT = 90


def create_driver(value):
    if value == 'CHROME':
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(options=options)
        driver.delete_all_cookies()
        #driver.maximize_window()
        return driver

    elif value == 'FIREFOX':
        driver = webdriver.Firefox()
        driver.delete_all_cookies()
        driver.maximize_window()
        return driver

    else:
        return "Create with values as either CHROME or FIREFOX to initiate the driver"


class WebUI:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def open(self, link):
        self.driver.get(link)

    def enter(self, locator, data):
        #print(*locator, data)
        WebDriverWait(self.driver, TIME_TO_WAIT).until(EC.visibility_of_element_located((locator)))
        self.driver.find_element(*locator).send_keys(data)

    def click(self, locator):
        #print(locator)
        WebDriverWait(self.driver, TIME_TO_WAIT).until(EC.visibility_of_element_located((locator)))
        self.driver.find_element(*locator).click()

    def go_to(self, locator):
        WebDriverWait(self.driver, TIME_TO_WAIT).until(EC.presence_of_element_located((locator)))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def right_click(self, locator):
        element = self.driver.find_element(*locator)
        action_right_click = ActionChains(self.driver)
        action_right_click.context_click(element).perform()

    def hover(self, locator):
        element = self.driver.find_element(*locator)
        action_hover = ActionChains(self.driver)
        action_hover.move_to_element(element).perform()

    def performance(self, option, locator):
        if option == 'visible':
            WebDriverWait(self.driver, TIME_TO_WAIT).until(EC.visibility_of_all_elements_located((locator)))
        if option == 'invisible':
            WebDriverWait(self.driver, TIME_TO_WAIT).until(EC.invisibility_of_element_located((locator)))

