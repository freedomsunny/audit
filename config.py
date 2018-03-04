# encoding=utf-8
import socket

redis_server = '127.0.0.1'
redis_port = '6379'
redis_password = ''
redis_db = 0
# 日志文件
log_file = '/var/log/audit.log'
# 日志等级
log_level = 10
# 实时监控的文件
audit_log = "/var/log/nginx/charging_resource.log"
# redis中存入偏移量的键名
charging_log_file_seek = "charging_log_file_seek" + "_" + socket.gethostname()
# redis中存入计费数据的键名
charging_data = "charging_data"
