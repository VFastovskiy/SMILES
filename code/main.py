#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:35:42 2022

@author: mac
"""

import funcs as f
import constants as c
from smiles_string_class import SmilesString
from smiles_strings_list_class import SmilesStringsList



def main():

    answer = f.read_command(c.LOAD_SOURCE)
    while answer.upper() != c.YES and answer.upper() != c.NO:
        print(c.INVALID_ANSWER)
        answer = f.read_command(c.LOAD_SOURCE)

    if answer.upper() == c.YES:
        file_name = input(c.PROMPT)
        #print(file_name)
        if f.open_file(file_name):
            smiles_items = f.read_from_file(file_name, 0)
            smiles_list = f.validate_smiles(smiles_items)
            if smiles_list.smiles_list == []:
                print(c.LIST_IS_EMPTY)
            else:
                for smiles in smiles_list.get_smiles_list():
                    print(smiles)
        else:
            print(c.FAILED_READING + str(file_name))
            smiles_list = SmilesStringsList([])

    if answer.upper() == c.NO:
        smiles_list = SmilesStringsList([])


    f.print_help_message()

    command = f.read_command(c.PROMPT)

    while command.upper() != c.QUIT:


        if command.upper() == c.COUNT_SUBSTRINGS:
            answer = f.read_command(c.INPUT_SOURCE)
            while answer.upper() != c.FILE and answer.upper() != c.TERMINAL:
                print(c.INVALID_INPUT)
                answer = f.read_command(c.INPUT_SOURCE)

            if answer.upper() == c.FILE:
                file_name = f.read_command(c.PROMPT)
                if f.open_file(file_name):
                    substrings_list = f.read_from_file(file_name, 0)
                    if substrings_list == []:
                        print(c.LIST_IS_EMPTY)
                    else:
                        smiles_list.cout_substrings(substring_list)
                else:
                    print(c.FAILED_READING + str(file_name))

            if answer.upper() == c.TERMINAL:
                num_of_strings = input()
                substring_list = f.read_from_terminal(num_of_strings)
                smiles_list.count_substrings(substring_list) #Error


        elif command.upper() == c.MOLECULAR_FORMULA:
            if smiles_list.smiles_list == []:
                print(c.LIST_IS_EMPTY)
            else:
                f.obtain_molecular_formula(smiles_list)


        elif command.upper() == c.DISSIMILARITY:
            if smiles_list.smiles_list == [] or len(smiles_list.smiles_list) == 1:
                print(c.LIST_EMPTY_OR_SINGULAR)
            elif len(smiles_list.smiles_list) > 1:
                number_of_substrings = int(f.read_command(c.NUMBER_OF_SUBSTRINGS))
                while int(number_of_substrings) <= 0:
                    number_of_substrings = f.read_command(c.NUMBER_OF_SUBSTRINGS)

                substring_list = f.read_from_terminal(number_of_substrings)
                print(c.COMPARE_STRINGS)
                str1 = input()
                str2 = input()
                while str1 not in smiles_list.get_smiles_list():
                    print('SMILES ' + str1 + ' unknown; input a valid one:')
                    str1 = input()
                while str2 not in smiles_list.get_smiles_list():
                    print('SMILES ' + str2 + ' unknown; input a valid one:')
                    str2 = input()
                dissimilarity = f.count_dissimilarity(str1, str2, substring_list)
                res = 'Dissimilarity degree between SMILES ' + str1 + ' and ' + str2 +' w.r.t.'
                substring_list.sort()
                for i in range(len(substring_list)):
                    if i == len(substring_list) - 1:
                        res += ' ' + substring_list[i]
                    else:
                        res += ' ' + substring_list[i] +' and'
                res += ': ' + str(dissimilarity)
                print(res)

        elif command.upper() == c.INPUT:
            f.input_new_smiles(smiles_list)


        elif command.upper() == c.HELP:
            f.print_help_message()

        else:
            print(c.INVALID_COMMAND)

        command = f.read_command(c.PROMPT)

    if command.upper() == c.QUIT:
        answer = f.read_command(c.SAVE_SMILES)
        while answer.upper() != c.YES and answer.upper() != c.NO:
            print(c.INVALID_ANSWER)
            answer = f.read_command(c.SAVE_SMILES)

        if answer.upper() == c.YES:
            f.write_to_file(smiles_list)

        print(c.GOODBYE)

main()