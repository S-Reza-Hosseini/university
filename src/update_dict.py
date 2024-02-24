
def update_nested_dict_value(nested_dict, new_value):

    try:
        for outer_key, inner_dict in nested_dict.items():
            for inner_key in inner_dict:
                nested_dict[outer_key][inner_key] = new_value
                return nested_dict

    except NameError as nr:
        print(nr)
        print("name has error ")

