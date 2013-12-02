# -*- coding: UTF-8 -*-

from fileHelper import saveTextFile
import os
from pathHelper import pathJoin

class CSV(object):
	def write(self, dataList):
		text = self.dataListToText(dataList)
		filePath = pathJoin(os.getcwd(), u'导出文件表格.csv')
		saveTextFile(filePath, text)
		return filePath

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
