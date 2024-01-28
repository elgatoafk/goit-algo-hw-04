def get_cats_info(path: str) -> list[dict]:
    """get_cats_info Function reads the file with cat information and return it in list of dictionaries.

    :param path: path to the file with cat information
    :type path: str
    :return: list of dictionaries, each dictionary contins information for one cat
    :rtype: list[dict]
    """    
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as cats_info:
            while line := cats_info.readline():
                line = line.split(',')
                lines_dict = {"cat_id":line[0], "cat_name":line[1], "cat_age":line[2].replace("\n", "")}
                cats_list.append(lines_dict)           
    except FileNotFoundError:
        print("File not found, please check filepath")
    return cats_list

