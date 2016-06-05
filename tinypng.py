#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import os.path
import tinify

tinify.key = "zidrhYcSiBTy3oUEQLCdfjW6hQWmVEtW"	 # APIKAY

img_w = 300
img_h = 533

#----------------------------------------------------------

print "Start..."

currentPath = os.getcwd()
fromFilePath = currentPath # 源路径
toFilePath = currentPath+"/tiny" # 输出路径

# print "workspace:"+fromFilePath
# print "ouputspace:"+toFilePath

print "Compression，please wait ..."

for root, dirs, files in os.walk(fromFilePath):
	for name in files:
		fileName, fileSuffix = os.path.splitext(name)
		if fileSuffix == '.png' or fileSuffix == '.jpg' or fileSuffix == '.jpeg':
			toFullPath = toFilePath + root[len(fromFilePath):]
			toFullName = toFullPath + '/' + name

			if os.path.isdir(toFullPath):
				pass
			else:
				os.mkdir(toFullPath)

			source = tinify.from_file(root + '/' + name)
			if len(sys.argv)>=2 and sys.argv[1]=="-s":
				resized = source.resize(
					method="fit",
					width=img_w,
					height=img_h
				)
				resized.to_file(toFullName)
				pass
			else:
				source.to_file(toFullName)
			
			with open(toFullName, 'rb') as source:
			    source_data = source.read()
			    result_data = tinify.from_buffer(source_data).to_buffer()

print "Successful !"

