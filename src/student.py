from src.role import Role
from src.file_work import save_lecture_in_json
from src.file_work import read_data_file
from src.file_work import choose_file_name
from src.fetch_grade import fetch_grade_from_dict


class Student(Role):

    # moadel ha ra dar list vared kon
    list_avg = []
    def __init__(self, name, family, std_id, grade = None):

        super().__init__(name, family)
        self.grade = grade
        self.std_id = std_id

    def pick_lecture(self, *args):
        info_dict = {}
        
        for input_course in args:
            info_dict.setdefault(self.std_id, {})[input_course] = self.grade
        
        load_path = choose_file_name()
        save_lecture = save_lecture_in_json(load_path, info_dict)


       
      
    def avg(self):
        
        grade = fetch_grade_from_dict()
        
        return (sum(grade) / len(grade))
        


    def status(self):
        msg = "normal"
        if self.avg() < 12 :
            msg = "mashroot"

        return msg
       

    def __repr__(self):
        return f"student {self.name} {self.family} with id {self.std_id}"