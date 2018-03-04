# -*- coding: utf-8 -*-
import logging
from cloghandler import ConcurrentRotatingFileHandler
from config import *


def createlog(name, level):
    log = logging.getLogger(name)

    logfile = log_file
    # mode: 默认为"a"
    # maxBytes：文件长度，超过最大长度自动分片，最初日志都会写入filename里面，到达设置的最大长度之后进行分片，分片后文件名为filename.1 filename.2，以此类推
    # backupCount：最大日志文件保留数量，默认为0即不会删除日志文件
    # encoding：日志文件编码格式
    rotate_handler = ConcurrentRotatingFileHandler(
        filename=logfile, mode="a", maxBytes=800*1024*1024, backupCount=5, encoding="utf-8"
    )

    datefmt_str = '%Y-%m-%d %H:%M:%S'
    format_str = '%(asctime)s\t%(levelname)s\t%(message)s '
    formatter = logging.Formatter(format_str, datefmt_str)
    rotate_handler.setFormatter(formatter)

    log.addHandler(rotate_handler)
    # 设置什么级别的log输出，   CRITICAL 50; ERROR 40; WARNING 30; INFO 20; DEBUG 10, NOSET 0;
    log.setLevel(level)

    return log

if __name__ == '__main__':
    log = createlog(__file__, 10)
    log.info('hahaha')
    log.debug('debughahaha')
