#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import pytest

from config.filepath import readFilepath

# 生成allure测试报告
'''
    1.安装allure-pytest   pip install allure-pytest  (测试报告中是有数据的，该库用力啊生成测试数据)
    2.下载allurecommand包（https://github.com/allure-framework/allure2/releases）,放在python安装路径下
    3.配置：环境变量path中添加(D:\tools\Python3.7\Lib\site-packages\allure2.14.0\bin)
    4.重启
'''

if __name__ == '__main__':
    # 执行测试用例获得测试数据
    reportpath = readFilepath.ReportPath
    testpath = readFilepath.ServerTestPath
    pytest.main(['-s', testpath, '--alluredir', 'reportpath/allure-result'])

    # 生成测试报告步骤：
    # 1.找到测试数据： allure-result
    # 2.生成测试报告的目录：report
    os.system('allure generate reportpath/allure-result -o reportpath/report --clean')
    # os.system('allure serve ./report')   #打开测试报告
    # 最后的测试报告路径：D:/WorkTools/PyProjects/TopHC/reports/index.html

'''
# --clean-alluredir清空上一次的xml报告
os.system('allure generate report/report_data -o report/html --clean') 
os.system('allure serve report/report_data')
'''

# 关联Jenkins
# 开启Jenkins服务：
'''
    1.Jenkins配置
        下载Jenkins到本地
        全局配置(本地安装好后将安装路径复制到jenkins中)：1.jdk  2.allurecommand
        插件：allure  chinese(jenkins汉化版) Email(安装之后需要配置邮箱：configure System--已安装-->SMTP server:smtp.qq.com;SMTP Port:465;Default Recipients(格式)：2608606229@qq.com;)
    2.构建环境
        新建item-->输入任务名；选择Freestyle project-->General:1.描述：非必填；2.勾选“使用自定义的工作空间”；3.复制run.py的路径（D:\WorkTools\PyProjects\TopHC\reports\）
        -->源码管理:勾选“无”-->构建触发器：不勾选-->构建环境：不勾选-->构建：1.命令：python run.py (windows命令(也可以使用shell命令）)-->构建后操作：1.path:allure-results(生成测试报告)；
        2.增加构建后的操作步骤：选择配置好的邮箱类型（Editable Email Notification）,Send To(接收人)
    3.手动或定时运行测试用例，执行完后自动发送测试报告邮件到邮箱（以地址的方式得到测试报告）
'''
