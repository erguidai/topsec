'''
    每个页面都是独立的对象，main用来实现页面对象的组合，即从一个页面跳转到另一个页面
'''

from ui.base.basepage import BasePage
from ui.page_object.goto_mianpage import HomePage, CserviceMoudelFile


class Main(BasePage):
    # 登录页面（用户名登录的步骤）
    url = 'https://10.30.45.90/#/login'

    # 1.首页-->概览模块
    # 1.1首页页面入口
    def goto_homepage(self):
        return HomePage(self.driver)  # 跳转至首页功能实现的流程方法类

    # 2.计算模块
    # 2.1云服务器子模块入口路径
    def goto_cserver(self):
        CserviceMoudelFile(self.driver).goto_cserver()
        return CserviceMoudelFile(self.driver).goto_cserverpage()  # 先调用入口方法进入云服务器模块/云服务器页面

    # 2.1.1云服务器页面入口
    def goto_serverpage(self):
        return CserviceMoudelFile(self.driver).goto_cserverpage()  #先调云服务器云服务器页面入口

    # 2.1.2云服务器模板页面入口
    def goto_mouldpage(self):
        return CserviceMoudelFile(self.driver).goto_mouldpage()  # 先调云服务器模板页面入口

    # 2.1.3云服务规格页面入口
    def goto_specs(self):
        return CserviceMoudelFile(self.driver).goto_specspage()  # 先调云服务器规格页面入口

    # 2.1.4云服务备份页面入口
    def goto_backup(self):
        return CserviceMoudelFile(self.driver).goto_backup()  # 先调云服务器备份页面入口

    # 2.1.5云服务策略页面入口
    def goto_strategy(self):
        return CserviceMoudelFile(self.driver).goto_strategy()  # 先调云服务器策略页面入口
