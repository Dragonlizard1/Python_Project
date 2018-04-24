class Patient_info(object):
	def __init__(self, id1, name, allergy):
		self.id1 = id1
		self.name = name
		self.allergy = allergy
		self.bed = "none"

class Hospital(object):
	def __init__(self, name, capacity):		
		self.patient = []
		self.hospital_name = name
		self.capacity = capacity		#max num 
		self.discharge_patient = []
		self.bednum = []
		for i in range(capacity+1)
			self.bednum[i-1] = i

	def Admit(self, id1, name, allergy):		
		if len(self.patient) <= self.capacity:
			self.patient.append(Patient_info(id1, name, allergy))	
			print "Admission is completed."
		else:
			print "Hospital is full"
		return self

	def Discharge(self, name):
		for i in range(len(self.patient)):
			if name == self.patient[i].name:
				self.patient[i].bed = "none"
				self.discharge_patient.append(self.patient[i])
				self.patient.pop(i)		
				return self
			
		print "Can not find the name"
		return self

	def Bedassign(self, name, num):
		for i in range(len(self.patient)):
			if name == self.patient[i].name:			
				self.patient[i].bed = num
				print "Bed is assigned"
				print ""
				return self

		print "Can not find the name"
		return self

	def display(self, name, type1):

		if type1 == "discharge":
			for i in range(len(self.discharge_patient)):
				if name == self.discharge_patient[i].name:
					print "This person is discharged"
					print "ID:", self.discharge_patient[i].id1
					print "Name:", self.discharge_patient[i].name
					print "Allergy:", self.discharge_patient[i].allergy
					print "Bed:", self.discharge_patient[i].bed
					print ""
					return self
			print "Can not find the name in discharge list"

		elif type1 == "whole_discharge":
			print "The whole discharge list"
			for i in range(len(self.discharge_patient)):
				print "ID:", self.discharge_patient[i].id1
				print "Name:", self.discharge_patient[i].name
				print "Allergy:", self.discharge_patient[i].allergy
				print "Bed:", self.discharge_patient[i].bed
				print ""
					
		elif type1 == "inpatient":
			for i in range(len(self.patient)):
				if name == self.patient[i].name:
					print "In patient is in."
					print "ID:", self.patient[i].id1
					print "Name:", self.patient[i].name
					print "Allergy:", self.patient[i].allergy
					print "Bed:", self.patient[i].bed
					print ""
					return self
			print "Can not find the name in patient list"

		elif type1 == "whole_inpatient":
			print "The whole in patient list"
			for i in range(len(self.patient)):
					print "ID:", self.patient[i].id1
					print "Name:", self.patient[i].name
					print "Allergy:", self.patient[i].allergy
					print "Bed:", self.patient[i].bed
					print ""

Baylor = Hospital("Baylor Medical Center", 100)
Baylor.Admit(1, "bob", "hiccup")
Baylor.Admit(2, "jacob", "goose")
Baylor.Admit(13, "david", "itch")
Baylor.Admit(45, "rob", "people")
Baylor.Bedassign("jacob", 25)
Baylor.Bedassign("bob", 125)
Baylor.Bedassign("rob", 325)
Baylor.Bedassign("david", 225)
print Baylor.patient[0].bed
print Baylor.patient[1].bed
print Baylor.patient[2].bed
print Baylor.patient[3].bed
Baylor.Discharge("david")
Baylor.display("david", "discharge")
Baylor.display("","whole_inpatient")