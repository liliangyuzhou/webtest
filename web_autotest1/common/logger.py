import logging
import time
from common import constants

def my_logger(name):
    # #设置日志文件的名称
    # now=time.strftime('%Y-%M-%d')
    # name=now + ".txt"

    #1.新建日志收集器
    logger=logging.getLogger(name)
    #设置日志的输出级别
    logger.setLevel('DEBUG')


    #2.指定日志的输出格式
    fmt=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-日志信息:%(message)s- [%(filename)s:%(lineno)d ]')


    #3.新建日志输出器
    #a.指定日志输出到控制台
    ch=logging.StreamHandler()
    ch.setLevel('DEBUG')
    ch.setFormatter(fmt)
    #b.日志输出到指定文件=
    curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())
    sh=logging.FileHandler(constants.log_dir+'/webtest_{}.log'.format(curTime),encoding='utf-8',mode='w')
    sh.setLevel('DEBUG')
    sh.setFormatter(fmt)

    #4.日志收集器和日志输出器配合使用：handler：渠道
    logger.addHandler(ch)
    logger.addHandler(sh)
    return logger

# logger = my_logger('case')
# logger.info('测试开始啦')
# logger.error('测试报错')
# logger.debug('测试数据')
# logger.info('测试结束')
