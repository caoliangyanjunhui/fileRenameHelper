#-*- coding:UTF-8 -*-

import os
from localEncode import localEncodeText, unicodeFromLocalEncode
from pathHelper import pathJoin, parentPath

class FileReader(object):
	def fileUnderPath(self, folderPath, folderName='', level=1, fileList=[]):
		folderPath = localEncodeText(folderPath)
		children = os.listdir(folderPath)
		for child in children:
			childPath = pathJoin(folderPath, child)
			if os.path.isfile(childPath):
				head, ext = os.path.splitext(child)
				fileDict = {}
				fileDict['fileName'] = child
				fileDict['fileHead'] = head
				fileDict['newHead'] = head
				fileDict['fileExt'] = ext
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
			record = [	fileDict['fileHead'], 
						'', 
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


class FileRename(object):
	def __init__(self, fileList, operations):
		self.fileList = fileList
		self.operations = operations

	def preview(self):
		if not self.operations: return
		self.excuteNewName()
		self.excuteAddNum()
		return self.fileList, self.listToShow(self.fileList)

	def excuteNewName(self):
		newName = self.operations['newName']
		if not newName: return
		newName = localEncodeText(newName)
		operation = self.operations['newNameOperation']
		if operation == 'replace':
			self.setNewName( newName )
		elif operation == 'prefix':
			self.addNamePrefix( newName )
		elif operation == 'postfix':
			self.addNamePostfix( newName ) 

	def setNewName(self, newHead):
		print 'setNewName', newHead
		for fileDict in self.fileList:
			fileDict['newHead'] = newHead

	def addNamePrefix(self, prefix):
		for fileDict in self.fileList:
			fileDict['newHead'] = prefix + fileDict['fileHead']

	def addNamePostfix(self, postfix):
		for fileDict in self.fileList:
			fileDict['newHead'] = fileDict['fileHead'] + postfix

	def excuteAddNum(self):
		startNum = self.operations['startNum']
		if not startNum: return
		operation = self.operations['addNumOperation']
		if not operation: return
		if operation == 'prefix':
			self.addNumPrefix(startNum)
		elif operation == 'postfix':
			self.addNumPostfix(startNum)

	def addNumPrefix(self, startNum):
		num = int(startNum)
		for fileDict in self.fileList:
			prefix = str(num).zfill(len(startNum))
			fileDict['newHead'] = prefix + fileDict['newHead']
			num += 1

	def addNumPostfix(self, startNum):
		num = int(startNum)
		for fileDict in self.fileList:
			postfix = str(num).zfill(len(startNum))
			fileDict['newHead'] = fileDict['newHead'] + postfix
			num += 1

	def listToShow(self, fileList):
		recordList = []
		for fileDict in fileList:
			record = [	fileDict['fileHead'], 
						fileDict['newHead'], 
						fileDict['level2Name'],
						fileDict['level3Name'],
						fileDict['filePath'],
					]
			recordList.append(record)
		return recordList

def test():
	folderPath = u'f:\\temp\\中文目录'
	fileList, showList = FileReader().readAllFrom(folderPath)
	print fileList
	print showList
	print FileRename(fileList, {'newNameOperation':'replace', 'newName':u'new', 
		'addNumOperation':'prefix', 'startNum':'001'}).preview()

if __name__ == '__main__':
	test()