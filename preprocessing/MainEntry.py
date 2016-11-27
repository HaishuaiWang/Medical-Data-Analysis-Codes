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

import numpy as np
import medical_dataset_loder
from patientClass import Patient
#from patientInfo import PatientInfo

def _generate_patientInfo(dataset_name, base_folder, patientID, attribute, label):
	# load the data 
	patient_id_np, read_column_np, label_column_np, label_patient_id = medical_dataset_loder.load_dataset(dataset_name, base_folder, patientID, attribute, label)
	unique_patientID = np.unique(patient_id_np)
	patients = np.empty(unique_patientID.shape[0], dtype=object)
	for obj in range(0, unique_patientID.shape[0]):
		each_patient_index = np.where(patient_id_np == unique_patientID[obj])
		#patient_label_index = np.where(label_column_np == unique_patientID[obj])
		label_patient_id_index = np.where(label_patient_id == unique_patientID[obj])
		hr_list= []
		for i in each_patient_index:
			hr_list.append(read_column_np[i])
		patients[obj] = Patient(unique_patientID[obj])
		patients[obj].set_hr(hr_list)
		patients[obj].set_outcomes_SurveyHeartFailure(label_column_np[label_patient_id_index[0][0]])
	return patients

def writefiles(filename, patientObj):
	filename = open(filename, 'a')
	for patient in patients:
		st_list = ''
		print(len(patient.get_hr()[0]))
		for i in range(0, len(patient.get_hr()[0])):
			st_list = st_list + ',' + str(patient.get_hr()[0][i])
		filename.writelines(patient.get_outcomes_SurveyHeartFailure()[0][0] + st_list + '\n')
	filename.close()

if __name__ == '__main__':
	database_name = ['IntraOp.csv', 'Outcomes.csv']
	patients = _generate_patientInfo(database_name, 'data', "PatientID", "HR", "SurveyHeartFailure")
	#write files: hr with label, time series
	filename = 'hr'
	writefiles(filename, patients)
	