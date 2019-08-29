from selenium.webdriver.common.by import By

login_user_loc=(By.XPATH,'//*[@name="phone"]')
login_passwd_loc=(By.XPATH,'//*[@name="password"]')
login_button_loc=(By.XPATH,'//button[text()="登录"]')

login_form_error_info_loc=(By.XPATH,'//*[@class="form-error-info"]')
login_middle_error_msg_loc=(By.XPATH,'//*[@class="layui-layer-content"]')