"""
主要因为封装basepage页面，为后续测试用例提供日志输出和失败截图功能
"""
from common.basepage import BasePage
from pagelocators import login_locators as lc
class LoginPage(BasePage):
    # 登陆
    def login(self, user, passwd):
        self.input_text(lc.login_user_loc,"登陆页面_用户名输入框",user)
        self.input_text(lc.login_passwd_loc,"登陆页面_密码输入框",passwd)
        self.button_click(lc.login_button_loc,loc_msg="登陆页面_登陆按钮")


    # 获取表单区域的错误信息
    def get_form_area_error_message(self):
        return self.get_element_text(lc.login_form_error_info_loc,"登陆页面_表单区域的错误信息")


    # 获取页面中间的错误信息
    def get_middlepage_area_error_message(self):
        return self.get_element_text(lc.login_middle_error_msg_loc,"登陆页面_页面中间区域的错误信息")

