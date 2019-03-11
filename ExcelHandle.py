# -*- coding: UTF-8 -*-
import os
import os.path

import xlrd
import xlwt

# Excel操作类
class ExcelHandle:

	def __init__(self,path):
		self.path=path
	
	
	#输出到Excel
	def write2Excel(targetPath,sheetName,data):
		if len(targetPath) <=0 :
			print("error. targetPath is empty ")
			return
		else:
			print("targetPath %s"%(targetPath))
			
		if len(sheetName) <=0 :
			sheetName="Sheet1"
			print("sheetName is empty . use default name %s"%(sheetName))
		else:
			print("sheetName is %s"%(sheetName))
			
		rowLen=len(data)
		if rowLen <= 0:
			print("error. data len is 0")
			return
		else:
			print("data row %d"%(rowLen))
			
		workbook = xlwt.Workbook(encoding = 'ascii')
		worksheet = workbook.add_sheet(sheetName)
		rowIndex=0;
		for rowData in data:
			columnIndex=0;
			for value in rowData:
				worksheet.write(rowIndex, columnIndex, label = value)
				columnIndex+=1
			rowIndex+=1
		workbook.save(targetPath)
		print("save success!")
		
	#读取Excel
	def readExcel(self):
		data = xlrd.open_workbook(self.path)
		table = data.sheet_by_index(0) #通过索引顺序获取
		#print (table.nrows)
		#print (table.ncols)
		v=[]
		for index in range(table.nrows) :
			rowData=[]
			for col in range(table.ncols) :
				#print(table.row_values(index)[col])
				rowData.append(table.row_values(index)[col])
			v.append(rowData)
		return v
		
import datetime
