#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
actfast -- Anesthesiology Control Tower FAST
Copyright (c) 2016 chen's lab <https://bitbucket.org/wustlchenlab/actfast>
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.
"""

import numpy
import csv

def load_dataset(dataset_name, dataset_folder, patient_id, read_column, lable_column):
	file_path_IntraOp = dataset_folder + "/" + str(dataset_name[0])
	file_path_Outcomes = dataset_folder + "/" + str(dataset_name[1])
	patient_id_np, read_column_np = read_large_file_numpy(file_path_IntraOp, patient_id, read_column)
	lable_column_np, lable_id_np = read_outcomes_file(file_path_Outcomes, lable_column, patient_id)

	return patient_id_np, read_column_np, lable_column_np, lable_id_np

def read_large_file_numpy(filepath, patient_id, read_column):
	field_name = csv_headers(filepath)
	patient_id_index = field_name.index(patient_id)
	read_column_index = field_name.index(read_column)
	row_no = sum(1 for row in readfile_csv(filepath))
	column_no = len(field_name)
	patient_id_np = numpy.empty(row_no, dtype=object)
	read_column_np = numpy.empty(row_no, dtype=object)
	count = 0
	for line in readfile_csv(filepath):
		patient_id_np[count] = line[patient_id_index]
		read_column_np[count] = line[read_column_index]
		count += 1
	return patient_id_np, read_column_np

def read_outcomes_file(filepath, lable_column, lable_patient_id):
	csv_content = numpy.genfromtxt(filepath, dtype=None, delimiter=',')
	column_no = csv_content.shape[1]
	row_no = csv_content.shape[0]
	lable_column_np = numpy.empty(row_no, dtype=object)
	lable_id_np = numpy.empty(row_no, dtype=object)
	field_name = csv_content[0,:]
	lable_column_index = numpy.where(field_name == lable_column)
	for i in range(0, csv_content.shape[0]):
		lable_column_np[i] = csv_content[i,lable_column_index]
		lable_id_np[i] = csv_content[i,0]
	return lable_column_np, lable_id_np


def readfile_csv(filepath):
	csvfile = file(filepath, 'rb')
	reader = csv.reader(csvfile)
	next(reader)
	return reader

def csv_headers(filepath):
	csvfile = file(filepath, 'rb')
	head_reader = csv.reader(csvfile)
	headers = []
	for i,rows in enumerate(head_reader):
		if i == 0:
			headers = rows
	return headers
