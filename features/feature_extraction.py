import numpy as np 


class Features:

	def __init__(self, train_data, train_label):
		self.train_data = train_data
		self.train_label = train_label

	def maxmin(self):
		print("Extracting Maximum, Minimum and Mean features...")
		#read files
		maxmum_list = []
		minmum_list = []
		mean_list = []
		for instance in self.train_data:
			minimum = 300
			maxmum_list.append(np.amax(instance))
			length = 0
			sum_i = 0
			for i in instance:
				if i != None:
					sum_i += i
					length += 1
					if i < minimum:
						minimum = i
			mean = sum_i / length
			minmum_list.append(minimum)
			mean_list.append(mean)
		x_train_features = np.empty((self.train_data.shape[0], 3), dtype = object)
		#y_train_labels = self.train_label
		for index in range(0, len(maxmum_list)):
			x_train_features[index][0] = maxmum_list[index]
			x_train_features[index][1] = minmum_list[index]
			x_train_features[index][2] = mean_list[index]
		return x_train_features, self.train_label
