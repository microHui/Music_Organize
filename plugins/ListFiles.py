#!/usr/bin/python
#coding=utf-8

import os
from glob import glob
files=[]
def listDir(dic,fileExtlist):
	for fileName in glob(dic+"/*"):
		if os.path.isdir(fileName):
			listDir(fileName,fileExtlist)
		elif fileName.lower().split(".")[-1] in fileExtlist:
				files.append(fileName)
		continue
	return files