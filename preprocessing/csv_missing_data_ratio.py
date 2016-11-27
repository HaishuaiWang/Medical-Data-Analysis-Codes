# coding: utf-8

import csv
import os
import numpy as np
import sys

def readfile_csv(filepath):
	csvfile = file(filepath, 'rb')
	reader = csv.reader(csvfile)
	return reader

def readfile_numpy(filepath):
	csv_content = np.genfromtxt(filepath, dtype=None, delimiter=',')
	column_no = csv_content.shape[1]
	row_no = csv_content.shape[0]
	for i in range(0, column_no):
		csv_content = csv_content.astype(np.str)
		#print(csv_content[1:,i])
		null_index = np.where(csv_content[1:,i] == 'NULL')
		sys.stdout.write(str(csv_content[0,i]) + ', ')
		ratio = (len(null_index[0]) * 100) / int(row_no - 1)
		if ratio > 0:
			print(str(csv_content[0,i]) + ' missing ratio: ' + str(int(ratio)) + '%')

def read_large_file_numpy(filepath):
	field_name = []
	for i,rows in enumerate(readfile_csv(filepath)):
		if i == 0:
			field_name = rows
	print(field_name)
	row_no = sum(1 for row in readfile_csv(filepath))
	print(row_no)
	column_no = len(field_name)
	column_np = np.zeros(column_no)
	for line in readfile_csv(filepath):
		for element in range(0, column_no):
			if str(line[element]) == 'NULL':
				column_np[element] += 1
	column_np = column_np.astype(np.int)
	for i in range(0, column_np.shape[0]):
		ratio = (column_np[i] * 100) / row_no
		if ratio > 0:
			#print(field_name[i]  + ' missing ratio: ' + str(int(ratio)) + '%')
			sys.stdout.write('('+field_name[i]+', '+str(int(ratio))+'%), ')

if __name__ == '__main__':
	currentPath = os.getcwd()
	filename = 'PreOp.csv'
	filepath = currentPath + '\\' + filename
	#readfile_csv(filepath)
	print('------ PreOp.csv ------')
	#readfile_numpy(filepath)
	print('------ IntraOp.csv ------')
	filepath1 = 'IntraOp.csv'
	#read_large_file_numpy(filepath1)
	print('-----Outcomes.csv-----')
	filepath2 = 'Outcomes.csv'
	readfile_numpy(filepath2)