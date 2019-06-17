import logging
import time
from base.base_logs import Logger
import os
import re

# 获取脚本路径的上一层路径
objpath = os.path.abspath('..')

# 删除不是当天的日志
path = objpath + "\\logs\\"
timestr = time.strftime('%Y%m%d', time.localtime(time.time()))
listfile = os.listdir(path)

if os.path.exists(path):
    for i in listfile:

        if timestr in i:
            pass

        else:
            ipath = path + i
            os.remove(ipath)
else:
    print("初始化时，日志文件夹不存在！")

# 新建日志文件 打印的当天日志写入该文件
name = time.strftime('%Y%m%d%H%M', time.localtime(time.time())) + '.txt'

logger = Logger(log_file_name=name, log_level=logging.INFO, logger_name="logging").get_log()

# 自动更新元素到日志打印的名字数据里

yamlpath = objpath + '\\data\\name_data.yaml'
elepath = objpath + '\\base\\base_element.py'
if (os.path.exists(yamlpath)):
    os.remove(yamlpath)
filename = open(elepath, "r", encoding="utf-8")
str2 = "="
lines = filename.readlines()
for i in lines:
    if str2 in i:
        pattern = re.compile(r'(?<==).+?(?=")')
        out = re.sub(pattern, ':', i, count=1)
        str1 = out.replace("=:", ": ")
        # 遍历转换后写入
        with open(yamlpath, "a", encoding="utf-8") as f:
            f.writelines(str1)
            f.close()
# 在首行插入一行names 不然获取到的不是想要的数值类型
with open(yamlpath, "r+", encoding="utf-8") as f:
    content = f.read()
    f.seek(0, 0)
    f.write('names:\n' + content)
