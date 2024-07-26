class Appointment:
    def __init__(self, patient_name, doctor_name, appointment_fee):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.appointment_fee = appointment_fee
def total_doctor_income(appointments, doctor_name):
    return sum(appointment.appointment_fee for appointment in appointments if appointment.doctor_name == doctor_name)
appointments = [Appointment("Alice", "Dr. Smith", 100), Appointment("Bob", "Dr. Smith", 150), Appointment("Charlie", "Dr. Jones", 200)]
print(total_doctor_income(appointments, "Dr. Smith"))  
