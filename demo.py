import os
import time

path = os.getcwd() + "\\logs"
timestr = time.strftime('%Y%m%d', time.localtime(time.time()))
print(timestr)
listfile = os.listdir(path)

if os.path.exists(path):
    for i in listfile:

        if timestr in i:
            pass

        else:
            ipath = path+"\\"+i
            os.remove(ipath)
else:
    print("sdsads")
