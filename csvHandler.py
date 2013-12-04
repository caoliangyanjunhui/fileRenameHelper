# -*- coding: UTF-8 -*-

from fileHelper import saveTextFile
import os
from pathHelper import pathJoin
from localEncode import localEncodeText, unicodeFromLocalEncode

class CSV(object):
	def write(self, filePath, dataList ):
		text = self.dataListToText(dataList)
		saveTextFile(filePath, text)

	def dataListToText(self, dataList):
		text = ''
		for item in dataList:
			line = ','.join(item)
			text += line + '\n'
		return text


def text():
	dataList = [['a','b'],['c', 'c']]
	CSV().write(dataList)



if __name__ == '__main__':
	text()
