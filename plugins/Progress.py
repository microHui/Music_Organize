#!/usr/bin/python
#coding=utf-8

def Progress(count,total,character):
	from sys import stdout
	tot_len=50
	if total:
		percentcomplete=float(count)/float(total)
		if percentcomplete < 0:
			percentcomplete=1
	else:
		percentcomplete=1
	blockcount=int(percentcomplete/2)
	block=character*int(percentcomplete*tot_len)
	block="["+block+" "*int(tot_len-percentcomplete*tot_len)+"]"
	text="\rProcessing\t%s\t%.2f%%"%(block,percentcomplete*100)
	stdout.write(text)
	stdout.flush()

	if percentcomplete == 1: stdout.write("\n")
	blockcount_New=blockcount
	return
