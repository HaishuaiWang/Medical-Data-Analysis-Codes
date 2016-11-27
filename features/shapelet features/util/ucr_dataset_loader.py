from numpy import genfromtxt
import numpy as np


def load_dataset(dataset_name, dataset_folder):
    train_file_path = dataset_folder + "/" + dataset_name + "/" + dataset_name + "_TRAIN"
    test_file_path = dataset_folder + "/" + dataset_name + "/" + dataset_name + "_TEST"
    # read training data into numpy arrays
    f = open(train_file_path)
    train_raw_arr = np.empty((670,1790), dtype=object)
    count = 0
    for line in f.readlines():
        values = line.split(',')
        for v in range(0, len(values)):
            train_raw_arr[count][v] = values[v].strip()
        count += 1
    train_labels = train_raw_arr[:, 0]
    train_data = train_raw_arr[:, 1:]
    # read test data into numpy arrays
    ff = open(test_file_path)
    test_raw_arr = np.empty((30,700), dtype=object)
    count = 0
    for line in ff.readlines():
        values = line.split(',')
        for v in range(0, len(values)):
            train_raw_arr[count][v] = values[v].strip()
        count += 1
    test_labels = test_raw_arr[:, 0]
    test_data = test_raw_arr[:, 1:]
    return train_data, train_labels, test_data, test_labels
