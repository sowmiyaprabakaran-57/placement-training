class Patient:
    def __init__(self, name, illness, treatment_cost):
        self.name = name
        self.illness = illness
        self.treatment_cost = treatment_cost

def total_treatment_cost(patients, illness):
    return sum(patient.treatment_cost for patient in patients if patient.illness == illness)
patients = [Patient("John", "Flu", 100), Patient("Jane", "Flu", 120), Patient("Doe", "Cold", 80)]
print(total_treatment_cost(patients, "Flu")) 
