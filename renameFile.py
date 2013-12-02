#-*- coding:UTF-8 -*-

import os
from localEncode import localEncodeText, unicodeFromLocalEncode
from pathHelper import pathJoin, parentPath, fileNameWithoutExtention

class FileReader(object):
	def fileUnderPath(self, folderPath, folderName='', level=1, fileList=[]):
		folderPath = localEncodeText(folderPath)
		children = os.listdir(folderPath)
		for child in children:
			childPath = pathJoin(folderPath, child)
			if os.path.isfile(childPath):
				fileDict = {}
				fileDict['fileName'] = fileNameWithoutExtention(child)
				fileDict['filePath'] = childPath
				fileDict['folderName'] = folderName
				fileDict['level'] = level
				fileDict['level2Name'] = ''
				fileDict['level3Name'] = ''
				if level == 2: fileDict['level2Name'] = folderName 
				if level == 3: 
					fileDict['level2Name'] = os.path.split( os.path.dirname( folderPath ) )[1] 
					fileDict['level3Name'] = folderName
				fileList.append(fileDict)
			elif os.path.isdir(childPath):
				fileList = self.fileUnderPath(childPath, child, level+1, fileList)
		return fileList

	def listToShow(self, fileList):
		recordList = []
		for fileDict in fileList:
			record = [	fileDict['fileName'], 
						fileDict['fileName'], 
						fileDict['level2Name'],
						fileDict['level3Name'],
						fileDict['filePath'],
					]
			recordList.append(record)
		return recordList

	def readAllFrom(self, folderPath):
		fileList = self.fileUnderPath(folderPath, fileList=[])
		showList = self.listToShow(fileList)
		return fileList, showList

def test():
	folderPath = u'f:\\temp\\中文目录'
	fileList, showList = FileReader().readAllFrom(folderPath)
	print fileList
	print showList

if __name__ == '__main__':
	test()