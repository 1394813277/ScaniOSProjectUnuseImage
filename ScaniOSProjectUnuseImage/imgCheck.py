import sys
import os

# 查找iOS工程内所有的.m文件的图片

mFileCount = 0

a = set() #.m文件里面的图片
b = set() #工程里面的图片

deleteList = ['.jpg','.png','@2x','@3x']

def checkFile(path):
    global a
    try:
        with open(path,'r') as f:
            for each_line in f:
                if  r'@"' in each_line:
                    eachLineArr = each_line.split(r'"')
                    if len(eachLineArr) > 0:
                        imageStr = eachLineArr[1]
                        # print(imageStr)
                        a.add(imageStr)
    except OSError as reason:
        print('文件读取出错'+path+str(reason))

def printPath(path):
    global b
    global mFileCount
    list = os.listdir(path) #列出文件夹下所有的目录与文件
    for i in list:
        path1 = os.path.join(path,i)
        if os.path.isfile(path1):

            if path1.lower().endswith('.jpg') or path1.lower().endswith('.png'):
                res = i.lower()

                for deleteStr in deleteList:
                    if deleteStr in res:
                        res = res.replace(deleteStr,'')


                b.add(res)
            if path1.endswith('.m'):
                checkFile(path1)
        else:
            printPath(path1)

if __name__ == "__main__":
    printPath(sys.argv[1])
    count = 0

    for str in b - a:
        print('project un use image file is ======' + str) #有用但是文件没发现1
        count+=1

    print('total = %d' % count)
