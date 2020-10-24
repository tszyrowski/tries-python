'''
Created on 3 Oct 2020

@author: tszyr
'''
my_dict = [
    {"id": "a", 'val': 1},
    {"id": "b", "val": 2},
    {"id": "c", "val": 2}
]

def get_dict_by_id_(dict_list, dict_id):
    """find dict where id is a value"""
    return next(
        (iner_dict for iner_dict in dict_list if iner_dict["id"] == dict_id),
        None
    )

def get_dict_by_id(dict_list, dict_id):
    """find dict where id is a value"""
    for iner_dict in dict_list:
        if iner_dict["id"] == dict_id:
            d = iner_dict
            return d
    return None

if __name__ == "__main__":
    print(get_dict_by_id(my_dict, "b"))
    assert get_dict_by_id(my_dict, "b") == {"id": "b", "val": 2}
    assert get_dict_by_id(my_dict, "c") == {"id": "c", "val": 2}
    print("all good")