import sys
import pickle
sys.path.append('.')
sys.path.append('..')
from Patient import Patient
from LinearInterpolate import interpolate
from itertools import groupby
import SingleFeature
import numpy as np
import math


def main():
    # load the arguments
    data_path = sys.argv[1]
    out_feature_path = sys.argv[2]
    model_path = sys.argv[3]
    checklist = sys.argv[4]

    # load the preprocessed data
    patients = pickle.load( open( data_path, "rb" ) )

    # extract features from the loaded data
    features = []
    IDs = []
    outcomes = []

    print "Extracting features ..."
    for patient in patients:
        IDs.append(patient.ID.astype(int))
        outcomes.append(patient.In_hospital_death.astype(int))
        feature = []
        # single feature for each sign (from abba model)
        if checklist[0] == '1':
            feature_1 = np.zeros(48)
            # hard sign
            feature_1 = feature_1 +SingleFeature.Age(patient.Age) * np.ones(48)
            # soft sign
            Signs = ['HR','SysABP','Temp', 'RespRate','Urine','BUN','HCT', 'WBC','Glucose','K','Na','HCO3','GCS','DiasABP','Mg','PaCO2','PaO2','pH','SaO2']
            for sign in Signs:
                # extract features according to sign
                ind = ((patient.data[:,1]==sign) & (patient.data[:,0].astype(int)<48))
                time = patient.data[ind,0]
                val = patient.data[ind,2]
                # transfer val to float array
                val = val.astype(np.float)
                time = time.astype(np.int)
                # calculate sign values from timeseries
                if len(val) ==0:
                    # to be modified to make it more sense
                    continue
                else:
                    command = 'SingleFeature.' +sign + '(val)'
                    value = eval(command)
                    #print sign, eval('SingleFeature.' + sign + '(np.array([5]))')
                # complete the missing values
                # 1) take mean for each time
                time_set = set(time)
                value_mean = []
                for time_point in time_set:
                    value_mean.append(np.mean(value[time==time_point]))
                time = np.array(list(time_set)).astype(int)
                value = np.array(value_mean)
                # 2) sort
                sort_index = np.argsort(time)
                time= time[sort_index]
                value= value[sort_index]
                # 3) interpl
                i=range(48)
                if len(value) == 1:
                    feature_1 = feature_1 + value[0]
                    continue
                else:
                    time,value = interpolate(time,value)
                # 4) extend
                newtime = np.array(range(0,48))
                newvalue = -np.ones(48)
                newvalue[time] = value
                if (time[0]!=0):
                    newvalue[0:time[0]] = np.ones(time[0])*value[0]
                if (time[-1]!=47):
                    newvalue[time[-1]:48] = np.ones(47 - time[-1] +1)*value[-1]
                # sum the values to be feature
                feature_1 = feature_1 + newvalue

            feature.append(feature_1)

        # alek features
        if checklist[1] =='1':
            pass
        # bucket features
        if checklist[2] =='1':
            pass
        # complicated time series features (could come from the comparable feature-based TS classification method)
        if checklist[3] =='1':
            pass

        feature = np.concatenate(feature,0)
        features.append(feature)
    features = np.vstack(features)
    IDs = np.array(IDs)
    outcomes = np.array(outcomes)

    print "FeatureExtraction finished"
    out_file = out_feature_path + "/" + "features.dat"
    with open(out_file, 'w') as f:
            pickle.dump([features, IDs, outcomes], f)

    print "Data successfully saved."

if __name__ == "__main__":
    main()