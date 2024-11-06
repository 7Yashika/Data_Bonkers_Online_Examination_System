from models.user_model import SessionLocal, User, Student

class ExamService:
    def __init__(self):
        self.db = SessionLocal()

    def get_user(self, user_id):
        return self.db.query(User).filter(User.user_id == user_id).first()

    def create_user(self, user_data):
        user = User(**user_data)
        self.db.add(user)
        self.db.commit()
        return user
    
    def update_user(self, user_id, user_data):
     user = self.get_user(user_id)
     if user:
        for key, value in user_data.items():
         setattr(user, key, value)
        self.db.commit()  
        return user
     

            
    def delete_user(self,user_id):
        user=self.get_user(user_id)   
        if user:
            self.db.delete(user)
            self.db.commit()
            return user    
    
#student

    def get_student(self, student_id):
        return self.db.query(Student).filter(Student.student_id == student_id).first()

    def create_student(self, student_data):
        student = Student(**student_data)
        self.db.add(student)
        self.db.commit()
        return student

    def update_student(self, student_id, student_data):
     student = self.get_user(student_id)
     if student:
        for key, value in student_data.items():
         setattr(student, key, value)
        self.db.commit()  
        return student
    
            
    def delete_student(self,student_id):
        student=self.get_student(student_id)   
        if Student:
            self.db.delete(student)
            self.db.commit()
            return student 