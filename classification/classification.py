import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report


# digits = datasets.load_digits()

# clf = svm.SVC(gamma = 0.001, C = 100)
# print(digits.target)
# x, y = digits.data[:-10], digits.target[:-10]
# clf.fit(x,y)
# print('Prediction:', clf.predict(digits.data[-3]))
# plt.imshow(digits.images[-3], cmap=plt.cm.gray_r, interpolation = 'nearest')
# plt.show()

class Classification:

	def __init__(self, train_x, train_y, test_x, test_y):
		self.train_x = train_x
		self.train_y = train_y
		self.test_x = test_x
		self.test_y = test_y

	def svmClassifier(self):
		#svm
		clf = svm.SVC(gamma = 0.01, C = 100)
		print(type(self.train_y))
		y_train = np.asarray(self.train_y, dtype="|S6")
		clf.fit(self.train_x,y_train)
		print(clf.predict(self.test_x))
		print(self.test_y)
		self.test_y = np.asarray(self.test_y, dtype="|S6")
		prediction = clf.predict(self.test_x)
		print(classification_report(self.test_y, prediction))
		print("---SVM classifier---")

	def bayersClassifier(self):
		print("---")
		#getAccuracy()

	def decisionTreeClassifier(self):
		model = DecisionTreeClassifier()
		#model.fit(x,y)
	