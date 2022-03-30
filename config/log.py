import logging
import time

from config.filepath import readFilepath


class Log():
    def __init__(self):
        '''
        1.定义一个日志器，设置级别位DEBUG
        2.定义格式器，格式输出时间，文件名，代码行数，日志级别，日志信息
        3.获取日志输出时间，并做为日志文件名称
        4.获取日志文件夹目录
        '''
        self.logger = logging.getLogger(name='Framework')
        self.logger.setLevel(level=logging.DEBUG)
        log_fmt = '%(asctime)s - %(filename)s - [line:%(lineno)d] - %(levelname)s - %(message)s'
        self.formatter = logging.Formatter(fmt=log_fmt)
        self.LogTime = time.strftime("%Y_%m_%d_")
        self.LogPath = readFilepath.LogPath  # 日志存放路径

    def streamhandler(self):
        '''控制台处理器'''
        handler_stream = logging.StreamHandler()
        handler_stream.setLevel(level=logging.INFO)
        handler_stream.setFormatter(fmt=self.formatter)
        self.logger.addHandler(hdlr=handler_stream)

    def filehandler(self):
        '''文件处理器'''
        handler_file = logging.FileHandler(filename='{0}\{1}.logs'.format(self.LogPath, self.LogTime))
        handler_file.setLevel(level=logging.INFO)
        handler_file.setFormatter(fmt=self.formatter)
        self.logger.addHandler(hdlr=handler_file)

    def getLog(self):
        '''实例化控制台处理器和文件处理器,返回日志器'''
        self.streamhandler()
        self.filehandler()
        return self.logger


# 实例化日志类，并将返回值赋值给变量logger
logs = Log().getLog()

# if __name__ == '__main__':
#     logger.info('test')


#
# import os
# import logging
# from logging.handlers import TimedRotatingFileHandler
# from TopHCS.others.filepath import readFilepath
#
# class Logger:
#     LogPath = readFilepath.LogPath
#
#     def __init__(self):
#         # self._log_config = config.get('log')
#         self._logger = logging.getLogger(self._log_config.get('log_name', 'AUTO'))
#         logging.root.setLevel(logging.NOTSET)
#         f = '%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(message)s'
#         self._f = logging.Formatter(self._log_config.get('format', f))
#
#     def get_logger(self):
#         if not self._logger.handlers:
#             console_handler = logging.StreamHandler()
#             file_handler = TimedRotatingFileHandler(
#                 filename=os.path.join(LOG_PATH, self._log_config.get('file_name')),
#                 when='D',
#                 interval=self._log_config.get('interval', 1),
#                 backupCount=self._log_config.get('backup', 7),
#                 encoding='utf-8',
#                 delay=True
#             )
#             console_handler.setLevel(logging.INFO)
#             file_handler.setLevel(logging.INFO)
#             console_handler.setFormatter(self._f)
#             file_handler.setFormatter(self._f)
#             self._logger.addHandler(console_handler)
#             self._logger.addHandler(file_handler)
#         return self._logger
#
# logs = Logger().get_logger()
