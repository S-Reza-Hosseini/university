from src.student import Student
from src.professor import Professor
from src.file_work import choose_file_name
from src.reset_json import reset_json_file

def main():
    student_1 = Student("reza", "hosseini", "39916341054465")
    student_1.pick_lecture("software engineering", "compiler")

    teacher_1 = Professor("vahid", "safari", "1")
    teacher_2 = Professor("roya", "behroozi", "2")

    teacher_1.take_lecture("software engineering" )
    teacher_2.take_lecture("compiler")

    giving_grade_1 = t1.give_grade("software engineering", 16.5)
    giving_grade_2 = t2.give_grade("compiler" ,20)

    
    
    

    return student_1.status()


print(main())

path = choose_file_name()
reset_json_file(path)
    