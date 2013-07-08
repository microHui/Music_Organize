#!/usr/bin/python
#coding=utf-8
class Info:
	def __init__(self,song=None):
		self.file=song.split('/')[-1]
		self.file=self.file.replace('\00','')

		self.fileName='.'.join(self.file.split('.')[0:-1])

		self.file_artist=self.fileName.split('-')[0]
		self.file_title=self.fileName.split('-')[-1]

	def get(self):
		if self.file_artist[-1]==" ": 
			self.file_artist=self.file_artist[0:-1]
		self.file_artist.replace("  "," ")	
		if self.file_title==self.file_artist:
			try:
				regex_text=re.compile("([\D\d]*)\(([\D\d]*)\)")
				self.file_artist=regex_text.search(self.fileName).groups()[1]
				self.file_title=regex_text.search(self.fileName).groups()[0]
			except:
				self.file_artist="Unkown"

	def getArtist(self):
		return self.file_artist
	def getTitle(self):
		return self.file_title