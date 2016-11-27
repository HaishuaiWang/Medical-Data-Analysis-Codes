import numpy as np
import os
from itertools import groupby
from operator import itemgetter

def interpolate(path,newpath):
	#content = np.genfromtxt(path, dtype=None, delimiter=',')
	f = open(path,'r')
	w = open(newpath, 'a')
	for line in f.readlines():
		values = line.split(",")
		line_np = np.empty(len(values), dtype=object)
		for v in range(0, len(values)):
			line_np[v] = values[v].strip()
		null_index = np.where(line_np == 'NULL')
		delete_index = []
		for np_value in null_index:
			for group in group_consecutives(np_value):
				if len(group) > 0:
					if len(group) > 4 or group[0] == 1 or group[len(group)-1] == len(values)-1:
						for i in group:
							delete_index.append(i)
					else:
						interpolate = (int(line_np[group[0]-1]) + int(line_np[group[len(group)-1]+1])) / 2
						for g in group:
							line_np[g] = interpolate
		line_np = np.delete(line_np,delete_index)
		writefile(line_np,w)

def writefile(lines,write_obj):
	#print(lines)
	for l in range(0, len(lines)-1):
		write_obj.write(str(lines[l]) + ',')
	write_obj.write(lines[len(lines)-1] + '\n')

def group_consecutives(vals, step=1):
	"""Return list of consecutive lists of numbers from vals (number list)."""
	run = []
	result = [run]
	expect = None
	for v in vals:
		if (v == expect) or (expect is None):
			run.append(v)
		else:
			run = [v]
			result.append(run)
		expect = v + step
	return result

def count_length(path):
	f = open(path)
	length = []
	for line in f.readlines():
		l = line.split(',')
		length.append(len(l)-1)
	print("Max length: " + str(max(length)))
	print("Min length: "  + str(min(length)))

if __name__ == '__main__':
	currentPath = os.getcwd()
	parent_path = os.path.dirname(currentPath)
	filename = 'hr'
	filepath = parent_path + '\\data\\' + filename
	newfilename = "interpolate_hr"
	newfilepath = parent_path + '\\data\\' + newfilename
	#interpolate(filepath, newfilepath)
	count_length(newfilepath)