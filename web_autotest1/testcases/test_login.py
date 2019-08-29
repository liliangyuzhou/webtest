
import unittest
from selenium import webdriver
from pageobjects.login_page import  LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class Test_Login(unittest.TestCase):


    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://120.78.128.25:8765/Index/login.html")

    def tearDown(self):
        self.driver.close()


    # 正常登陆
    def test_login_success(self):
        LoginPage(self.driver).login('18684720553','python')
        # 判断登陆页面的一个元素存在
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.XPATH,'//*[contains(text(),"我的帐户")]')))
        #判断页面的url发生跳转
        self.assertEqual(self.driver.current_url,'http://120.78.128.25:8765/Index/index')

    # 登陆手机号和密码都为空
    def test_login_failed_mobile_null(self):
        LoginPage(self.driver).login("","")
        self.assertEqual('请输入手机号',LoginPage(self.driver).get_form_area_error_message())


    # 登陆手机号为空，密码不为空
    def test_login_failed_mobliephone_isnull(self):
        LoginPage(self.driver).login('','python')
        self.assertEqual('请输入手机号',LoginPage(self.driver).get_form_area_error_message())

     #登陆密码为空
    def test_login_failed_passwd_isnull(self):
        LoginPage(self.driver).login('18684720553','')
        self.assertEqual('请输入密码',LoginPage(self.driver).get_form_area_error_message())

    #登陆手机号错误格式输入
    def test_login_failed_mobile_type_error(self):
        LoginPage(self.driver).login('1868472055','python')
        self.assertEqual('请输入正确的手机号',LoginPage(self.driver).get_form_area_error_message())



    # 输入正确的手机号，错误的密码
    def test_login_failed_mobile_passwd_error(self):
        LoginPage(self.driver).login('18684720553','python1')
        self.assertEqual("帐号或密码错误!",LoginPage(self.driver).get_middlepage_area_error_message())

    #输入未注册的手机号和密码进行登陆
    def test_login_failed_with_unrigister_mobile(self):
        LoginPage(self.driver).login("18392628362",'python1')
        self.assertEqual("此账号没有经过授权，请联系管理员!",LoginPage(self.driver).get_middlepage_area_error_message())


