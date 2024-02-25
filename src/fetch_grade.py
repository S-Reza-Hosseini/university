from src.file_work import choose_file_name
from src.file_work import read_data_file



def fetch_grade_from_dict():
    try:
        file_name = choose_file_name()
        data_read = read_data_file(file_name)

        all_grades = []
        for outer_key, inner_dict in data_read.items():
            for inner_key in inner_dict:
                data = data_read[outer_key][inner_key]
                all_grades.append(data)

        return all_grades
    except TypeError as te:
        print(te)
