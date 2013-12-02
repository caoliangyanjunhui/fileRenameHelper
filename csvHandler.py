# -*- coding: UTF-8 -*-

from fileHelper import saveTextFile

class CSV(object):
	def write(self, dataList):
		text = self.dataListToText(dataList)
		print text
		saveTextFile('export.csv', text)

	def dataListToText(self, dataList):
		text = ''
		for item in dataList:
			print
			line = ','.join(item)
			print line
			text += line + '\n'
		return text


def text():
	dataList = [['a','b'],['c', 'c']]
	CSV().write(dataList)



if __name__ == '__main__':
	text()
