from src.student import Student
from src.professor import Professor

def main():

    s1 = Student("reza", "hosseini", "39916341054461")
    inp_course = s1.pick_lecture("zaban", "compiler", "adabiat", "shimi")
    

    
    # t1 = Professor("vahid", "safari", "1")
    # give_grade = t1.give_grade(16.5)
    # take_lecture = t1.take_lecture("zaban", "compiler", "adabit","shimi")

    # t2 = Professor("sayed taleb", "mousavi" , "2")
    # give_grade = t1.give_grade(16.5)
    # take_lecture("shimi")
    # return take_lecture

print(main())