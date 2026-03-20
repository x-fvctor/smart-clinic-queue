from datetime import datetime

# Patient class (OOP)
class Patient:
    def __init__(self, name):
        self.name = name
        self.time = datetime.now()

    def get_details(self):
        return f"{self.name} - {self.time.strftime('%H:%M:%S')}"


# Queue system (FIFO)
class ClinicQueue:
    def __init__(self):
        self.queue = []
        self.total_served = 0

    def add_patient(self, patient):
        self.queue.append(patient)

    def serve_patient(self):
        if self.queue:
            served = self.queue.pop(0)  # FIFO
            self.total_served += 1
            return served
        return None

    def get_all_patients(self):
        return self.queue

    def get_total_served(self):
        return self.total_served
    
    def get_name(self):
    return self.name.upper()