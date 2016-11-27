#!/usr/bin/python
# -*- coding: UTF-8 -*-

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

class Patient:

	def __init__(self, patientID):
		self.ID = patientID

	def set_patientID(self, patientID):
		self.ID = patientID

	def set_sex(self, sex):
		self.sex = sex

	def set_hr(self, hr_list):
		self.hr = hr_list

	def set_outcomes_HeartAttack(self, heartattack):
		self.heartattack = heartattack

	def get_patientID(self):
		return self.ID

	def get_hr(self):
		return self.hr

	def get_outcomes_heartAttach(self):
		return self.heartattack

	def set_outcomes_SurveyHeartFailure(self, SurveyHeartFailure):
		self.SurveyHeartFailure = SurveyHeartFailure

	def get_outcomes_SurveyHeartFailure(self):
		return self.SurveyHeartFailure