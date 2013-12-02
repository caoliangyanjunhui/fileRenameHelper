# -*- coding: UTF-8 -*-

LOCAL_ENCODE = 'gbk'

def localEncodeText(text):
	if isinstance(text, unicode):
		return text.encode( LOCAL_ENCODE )
	else:
		return text

def unicodeFromLocalEncode(text):
	if isinstance(text, unicode):
		return text
	else:
		return text.decode( LOCAL_ENCODE )

def utf8(text):
	if isinstance(text, unicode):
		return text.encode('UTF-8')
	else:
		return text