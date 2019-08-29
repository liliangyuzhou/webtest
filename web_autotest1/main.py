from common import HTMLTestRunnerNew
import unittest
from common import constants
from common.logger import my_logger

logger=my_logger(__name__)

discover=unittest.defaultTestLoader.discover(constants.tescase_dir,'test_*.py')
with open(constants.report_dir+'/report.html','wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,
                                            title="test-reporter",description="autotest",
                                            tester="liliang")
    runner.run(discover)

