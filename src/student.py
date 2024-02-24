from src.role import Role
from src.file_work import save_lecture_in_json
from src.file_work import choose_file_name


class Student(Role):

    # moadel ha ra dar list vared kon
    list_avg = []
    def __init__(self, name, family, std_id, grade = None):

        super().__init__(name, family)
        self.grade = grade
        self.std_id = std_id

    def pick_lecture(self, *args):
        
        for input_course in args:
            info_dict = { self.std_id : { input_course: self.grade }}
            load_path = choose_file_name()
            save_lecture  = save_lecture_in_json(load_path,info_dict)
       
      
    def avg(self):
        pass


    def status(self, msg):
        pass

       

    def __repr__(self):
        return f"student {self.name} {self.family} with id {self.std_id}"