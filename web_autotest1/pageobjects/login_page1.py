
"""
主要抽出所有的元素定位表达sh
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pagelocators import login_locators as lc
class LoginPage:
    def __init__(self,driver):
       # self.driver=webdriver.Chrome()
        self.driver=driver


    # 登陆
    def login(self,user,passwd):

        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(lc.login_user_loc))
        self.driver.find_element(*lc.login_user_loc).send_keys(user)
        self.driver.find_element(*lc.login_passwd_loc).send_keys(passwd)
        self.driver.find_element(*lc.login_button_loc).click()

    # 获取表单区域的错误信息
    def get_form_area_error_message(self):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(lc.login_form_error_info_loc))
        return self.driver.find_element(*lc.login_form_error_info_loc).text

    # 获取页面中间的错误信息
    def get_middlepage_area_error_message(self):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(lc.login_middle_error_msg_loc))
        return self.driver.find_element(*lc.login_middle_error_msg_loc).text


