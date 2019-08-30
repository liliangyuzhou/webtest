
import pytest

from pageobjects.login_page2 import  LoginPage

from pagedatas.login_data import *
from common.logger import my_logger
logger=my_logger(__name__)

from  ddt import  ddt,data,unpack
@pytest.mark.usefixtures("open_url")
@pytest.mark.usefixtures("refresh_page")
@pytest.mark.smoke
class Test_Login:
    #
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver=webdriver.Chrome()
    #     cls.driver.get("{}/Index/login.html".format(url))
    #
    # def tearDown(self):
    #     self.driver.refresh()
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()



    #登陆表单错误
    @pytest.mark.parametrize("data",login_failed_from_data)
    def test_login_fail_form_error(self,data,open_url):

        LoginPage(open_url).login(data["user"],data["password"])
        assert data["check"]==LoginPage(open_url).get_form_area_error_message()


    #登陆页面中间错误

    @pytest.mark.parametrize("data",login_failed_middle_data)
    def test_login_fail_middle_error(self,data,open_url):

        LoginPage(open_url).login(data["user"],data["password"])
        assert data["check"]==LoginPage(open_url).get_middlepage_area_error_message()


    #登陆成功

    def test_login_success(self,open_url):
        LoginPage(open_url).login(login_success_data['user'],login_success_data['password'])
        assert  login_success_data['check']==open_url.current_url




