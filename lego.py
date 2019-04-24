###
### Author: Firedorange717
### Description: A program that takes 4 user inputs, a LEGO set file name, a type of input {sets or pieces}
###                 type of search {subset, superset, none} and the id numbers. it them depending on the
###                     inputs performs the desired search with the correct type of input and gives out the
###                         names of the sets that satisfy that search.
###

def print_results(results):
    '''
    Print the results in sorted order.
        Students should use this function to print out the search results.
            results: A set of pairs of elements to print in sorted order.
                The pairs of elements will be tuples/lists of set name, then set ID.
    '''
    print()
    results = list(results)
    results.sort()
    for e in results:
        print(e[1] + ' : ' + e[0])

def read_file(file_name):
    '''
    Gets the user specified file and opens it, then it splits and strips the
        data at the ||| and then the , . It than adds all the values to a dictionary
            as tuples for keys and sets for values.
    file_name = Type {String}
    '''
    file = open(file_name,'r')
    lego_sets = {}

    # Runs for each line in the user file
    for line in file:

        # Seperastes potential keys from values
        line = line.split('|||')

        # Makes tuple key with name first then set number
        key = line[0].split(',')
        key_tuple = (key[0].strip(' '), key[1].strip(' '))

        #Seperates values by ,
        value_list = line[1].split(',')
        value_set = set([])

        # Strips \n and spaces then sets that set to the
        #     value for the dictionary key.
        for value in value_list:
            value = value.strip('\n')
            value = value.strip(' ')
            value_set.add(value)
        lego_sets[key_tuple] = value_set

    return lego_sets

def subset_search(lego_sets, search_ids,input_type):
    '''
    Gets the set dictionary, ids to be searched and type, then
        depending on type checks if the values given are a subset of
            any sets. If so it adds the name of the set.
    lego_sets = Type {Dictionary}
    search_ids = Type {List}
    input_type = Type {String}
    '''
    output = []
    sets_values = set()

    if input_type == 'sets':
        # Gets values from user and adds the
        #   coresponding dictionary values to a set
        #     if theres a match.
        for set_key in search_ids:
            for key,value in lego_sets.items():
                if set_key in key:
                    sets_values.update(value)

        # Checks for subsetsbetween dictionary values
        #   and the values from all sets.
        for key,value in lego_sets.items():
            if value.issubset(sets_values):
                output.append(key)

    elif input_type == 'pieces':
        # Checks for subsets between user data
        #   and dictionary values
        search_ids = set(search_ids)
        for key,value in lego_sets.items():
            if value.issubset(search_ids):
                output.append(key)
    else:
        print('Invalid search')

    print_results(output)

def superset_search(lego_sets, search_ids,input_type):
    '''
    Gets the set dictionary, ids to be searched and type, then
        depending on type checks if any set values are a superset of
            the data given. If so it adds the name of the set.
    lego_sets = Type {Dictionary}
    search_ids = Type {List}
    input_type = Type {String}
    '''
    output = []
    sets_values = set()

    if input_type == 'sets':
        # Gets values from user and adds the
        #   coresponding dictionary values to a set
        #     if theres a match.
        for set_key in search_ids:
            for key,value in lego_sets.items():
                if set_key in key:
                    sets_values.update(value)

        # Checks for supersets between dictionary values
        #   and the values from all sets.
        for key,value in lego_sets.items():
            if value.issuperset(sets_values):
                output.append(key)

    elif input_type == 'pieces':
        # Checks for supersets between user data
        #   and dictionary values
        search_ids = set(search_ids)
        for key,value in lego_sets.items():
            if value.issuperset(search_ids):
                output.append(key)

    else:
        print('Invalid search')

    print_results(output)

def none_search(lego_sets, search_ids,input_type):
    '''
    Gets the set dictionary, ids to be searched and type, then
        depending on type checks if the values given are in any sets
            if not it adds the name of the set.
    lego_sets = Type {Dictionary}
    search_ids = Type {List}
    input_type = Type {String}
    '''
    output = []
    sets_values = set()

    if input_type == 'sets':
        # Gets values from user and adds the
        #   coresponding dictionary values to a set
        #     if theres a match.
        for set_key in search_ids:
            for key,value in lego_sets.items():
                if set_key in key:
                    sets_values.update(value)

        # Checks for intersections between dictionary values
        #   and the values from all sets.
        for key, value in lego_sets.items():
            check = value.intersection(sets_values)
            if check == set():
                output.append(key)

    elif input_type == 'pieces':
        # Checks for intersections between user data
        #   and dictionary values
        search_ids = set(search_ids)
        for key, value in lego_sets.items():
            check = search_ids.intersection(value)
            if check == set():
                output.append(key)

    print_results(output)

def search_selector(lego_sets,search_ids,input_type,search_type):
    '''
    Gets the set dictionary, ids to be searched, type and search type then
        selects the correct function and passes through all the data.
            Also seperates user search values.
    lego_sets = Type {Dictionary}
    search_ids = Type {List}
    input_type = Type {String}
    search_type = Type {String}
    '''

    # Seperates user values on space
    search_ids = search_ids.split(' ')
    search_id_list = []

    # Adds user values to a list
    for number in search_ids:
        search_id_list.append(number)

    # Picks correct function
    if search_type == 'subset':
        subset_search(lego_sets,search_id_list,input_type)
    elif search_type == 'superset':
        superset_search(lego_sets,search_id_list,input_type)
    else:
        none_search(lego_sets,search_id_list,input_type)

def main():
    file_name = input('LEGO set file name:\n')
    input_type = input('Search by sets or pieces?:\n')
    search_type = input('Search type (subset or superset or none):\n')
    search_ids = input('Search IDs:\n')
    lego_sets = read_file(file_name)
    search_selector(lego_sets,search_ids,input_type,search_type)

main()