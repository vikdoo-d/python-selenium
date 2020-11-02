# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 Double Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
from selenium import webdriver
from selenium.webdriver import ChromeOptions




def set_ua_custom():
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("detach", True)
    option.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) |FXT-Agent-2.0__LAPTOP-9N2F1SOA__0.0.0.0_192.168.124.2_0.0.0.0_0.0.0.0__84-FD-D1-27-C6-A2_84-FD-D1-27-C6-9E_84-FD-D1-27-C6-9F_86-FD-D1-27-C6-9E__E823_8FA6_BF53_0001_001B_448B_44D2_E8C0.=PM056019AD000696=BFEBFBFF000806EC7FFAFBBF=LAPTOP-9N2F1SOA__0.0.0.0__Intel(R)Core(TM)i7-8565UCPU@1.80GHz=7.8G Safari/537.36')
    driver= webdriver.Chrome(options=option)
    # driver.implicitly_wait(30)  # 等待3秒
    driver.get("https://vip.qiaofangyun.com/login.jsp?companyUuid=wuhugejiafangchan_company53f9d1c92")
    # driver.quit()

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    set_ua_custom()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
