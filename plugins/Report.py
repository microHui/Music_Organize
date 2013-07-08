#!/usr/bin/python
#coding=utf-8
import os
import re
def MakeReport(errors,dst):
	fileName=dst+"ErrorReport.txt"
	if os.path.exists(fileName):
		os.remove(fileName)
	report=open(fileName,"a+")
	for error in errors.keys():
		try:
			reason=str(errors[error]).split(":")[0]
			reg=re.compile("[[\Dd]*] ([\Dd]*)")
			reason=' '.join(reg.search(reason).groups())
		except AttributeError:
			reason="unrecognized reason"
		sentence="Cannot move \"%s\" caused by %s.\n\n"%(error, reason)
		report.write(sentence)
