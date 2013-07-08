#!/usr/bin/python
#coding=utf-8
import re
try:
	import eyeD3
except:
	print "Current not find eyeD3, try install it."
	exit(1);
import FileTag

artistList=[]
def getTag(song):
	file_ext=song.split('.')[-1].lower()

	artist=""
	title=""
	tag_artist=""
	tag_title=""
	file_artist=""
	file_title=""

	if file_ext == "mp3":
		tag = eyeD3.Tag()
		tag.link(song)
		tag_artist=tag.getArtist()
		tag_title=tag.getTitle()
		title=tag_title

	# if tag_artist.replace(" ","").replace("\00","") == "" :
	# 	audiofile = eyeD3.load(song)
	# 	audiofile.tag.artist = file_artist
	# 	audiofile.tag.title = file_title
	# 	title=file_title

	if tag_artist.replace(" ","").replace("\00","") == "" :
		File = FileTag.Info(song)
		File.get()
		file_artist = File.getArtist()
		file_title = File.getTitle()
		if file_artist.replace(" ","").replace("\00","") != "" :
			artist = file_artist
	else:
		artist = tag_artist

	# Capitalize the first letter
	artist=artist.lower()
	artist=" ".join([k.capitalize() for k in artist.split(" ")])
	title=title.lower()
	title=" ".join([k.capitalize() for k in title.split(" ")])

	# if not artist in artistList:
	# 	artistList.append(artist)

	return artist.replace("/","")

