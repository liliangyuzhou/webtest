
import os

base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)
log_dir=os.path.join(base_dir,'Outputs','logs')
# print(log_dir)
report_dir=os.path.join(base_dir,'Outputs','report')
# print(report_dir)
screenshoots_dir=os.path.join(base_dir,'Outputs','screenshoots')
# print(screenshoots_dir)

tescase_dir=os.path.join(base_dir,"testcases")