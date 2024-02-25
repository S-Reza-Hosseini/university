
def update_nested_dict_value(nested_dict, course_name, new_value):

    try:
        for outer_key, inner_dict in nested_dict.items():
            for inner_key in inner_dict:
                if course_name in [inner_key] :

                    nested_dict[outer_key][inner_key] = new_value
                    return nested_dict

    except NameError as nr:
        print(nr)
        print("name has error ")

    except KeyError as ke:
        print(ke)
        print("key not found in subkey")
    
    except TypeError as te:
        print(te)
       