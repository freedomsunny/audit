import psutil
import redis
from config import *


def find_procs_by_name(name):
    """Return a list of processes matching 'pid'."""
    result = []
    for p in psutil.process_iter(attrs=["name", "exe", "cmdline"]):
        for cmd in p.info["cmdline"]:
            if name in cmd:
                result.append(p.pid)
    return result


def get_redis_conn():
    redis_conn_obj = redis.StrictRedis(host=redis_server,
                                       port=redis_port,
                                       db=redis_db,
                                       password=redis_password)
    if redis_conn_obj:
        return redis_conn_obj
    return None
