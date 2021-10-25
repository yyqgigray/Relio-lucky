# -*- coding: UTF-8 -*-
import re
import string




def replaceContent(content,replaceArr,regdict):
	output = ''
	print("替换前：" + content)
	for x in replaceArr:
		output = re.sub(r'[\\' + x + ']', regdict[x], content)
		content = output
	print("替换后：" + output)
	return output

def findError(content,findArr):
	errArr = []
	if(len(findArr) == 0):
		for i in range(len(content)):
			print(content[i])
			if (string.punctuation).find(content[i]) >= 0:
				errArr.append(float(i))
	else:
		for i in range(len(content)):
			if string.punctuation.find(findArr[i]) >= 0:
				errArr.append(float(i))
	print(errArr)
	return errArr






