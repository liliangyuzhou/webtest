"""
初始版本，不方便维护
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self,driver):
       # self.driver=webdriver.Chrome()
        self.driver=driver


    # 登陆
    def login(self,user,passwd):
        user_loc=(By.XPATH,"//*[@name='phone']")
        print(user_loc)
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(user_loc))
        self.driver.find_element_by_xpath('//*[@name="phone"]').send_keys(user)
        self.driver.find_element_by_xpath('//*[@name="password"]').send_keys(passwd)
        self.driver.find_element_by_xpath('//button[text()="登录"]').click()

    # 获取表单区域的错误信息
    def get_form_area_error_message(self):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.XPATH,'//*[@class="form-error-info"]')))
        return self.driver.find_element_by_xpath('//*[@class="form-error-info"]').text

    # 获取页面中间的错误信息
    def get_middlepage_area_error_message(self):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.XPATH,'//*[@class="layui-layer-content"]')))
        return self.driver.find_element_by_xpath('//*[@class="layui-layer-content"]').text


    #刷新功能
    def refresh_page(self):
        self.driver.refresh()