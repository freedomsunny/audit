# encoding=utf-8
import sys
sys.path.append("/root/audit")
from utils import get_redis_conn
from config import *

################################################
#
# 用于手动添加订单数据，数据从nginx+lua中的日志获取
# 日志文件：'/var/log/nginx/charging_resource.log'
#
################################################

redis_con = get_redis_conn()

data = 'POST++instance++5b26203117ff41cbae690248106b96cd++{"server": {"security_groups": [{"name": "default"}], "OS-DCF:diskConfig": "MANUAL", "id": "d6bd688f-f77c-4a06-adb8-5ea8728723cf", "links": [{"href": "http://nova/v2.1/daa89f2bdee1431abd2794fd38598da9/servers/d6bd688f-f77c-4a06-adb8-5ea8728723cf", "rel": "self"}, {"href": "http://nova/daa89f2bdee1431abd2794fd38598da9/servers/d6bd688f-f77c-4a06-adb8-5ea8728723cf", "rel": "bookmark"}], "adminPass": "Haaaaaaaaaaad1"}}'


def add_data2redis(data):
    redis_con.sadd(charging_data, data)


if __name__ == '__main__':
    add_data2redis(data=data)

