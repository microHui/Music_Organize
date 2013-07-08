#!/usr/bin/python
#coding=utf-8
import os
from plugins.Progress import Progress
from plugins.MoveFile import Move
from plugins.ListFiles import listDir
from plugins.Report import MakeReport

# from time import sleep
def Organize(Src,Dst):
	# make sure the variable Src not end with /
	if Src[-1] == "/":
		Src=Src[:-1]
	if not os.path.exists(Src):
		print "No such file, Program terminated"
		exit(1)

	# make sure variable Dst must end with "/"
	if Dst[-1] != "/":
		Dst=Dst+"/"
	if not os.path.exists(Dst):
		try:
			os.mkdir(Dst)
		except OSError:
			print "Cannot create distance folder, Program terminated"
			exit(1)
	
	files=listDir(Src,["mp3","wma"])
	print "Find %d files in total"%len(files)
	
	total=len(files)
	count=0
	errorList={}
	for song in files:
		result=Move(song,Dst)
		if result == 1:
			count+=1
			Progress(count,total,"#")
		else:
			errorList[song]=result
	if errorList:
		print "\nMaking Error Report"
		MakeReport(errorList,Dst)