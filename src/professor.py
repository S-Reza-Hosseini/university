from src.role import Role
from src.file_work import save_lecture_in_json
from src.file_work import choose_file_name
from src.file_work import read_data_file
from src.update_dict import update_nested_dict_value
from src.exception import NumError

class Professor(Role):

    
    def __init__ (self, name, family, prof_id):

        super().__init__(name, family)
        self.prof_id = prof_id

        

    def give_grade(self, course_name:str, grade:float):
        
        load_path = choose_file_name()
        read_data = read_data_file(load_path)
        
        change_grade = update_nested_dict_value(read_data, course_name, grade)
        res = save_lecture_in_json(load_path, change_grade)

        return res
        

    #  need to try except
    def take_lecture(self, *args):
        num_lecture = []
        
        try:
            for input_lecture in args:
                if len(num_lecture) < 3:
                    num_lecture.append(input_lecture)
                else:
                    raise NumError()
            
        except NumError as ne:
            print(ne)

        return num_lecture
            


    def __repr__(self):
        return f"professor {self.name} {self.family} and with id {self.prof_id}"



        