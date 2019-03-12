# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET
import os
import os.path

class XmlHandle :
	def __init__(self,path):
		self.path=path
		
	def printXml(self):
		tree = ET.parse(self.path)
		root = tree.getroot()
		self.printElement(root,0)
		
	def printElement(self,element,depth):
		#缩进显示
		indent="".rjust(depth)
		#获取标签名称和标签的值
		value=element.text
		if value is None:
			value=""
		print(indent,element.tag,"value:",value.strip())
		#获取属性
		attribKeys=element.keys()
		if len(attribKeys):
			for key in attribKeys:
				print(indent,"  ",key,":",element.get(key))
		#print (len(list(element)))
		depth+=4;
		#获取子节点
		if len(element):
			for child in element:
				self.printElement(child,depth)
				
	def buildElement(self):
		root= ET.Element("root")
		first=ET.SubElement(root,"first")
		first.text="It's first element text"
		first.set("width","100")
		first.set("height","200")
		ET.dump(root)
		
	def findXml(self):
		tree = ET.parse(self.path)
		root = tree.getroot()
		namespaces = {'android': 'http://schemas.android.com/apk/res/android'}
		res=root.findall("application")
		#print(res)
		if len(res):
			for item in res:
				self.printElement(item,0)
		
xmlHandle=XmlHandle("sample/AndroidManifest.xml")
#xmlHandle=XmlHandle("sample/styles.xml")
xmlHandle.printXml();
#xmlHandle.buildElement();
#xmlHandle.findXml();
		