# #!/usr/bin/python3
# """practicing on input/output python"""


# def read_file(filename=""):
#     """read the file with encoding UTF8"""

#     with open(filename, encoding="UTF8") as myfile:
#        for line in myfile:
#             print(line, end="")
#!/usr/bin/python3
"""practicing on input/output python"""
import json


def load_from_json_file(filename):
    """ returns the JSON
    representation of an
    object (string)"""
    with open(filename, 'r') as my_file:
        data = json.load(my_file)
        return data
filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

filename = "my_dict.json"
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

try:
    filename = "my_set_doesnt_exist.json"
    my_set = load_from_json_file(filename)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filename = "my_fake.json"
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
