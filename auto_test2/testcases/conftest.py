

from selenium import webdriver
from pagedatas import common_data as cd
import pytest

driver = None

# fixture的定义。如果有返回值，那么写在yield后面。
# 在测试用例当中，调用有返回值的fixture函数时，函数名称就是代表返回值。
# 在测试用例当中，函数名称作为用例的参数即可。
@pytest.fixture(scope="class")  #
def open_url():
    global driver
    # 前置
    driver = webdriver.Chrome()
    driver.get(cd.url+"/Index/login.html")
    yield driver  # yield之前代码是前置，之后的代码就是后置。
    # 后置
    driver.quit()


# 刷新页面 - 定义的第二个fixture
@pytest.fixture
def refresh_page():
    yield
    global driver
    driver.refresh()


# session级别的
@pytest.fixture(scope="session")
def session_action():
    print("===== 会话开始，测试用例开始执行=====")
    yield
    print("===== 会话结束，测试用例全部执行完成！=====")




