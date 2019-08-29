
import unittest
from selenium import webdriver
from pageobjects.login_page1 import  LoginPage
from pagedatas import common_data
from pagedatas.login_data import *

from  ddt import  ddt,data,unpack
@ddt
class Test_Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get("{}/Index/login.html".format(common_data.url))

    def tearDown(self):
        self.driver.refresh()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()



    #登陆表单错误
    @data(*login_failed_from_data)
    def test_login_fail_form_error(self,data):
        LoginPage(self.driver).login(data["user"],data["password"])
        self.assertEqual(data["check"],LoginPage(self.driver).get_form_area_error_message())


    #登陆页面中间错误
    @data(*login_failed_middle_data)
    @unpack
    def test_login_fail_middle_error(self,user,password,check):
        LoginPage(self.driver).login(user,password)
        self.assertEqual(check,LoginPage(self.driver).get_middlepage_area_error_message())


    #登陆成功

    def test_login_success(self):
        LoginPage(self.driver).login(login_success_data['user'],login_success_data['password'])
        self.assertEqual(login_success_data['check'],self.driver.current_url)




