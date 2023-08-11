
#contructor to start doctor class properties then establish the parameters
class Doctor:
    def __init__(self, doctor_id, name, specialization, working_time, qualification, room_number):
      
      
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number
