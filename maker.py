import sys
import re
import csv
from collections import defaultdict, namedtuple

__author__ = 'alexander'

adress_register = namedtuple('adress_register', ['UV_adress', 'length'])


def open_csv_file(filename):
    with open(filename) as csvfile:
        variable_reader = csv.reader(csvfile)
        resulting_list = [variable[2] for variable in variable_reader]
        return resulting_list


def remove_chars_from_string(string_list):
    '''
    Filter out data
    '''
    resultin_dict = defaultdict(list)
    for variables in string_list:
        split_string = re.findall(r'([A-Z]*)([\d]*)', variables)
        resultin_dict[split_string[0][0]].append(int(split_string[0][1]))
    resultin_dict = dict(resultin_dict)
    return resultin_dict

def make_len_func(first_number, last_number, digital_data):
    '''
    calculates the length of the data, makes it dividible by 16 if digital data
    :param first_number: int
    :param last_number:int
    :param digital_data:bool
    :return len_of data: int
    '''
    if digital_data:
        first_number = make_div_by_sixteen_dec(first_number)
        len_of_data = make_div_by_sixteen(last_variable - first_number)
    elif not digital_data:
        len_of_data = last_variable - first_number
    return len_of_data

def find_intervals_in_variables(dict_with_variable):
    '''
    Make a variable list
    '''
    digital_data_types = ['CR']
    analog_data_types = ['MO', 'AI']
    for variables in dict_with_variable:
        if variables in digital_data_types:
            digital_data = True
            print('here comes a dig')
        elif variables in analog_data_types:
            digital_data = False
            print('here comes a ana')
        dict_with_variable[variables].sort()
        interval = 32
        last_variable = dict_with_variable[variables][0]
        first_number = dict_with_variable[variables][0]
        resulting_list = []
        for variable in dict_with_variable[variables]:
            if variable - last_variable > interval:
                # If interval is big enough, add it to the list
                len_of_data = make_len_func(first_number, last_variable, digital_data)
                resulting_list.append(adress_register(
                    first_number,
                    len_of_data
                    ))
                first_number = variable
            last_variable = variable
        len_of_data = make_len_func(first_number, last_variable, digital_data)
        # Add the trailing last numbers too
        resulting_list.append(adress_register(
            first_number,
            len_of_data
            ))
        dict_with_variable[variables] = resulting_list
        print(dict_with_variable)
    return dict_with_variable


def make_output_file(dict_with_variables):
    #Change this variable to change the time interval
    max_time_interval = 5

    #NOT THIS ONE!
    time_interval = 0
    value_dict = {
        'MO': ['7', '2'],
        'CR': ['3', '1']
    }
    result_list = []
    for prefix in dict_with_variables:
        for posts in dict_with_variables[prefix]:
            result_string = '''{prefix}\t{adress}\t{length}\t{type}\t{adress}\t{type}\t{adress}\t{max_interval}\t{interval}\t{max_interval}\t{interval}\t1\n'''.format(
                prefix=value_dict[prefix][0],
                adress=posts.UV_adress,
                length=posts.length,
                type=value_dict[prefix][1],
                interval=time_interval,
                max_interval=max_time_interval
            )
            result_list.append(result_string)
            if time_interval == max_time_interval:
                time_interval = 0
            time_interval += 1
        time_interval = 0
    return ''.join(result_list)


def make_div_by_sixteen(an_int):
    temp_int = 0
    while an_int > temp_int:
        temp_int += 16
    return max(temp_int, 16)

def make_div_by_sixteen_dec(an_int):
    temp_int = 0
    while an_int - 15 > temp_int:
        temp_int += 16
    return max(temp_int, 16)

def maker_main(argv):
    try:
        csv_file = argv[1]
        output_txt_file = argv[2]
    except IndexError:
        print('No CSV or output file specified')
        sys.exit()
    vars = remove_chars_from_string(open_csv_file(csv_file))
    with open(output_txt_file, 'w') as f:
        f.write(make_output_file(find_intervals_in_variables(vars)))

if __name__ == '__main__':
    # first arg CSV file, second arg output file
    main(sys.argv)

