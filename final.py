from algorithms import (arrays,string)
algorithms_file = open('./algorithms.py', 'r')
algorithms_read_file = algorithms_file.read()
algorithms_file.close()
move_zeros_file = open('./move_zeros_problem', 'r')
move_zeros_probelm = move_zeros_file.read()
move_zeros_file.close()
plus_one_file = open('./plus_one_problem', 'r')
plus_one_probelm = plus_one_file.read()
plus_one_file.close()
reverse_string_file = open('./reverse_string_probelm','r')
reverse_string_probelm = reverse_string_file.read()
reverse_string_file.close()
reverse_integer_file = open('./reverse_integer_problem','r')
reverse_integer_probelm = reverse_integer_file.read()
reverse_integer_file.close()

str_welcome = '''
Welcome to the Shaojun Leetcode Practise System
Please choose which Option you want to do:

1.Start a leetcode problem test
2.View the leetcode problem Algorithms 
3. Start a  leetcode Akgorithms test

0.Stop
'''

while True:
    print(str_welcome)
    action = input ('Please choose which Option you want to do:\n')
    if action == '1':
        print('''
        1.Array
        2.String
        ''')
        algorithms1 = input('please choose which Algorithms you want to test:\n')
        if algorithms1 == '1':
            print('''
            1.Move_Zeros
            2.Plus_One
            ''')
            problems1 = input('please choose which problem you want to test:\n')
            if problems1 == '1':
                print(move_zeros_probelm)
                arr = input('Please input an array and split by a space:')
                arr_list1 = [int(a) for a in arr.split(' ')]
                move_zeros = arrays(arr_list1)
                print(move_zeros.move_zeros())
                print('Your test was successful !')
                break
            elif problems1 == '2':
                print(plus_one_probelm)
                arr = input('Please input an array and split by a space:')
                arr_list2 = [int(a) for a in arr.split(' ')]
                plus_one = arrays(arr_list2)
                print(plus_one.plus_one())
                print('Your test was successful !')
                break
        elif algorithms1 == '2':
            print('''
                1.Reverse_String
                2.Reverse_Integer
                ''')

            problems2 = input('please choose which problem you want to test:\n')
            if problems2 == '1':   
                print(reverse_string_probelm)
                str1 = input('Please input an string and split by a space:')
                string_list1 = [a for a in str1.split(' ')]
                reverse_string = string(string_list1)
                print(reverse_string.reverseString())
                print('Your test was successful !')
                break
            elif problems2 == '2':
                print(reverse_integer_probelm)
                str2 = int(input('Please input an array and split by a space:'))
                reverse_integer = string(str2)
                print(reverse_integer.reverseInteger())
                print('Your test was successful !')
                break

    elif action == '2':
        print('''
                1.Arrary
                2.String
                ''')
        algorithms = input('please choose which Algorithms you want to view:\n')
        if algorithms == '1':
            print('''
                    1.Move_zeros
                    2.Plus_one
                    ''')
            problems = input('please choose which problem you want to view:\n')
            if problems == '1':
                print(move_zeros_probelm)
                move_zeros_start = algorithms_read_file.find('def move_zeros')
                move_zeros_end = algorithms_read_file.find('return move_zeros_result') + len('return move_zeros_result')
                print(algorithms_read_file[move_zeros_start:move_zeros_end])
                break
            elif problems == '2':
                print(plus_one_probelm)
                plus_one_start = algorithms_read_file.find('def plus_one')
                plus_one_end = algorithms_read_file.find('return res[::-1]') + len('return res[::-1]')
                print(algorithms_read_file[plus_one_start:plus_one_end])

                break

        elif algorithms == '2':
            print('''
                1.Reverse_String
                2.Reverse_Integer
                ''')
            problems = input('please choose which problem you want to test:\n')
            if problems == '1':
                print(reverse_string_probelm)
                reverse_string_start = algorithms_read_file.find('def reverseString')
                reverse_string_end = algorithms_read_file.find('return s[:]') + len('return s[:]')
                print(algorithms_read_file[reverse_string_start:reverse_string_end])

                break
            elif problems == '2':
                print(plus_one_probelm)
                plus_one_start = algorithms_read_file.find('def reverseInteger')
                plus_one_end = algorithms_read_file.find('return nums') + len('return nums')
                print(algorithms_read_file[plus_one_start:plus_one_end])

                break
    elif action == '0':
        print('The system will be stop!!!')
        break