def create_dict_from_lists(first_list, second_list ):
    """Returns a dictionary.
       takes two lists and converts them into a dictionary."""

    dictionary = {}
    for i in range(len(first_list)):
        dictionary[first_list[i]] = second_list[i]
    return dictionary

def main():
    items = ['Milk', 'Eggs', 'Bread', 'Pasta']
    costs = [5, 4.99, 2.79, 2.99]
    print(create_dict_from_lists(items,costs))

main()
