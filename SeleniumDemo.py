from selenium import webdriver

def SetUp(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.driver.get("http://seleniumdemo.com/")
    self.driver.implicitly_wait(5)

def tearDown(self):
    self.driver.quit()
