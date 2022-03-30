# todo 这里两个文件需要整合，文件路径不需要专门放一个路径

import os

class Filepath:
    '''
    定义一个Filepath类,用来获取文件路径
    1.自动传入data.yaml文件的路劲并读取数据
    2.获取yaml文件中各组数据并返回
    '''
    # 获取当前项目的绝对路径
    BasePath = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/../..')
    # 获取数据yaml文件所在绝对路径
    DataPath = BasePath + '\TopHC\data'
    # 获取测试用例文件所在路径
    TestPath = BasePath + r'\TopHC\test_case'
    # 日志文件所在路径
    LogPath = BasePath + '\TopHC\log'
    # HTML报告所在路径
    ReportPath = BasePath + r'\TopHC\report'
    # 报错截图路径
    ImagePath = BasePath + r'\TopHC\images'

    # 各模块测试数据路径
    # 浏览器驱动路径
    DriverPath = BasePath + '\TopHC\others\driver'

    # 0.登录模块
    # 0.1 登录页面
    # （1）测试步骤数据
    LoginDataPath = DataPath + '\page_data\login_module\login.yaml'
    # # （2）测试用例数据
    # LoginTestDataPath = DataPath + r'\test_data\hmoe_module_data\home_module\logintest.yaml'
    # # （3）测试用例
    # LoginTestPath = TestPath + r'\calculate_module\test_loginpage.py'

    # 1.首页模块

    # 2.计算模块
    # 2.1 云服务器模块
    # 2.1.1云服务器页面
    # （1）测试步骤数据
    ServerDataPath = DataPath + '\page_data\calculate_module_data\cserver_module\serverdata.yaml'
    # （2）测试用例数据
    ServerTestDataPath = DataPath + r'\test_data\calculate_module_data\cserver_module\servertest.yaml'
    # （3）测试用例
    ServerTestPath = TestPath + r'\calculate_module\test_cservermodule.py'
    # 2.1.2 模板页面
    # （1）测试步骤数据
    MouldDataPath = DataPath + '\page_data\calculate_module_data\cserver_module\moulddata.yaml'
    # （2）测试用例数据
    MouldTestPath = DataPath + r'\test_data\calculate_module_data\cserver_module\mouldtest.yaml'
    # （3）测试用例



# 实例化Filepath类并赋值给readFilepath,后面可直接调用readFilepath
readFilepath = Filepath()
