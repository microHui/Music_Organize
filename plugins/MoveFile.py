#!/usr/bin/python
#coding=utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import shutil
from Tags.Tag import getTag

def Move(song,Dst):
	try:
		artist=getTag(song)
		if not os.path.exists(Dst+artist):
			os.mkdir(Dst+artist)
		shutil.copy(song,Dst+artist)	
		return 1
	except:
		info=sys.exc_info()  
		return info[1]