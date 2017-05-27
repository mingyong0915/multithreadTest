#!/usr/bin/env python  
# _*_ coding:utf-8 _*_

""" 
@version: v1.0 
@author: MingYong 
@license: Apache Licence  
@contact: 13760182207@163.com 
@site: http://blog.csdn.net/mingyong_blog 
@software: PyCharm Community Edition 
@file: threadingTest2.py.py
@time: 2017/5/26 15:35
"""
import requests
import os
import threading
import time

def file2txt(filePath,url):
    try:
            if os.path.isfile(filePath):
                fileLength = len(filePath.split("."))
                fileType = filePath.split(".")[fileLength-1]
                files = {'file':open(filePath, 'rb')}
                r = requests.post(url, files=files)
                outputFolder = "C:\\Users\\yong\\Desktop\\数据架构师测试集\\数据架构测试集\\架构师Extract\\"
                txtFileName = filePath.split("\\")[-1]+".txt"
                outputPath = outputFolder.decode("utf-8")+txtFileName
                f = open(outputPath, "w")
                f.write(r.json()["data"].encode("utf-8"))
                f.close()
            else:
                return None
    except Exception, e:
            print "error message " ,e

def produce_file(dir_path):
    '''返回一个目录下所有的文件'''
    all_files = []
    filelist = os.listdir(dir_path.decode("utf-8"))
    for file in filelist:
        filePathName = dir_path.decode("utf-8")+"\\"+file
        all_files.append(filePathName)
    return all_files

def test():
    thread_list = []
    all_files = produce_file("C:\\Users\\yong\\Desktop\\数据架构师测试集\\数据架构测试集\\架构师")
    url = "http://106.15.43.96:8083/docparser/content"
    start = time.time()
    # for i in xrange(100):
    #     file2txt(all_files[i],url)
    for i in xrange(100):
        sthread = threading.Thread(target=file2txt, args=(all_files[i],url))
        sthread.setDaemon(True)
        sthread.start()
        thread_list.append(sthread)
    for i in xrange(100):
        thread_list[i].join()
    print "花费时间: %s" % (time.time() - start)

if __name__ == "__main__":
    test()