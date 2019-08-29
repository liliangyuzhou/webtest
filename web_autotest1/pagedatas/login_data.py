
from pagedatas import common_data
login_success_data= {"user":"18684720553","password":"python","check":"{}/Index/login.html".format(common_data.url)}

login_failed_from_data=[
    {"user":"18684720553","password":"","check":"请输入密码"},
    {"user":"18684720","password":"python","check":"请输入正确的手机号"},
    {"user":"","password":"python","check":"请输入手机号"},
    {"user":"18684720553112","password":"python","check":"请输入正确的手机号"},
    {"user":"","password":"","check":"请输入手机号"}
]

login_failed_middle_data=[
    {"user":"18392628352","password":"123456","check":"此账号没有经过授权，请联系管理员!"},
    {"user":"18684720553","password":"python1","check":"帐号或密码错误!"},

]
