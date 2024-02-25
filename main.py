from src.student import Student
from src.professor import Professor
from src.file_work import choose_file_name
from src.reset_json import reset_json_file

def main():
    s1 = Student("reza", "hosseini", "39916341054465")
    s1.pick_lecture("software engineering", "compiler")

    t1 = Professor("vahid", "safari", "1")
    t2 = Professor("farzad", "ghahremani", "2")

    t = t1.take_lecture("software engineering" )
    a = t2.take_lecture("compiler")

    giving_grade_1 = t1.give_grade("software engineering", 16.5)
    giving_grade_2 = t2.give_grade("compiler" ,12)

    
    
    

    return s1.status()


print(main())

path = choose_file_name()
reset_json_file(path)
    