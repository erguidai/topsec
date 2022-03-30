# 跳转到各个主页面

import time
from selenium.webdriver.common.by import By
from ui.base.basepage import BasePage


# 对首页(概览)页面内容进行检查
class HomePage(BasePage):
    # 1.1概览页面UI信息检查
    # （1）“集群状态”展示框
    def search_text1(self):
        time.sleep(2)
        return self.find(By.XPATH,
                         '//*[@id="panel-c-scroll"]/div[1]/section/section/div/div[1]/section[1]/div/div[1]/div/div[1]/h4').text

    # （2）“集群负载”展示框

    # 1.2.1首页功能1验证：创建云容器入口
    def add_cloud_container(self):
        return self.steps(r"/TopHC/page_object/home_module/home_add_cloud_container1.yaml")

    # 1.2.2首页功能2验证：创建云服务器入口
    def add_cloud_service(self):
        pass

    # 1.2.3首页功能3验证：创建云硬盘入口
    def add_cloud_disk(self):
        pass

    # 1.2.4首页功能4验证：创建网络拓扑入口
    def add_network_topo(self):
        pass


# 云服务器模块入口
# 从首页进入计算模块的首页-->云服务器模块
class CserviceMoudelFile(BasePage):
    # url1 = 'http://10.30.100.26:8080/#/pages/overview'

    def goto_cserver(self):
        # self.visit(url=self.url1)   #该函数是为了元素找不到导致页面卡住的情况下刷新页面，已使用刷新页面函数代替
        self.move_mouse(By.ID, 'navBar_item_计算_content')
        self.move_and_click(By.ID, 'navBar_item_计算_content_云服务器')

    def goto_cserverpage(self):  # 云服务器子模块首页入口
        self.click(By.XPATH, '//*[@id="tab-vmlist"]')

    def goto_mouldpage(self):
        self.click(By.ID, 'tab-template')  # 云服务器子模块模版页面入口

    def goto_specspage(self):
        self.click(By.ID, 'tab-specife')  # 云服务器子模块规格页面入口

    def goto_backup(self):
        self.click(By.ID, 'tab-backup')  # 云服务器子模块备份页面入口

    def goto_strategy(self):
        self.click(By.ID, 'tab-strategy')  # 云服务器子模块策略页面入口


# 云容器模块入口
# 从首页进入计算模块的首页-->云容器模块
class CcontainerMoudelFile(BasePage):
    def goto_ccontainer(self):
        self.move_mouse(By.ID, 'navBar_item_计算_content')
        self.move_and_click(By.ID, 'navBar_item_计算_content_云容器')

    def goto_containerpage(self):  # 云容器子模块首页入口：云容器页面
        self.click(By.XPATH, '//*[@id="tab-container"]')

    def goto_cipherpage(self):  # 云容器子模块密钥页面入口
        self.click(By.XPATH, '//*[@id="tab-secret"]')

    def goto_disposepage(self):  # 云容器子模块配置页面入口
        self.click(By.XPATH, '//*[@id="tab-image"]')


# 从首页进入计算模块的首页-->云服务器页面
class ConfigureHome(BasePage):
    def goto_configure(self):
        self.move_mouse(By.ID, 'navBar_item_系统_content')
        self.move_and_click(By.ID, 'navBar_item_系统_content_配置')

    def goto_configurehome(self):  # 云服务器子模块首页人口
        self.click(By.XPATH, '//*[@id="panel-c-scroll"]/div[1]/section/section/div[1]/div[1]/h3')



# 从首页进入存储模块页面
# 进入云硬盘页面
class CDiskMainPage(BasePage):
    # 进入云硬盘页面
    def goto_CDisk(self):
        self.move_and_click(By.ID, 'navBar_item_存储_content')
        self.move_and_click(By.ID, 'navBar_item_存储_content_云硬盘')

    def goto_CDiskhome(self):
        self.click(By.ID, 'tab-volumelist')

    # 进入存储池页面
    def goto_StoragePoolHome(self):
        self.click(By.ID, 'tab-pool')

    # 进入规格页面
    def goto_SpecsHome(self):
        self.click(By.ID, 'tab-specife')

    # 进入卷备份页面
    def goto_Volume_BackupHome(self):
        self.click(By.ID, 'tab-backup')

    # 进入策略页面
    def goto_StrategyHome(self):
        self.click(By.ID, 'tab-strategy')


# 从首页进入存储模块页面
# 进入文件存储页面
class FileStorageMainPage(BasePage):
    # 进入文件存储页面
    def goto_FileStorage(self):
        self.move_and_click(By.ID, 'navBar_item_存储_content')
        time.sleep(0.5)
        self.move_and_click(By.ID, 'navBar_item_存储_content_文件存储')
        time.sleep(0.5)

    def goto_FileStoragehome(self):
        self.click(By.ID, 'tab-volumelist')

    # # 进入对象存储页面


class ObjectStorageMainPage(BasePage):
    def goto_ObjectStorage(self):
        self.move_and_click(By.ID, 'navBar_item_存储_content')
        time.sleep(0.5)
        self.move_and_click(By.ID, 'navBar_item_存储_content_对象存储')
        time.sleep(0.5)

    def goto_ObjectStoragehome(self):
        self.click(By.ID, 'tab-volumelist')

    # # 进入共享存储页面


class ShareStorageMainPage(BasePage):
    def goto_ShareStorage(self):
        self.move_and_click(By.ID, 'navBar_item_存储_content')
        time.sleep(0.5)
        self.move_and_click(By.ID, 'navBar_item_存储_content_共享存储')
        time.sleep(0.5)

    def goto_ShareStoragehome(self):
        self.click(By.ID, 'tab-storageVolume')


# 运维    截面跳转
# 1、主备容灾
# 2、CDP
# 3、资源池
class ResourcePool(BasePage):
    def goto_pool(self):
        self.move_and_click(By.ID, 'navBar_item_运维_content')
        time.sleep(0.5)
        self.move_and_click(By.ID, 'navBar_item_运维_content_资源池')
        time.sleep(0.5)

    def add_pool(self):
        self.click(By.XPATH,
                   '//*[@id="panel-c-scroll"]/div[1]/section/section/div/section[1]/div[1]/div[1]/ul/li[1]/div/span')
