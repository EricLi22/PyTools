# -*- coding: UTF-8 -*-
import sys;
sys.path.append('ExcelHandle.py');
from ExcelHandle import ExcelHandle
import datetime

excelHandle=ExcelHandle('sample/ExcelHandleTest.xlsx')
data=excelHandle.readExcel()
i = datetime.datetime.now()
outFileName="Debug/ExcelHandleTest_res_%s%s%s.xls"%(i.year, i.month, i.day)
ExcelHandle.write2Excel(outFileName,"arvin",data)