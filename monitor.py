# encoding=utf-8
import time
import re
import traceback
from config import *
from log import createlog
from utils import find_procs_by_name, get_redis_conn

LOG = createlog(__name__, log_level)


redis_conn = get_redis_conn()

pat = re.compile(r".*==========(.+)==========.*")


def follow(thefile):
    file_seek = redis_conn.get(charging_log_file_seek)
    if not file_seek:
        # thefile.seek(0, 2)
        # thefile.seek(offset, where)
        # offset -- where begin start file
        # where  -- 0 begin start; 1 begin current; 2 begin end;
        thefile.seek(0, 0)
    else:
        thefile.seek(int(file_seek), 0)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        redis_conn.set(charging_log_file_seek, thefile.tell())
        yield line


if __name__ == '__main__':
    result = find_procs_by_name("monitor.py")
    if len(result) > 1:
        em = "process is already running with pid: {0}".format(result)
        print em
        exit(1)
    while 1:
        try:
            logfile = open(audit_log, "r")
            loglines = follow(logfile)
            for line in loglines:
                result = pat.match(line)
                if result:
                    json_str = result.group(1)
                    # 数据为空，不存数据
                    result = json_str.split("++")
                    if not result[-1]:
                        continue
                    redis_conn.sadd(charging_data, json_str)
                    LOG.info("get data: {0}".format(json_str))
                    print("get data: {0}".format(json_str))
        except Exception as e:
            LOG.error("send data error  msg: <{0}>".format(e))
            # traceback.print_exc()
            # print(e)
