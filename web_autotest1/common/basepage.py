
from common import logger
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC
from common.constants import screenshoots_dir
import datetime
import time

logger=logger.my_logger(__name__)
class BasePage:

    #此层可以封装pageobjects层所有用到selenium中的底层方法
    #还可以包含一些元素的通用操作，如alert，windows，iframe等
    #还可以封装一些额外的web断言
    #实现日志记录，实现失败截图
    #封装的关键字函数可以相互套用

    def __init__(self,driver):
        # self.driver=webdriver.Chrome()
        self.driver=driver



    def save_web_screenshot(self,loc_msg='1234566'):
        """
        封装的自己截图方法，方便日志输出，以及其他共呢个调用
        :function:页面截图
        :param loc_msg:功能页面page的描述
        :return:
        """

        now=time.strftime("%Y-%m-%d %H_%M_%S")
        filepath="{0}_{1}.png".format(loc_msg,now)
        print(filepath)

        try:
            self.driver.save_screenshot(screenshoots_dir + '/' + filepath)
            logger.info("{} 失败截图成功,图片存放在 {} 目录下".format(loc_msg,screenshoots_dir))
        except:
            logger.exception("截取网页截图失败")
            raise


    def visible_element(self,loc,loc_msg="",timeout=30,frequency=0.5):
        """
        封装自己的等待元素可见方法，方便日志输出以及等待失败页面截图
        :function:等待元素可见
        :param loc: 元素定位表达式
        :param timeout: 设置超时时间
        :param frequency: 设置刷新频率
        :param loc_msg: 功能页面page的描述
        :return:
        """
        logger.info("等待元素 {} 可见".format(loc_msg))
        try:
            # start=datetime.datetime.now()
            WebDriverWait(self.driver,timeout,frequency).until(EC.visibility_of_element_located(loc))
            # end=datetime.datetime.now()

            # logger.info("等待元素开始时间为{},结束时间为{},等待元素{}可见共耗时{}".format(start,end,loc,start-end))

        except:
            logger.exception(" {} 等待元素可见失败".format(loc_msg))
            self.save_web_screenshot(loc_msg)
            raise



    def get_element(self,loc,loc_msg=""):
        """
        :function:获取元素定位的对象
        :param loc: 元素定位表达式
        :param loc_msg: 功能页面page的描述
        :return: ele，返回一个定位到的元素对象
        """
        logger.info("获取 {} 的元素定位{}".format(loc_msg,loc))
        try:
            ele=self.driver.find_element(*loc)
            logger.info(" {} 元素定位成功".format(loc_msg))
            return ele
        except:
            logger.exception(" {} 元素定位失败".format(loc_msg))
            self.save_web_screenshot(loc_msg)
            raise


    def input_text(self,loc,loc_msg="",*args):


        """
        :function:输入框输入文本
        :param loc: 元素定位表达式
        :param loc_msg: 功能页面page的描述
        :param args: 动态参数
        :return:
        """
        #1.等待元素可见
        self.visible_element(loc,loc_msg)
        #2.获取元素定位
        ele=self.get_element(loc,loc_msg)
        #3.发送文本
        try:
            ele.send_keys(args)
            logger.info(" {} 输入文本成功".format(loc_msg))

        except:
            logger.exception(" {} 输入文本失败".format(loc_msg))
            self.save_web_screenshot(loc_msg)
            raise


    def button_click(self,loc,loc_msg=""):
        """
        :funcation:点击元素操作
        :param loc: 元素定位表达式
        :param loc_msg: 功能页面page的描述
        :return:
        """
        self.visible_element(loc,loc_msg)
        ele=self.get_element(loc,loc_msg)

        try:
            ele.click()
            logger.info(" {} 元素点击成功".format(loc_msg))
        except:
            logger.exception(" {} 元素点击操作失败".format(loc_msg))
            self.save_web_screenshot(loc_msg)
            raise

    def get_element_text(self,loc,loc_msg=""):
        """

        :funcation:获取元素文本
        :param loc: 元素定位表达式
        :param loc_msg: 功能页面page的描述
        :return:
        """
        #等待元素可见
        self.visible_element(loc,loc_msg)
        #获取定位元素
        ele=self.get_element(loc,loc_msg)
        #获取所定位元素的文本内容
        try:
            text=ele.text
            logger.info(" {} 元素成功获取文本".format(loc_msg))
            return text
        except:
            logger.exception(" {} 元素获取文本失败}".format(loc_msg))
            self.save_web_screenshot(loc_msg)
            raise



    def get_attribute_value(self,attribute_name,loc,loc_msg=""):
        """

        :funcation:获取元素的属性值
        :param loc: 元素定位表达式
        :param loc_msg: 功能页面page的描述
        :return:
        """
        self.visible_element(loc,loc_msg)
        ele=self.get_element(loc,loc_msg)
        try:
            attribute_value=ele.get_attribute(attribute_name)
            logger.info(" {} 属性值获取成功".format(attribute_name))
            return attribute_name
        except:
            logger.exception(" {} 获取元素属性值失败".format(attribute_name))
            self.save_web_screenshot(loc_msg)
            raise

    def switch_to_windows(self):
        pass

    def switch_to_iframe(self,loc,loc_msg=""):
        """
        :funcation:html切换到内嵌的iframe中
        :param loc: 元素定位表达式
        :param loc_msg: 功能页面page的描述
        :return:
        """
        try:
            WebDriverWait(self.driver,30,0.5).until(EC.frame_to_be_available_and_switch_to_it(loc))
            logger.info(" {} 成功切换到此iframe中".format(loc_msg))
        except:
            logger.exception(" {} 切入alert弹框失败".format(loc_msg))
            self.save_web_screenshot(loc_msg)


    def switch_to_alert(self,loc,loc_msg):
        """

        :funcation:切换并关闭alert弹框
        :param loc: 元素定位表达式
        :param loc_msg: 功能页面page的描述
        """
        #1.点击某个按钮，使弹框出现
        self.button_click(loc,loc_msg)
        try:
            #2.等待alert弹框可见
            WebDriverWait(self.driver,30,0.1).until(EC.alert_is_present())
            #3.切换到alert弹框中
            alert=self.driver.switch_to.alert()
            logger.info("alert弹框的文本内容是 {} ".format(alert.text))
            #4.处理alert弹框，是弹框消失
            alert.accept()
            logger.info(" {} 中的alert弹框成功处理结束")

        except:
            logger.exception(" {} 中的alert弹框处理失败")
            self.save_web_screenshot(loc_msg)
            raise







