"""This code is intended to show how container methods works."""


def norm_name(name, r, patronymic):
    """Transform full name in normal form."""
    full_name = name.strip().lower().replace('r', r).replace('ddd', patronymic).title()
    return full_name


my_name = norm_name(" вишневецька Rнастасія DdD", 'А', 'Володимирівна')
ann_name = norm_name(" шевченко Rня DdD", 'А', 'По батькові')
print(f"\nMy fullname -> {my_name}\n"
      f"Ann's name -> {ann_name}\n")


def letter_list(normal_name):
    letters_list = []
    for i in normal_name:
        if i != ' ':
            letters_list.append(i)
    return letters_list


def list_unique(letters):
    letters = [(j.replace('а', 'А')) for j in letters]
    new_list = sorted(set(letters))
    print(f"Length of list: {len(new_list)}")
    return new_list


my_nameList0 = letter_list(my_name)
ann_nameList0 = letter_list(ann_name)
my_nameList = list_unique(my_nameList0)
ann_nameList = list_unique(ann_nameList0)
print(f"My unique name_list features -> {my_nameList}\n"
      f"Ann's unique name_list features-> {ann_nameList}\n")


def dict_l(list_letters):
    """Return dictionary, where
    keys are letters and values are
    numbers of letters
    """
    dict_letters = {}
    for i in list_letters:
        dict_letters[i] = ord(i)
    return dict_letters


myDictionary = dict_l(my_nameList0)
annDictionary = dict_l(ann_nameList0)
print(f"My dictionary -> {myDictionary}\n"
      f"Ann's dictionary-> {annDictionary}\n")


def dict_get(diction, key):
    return diction.get(key)


my_value = dict_get(myDictionary, 'А')
ann_value = dict_get(annDictionary, 'а')
print(f"my value of key -> {my_value}\n"
      f"Ann's value of key -> {ann_value}\n")


def dict_join(my_dict, ann_dict):
    my_dict.update(ann_dict)
    return my_dict


dict_merger = dict_join(myDictionary, annDictionary)
print("Dictionary merge: ")
for i in dict_merger.items():
    print(i)


def merge_set(my_dict, ann_dict):
    my_set = set()
    ann_set = set()
    for key in my_dict:
        for key1 in ann_dict:
            ann_set.add(key1)
        my_set.add(key)
    my_set.union(ann_set)

    return my_set


set_merger = merge_set(myDictionary, annDictionary)
print(set_merger)

# An example of a short implementation of your merge_set function
print(set(myDictionary.keys()).union(set(annDictionary)))



