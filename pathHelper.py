# -*- coding: UTF-8 -*-
import os
import shutil
import localEncode



def pathJoin(parentPath, childNmae):
	return os.path.join( localEncode.localEncodeText(parentPath), localEncode.localEncodeText(childNmae) )

def copyToPath(sourcePath, destinationPath):
	try:
		if os.path.isdir(sourcePath):
			shutil.copytree(sourcePath, destinationPath)
		else:
			shutil.copy(sourcePath, destinationPath)
	except Exception, e:
		print e

def moveToPath(sourcePath, destinationPath):
	try:
		shutil.move(sourcePath, destinationPath)
	except Exception, e:
		print e

def removePath(path):
	if not os.path.exists(path): return
	try:
		if os.path.isfile(path):
			os.remove(path)
		else:
			os.system('rd/s/q %s' % path)
	except Exception, e:
		print e

def copyToPathWithOverWrite(sourcePath, destinationPath):
	removePath(destinationPath)
	try:
		copyToPath(sourcePath, destinationPath)
	except Exception, e:
		print e

def moveToPathWithOverWrite(sourcePath, destinationPath):
	removePath(destinationPath)
	try:
		shutil.move(sourcePath, destinationPath)
	except Exception, e:
		print e

def parentPath(path):
	return os.path.abspath(pathJoin(path, os.path.pardir))

def createFolder(path):
	try:
		if os.path.exists(path):
		 	if os.path.isdir(path): 
		 		return
		 	else:
		 		removePath(path)
		os.mkdir(path)
		return True
	except Exception, e:
		print e
		return False

def exists(path):
	return os.path.exists( localEncode.localEncodeText(path) )

def childFolderList(folderPath):
	folderPathDict = {}
	folderPath = localEncode.localEncodeText(folderPath)
	if not exists(folderPath): return folderPathDict
	dirList = os.listdir(folderPath)
	for item in dirList:
		itemPath = pathJoin(folderPath, item)
		if os.path.isdir(itemPath):
			folderPathDict[item] = itemPath
	return folderPathDict

def readText(filePath):
	text = ''
	filePath = localEncode.localEncodeText(filePath)
	if not exists(filePath): return text
	f = open(filePath, 'r')
	try:
		text = f.read()
	except Exception, e:
		print e
	finally:
		f.close()
	return localEncode.unicodeFromLocalEncode(text)