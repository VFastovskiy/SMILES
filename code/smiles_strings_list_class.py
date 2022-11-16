#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:36:22 2022

@author: mac
"""
import re

from smiles_string_class import SmilesString

def clear_sequence(sequence):
    regex = re.compile('[\/\\@0-9!()]')
    return regex.sub('',sequence)


def separate_branches(smiles_string):
    branches_final = []
    main_sequence = smiles_string
    regex = re.compile('[(][CNOBPFISrlcnos=\/\\@#0-9!]+[)]')
    while '(' in main_sequence or ')' in main_sequence:
        branches_found = regex.findall(main_sequence)
        for i in branches_found:
            branches_final.append(clear_sequence(i))
        main_sequence = regex.sub('',main_sequence)
    branches_final.append(clear_sequence(main_sequence))
    return branches_final

def count_occurances(string, substring):
    counter = 0
    occurances = 0
    while counter < len(string):
        if string[counter: counter + len(substring)] == substring:
            occurances += 1
            counter += len(substring)
        else: counter += 1
    return occurances


class SmilesStringsList:

    def __init__(self, smiles_strings_list):
        self.smiles_list = smiles_strings_list


    def add_smiles_string(self, smiles_string):
        self.smiles_list.append(smiles_string)

    def get_smiles_string(self, elem):
        return self.smiles_list[elem]

    def get_list(self):
        res = []
        for i in self.smiles_list:
            res.append(i.smiles)
        return res

    def count_substrings(self,substring_list):
        res_final = []
        for i in self.smiles_list:
            res = i.smiles + ' contains '
            branches = separate_branches(i.smiles)
            for j in range(len(substring_list)):
                occurences = 0
                for k in branches:
                    occurences += count_occurances(k,substring_list[j])
                if j == 0:
                    if occurences == 1:
                        res +=  substring_list[j] + ' ' + str(occurences) + ' time'
                    else:
                        res +=  substring_list[j] + ' ' + str(occurences) + ' times'
                else:
                    if occurences == 1:
                        res +=  ' and ' + substring_list[j] + ' ' + str(occurences) + ' time'
                    else:
                        res +=  ' and ' + substring_list[j] + ' ' + str(occurences) + ' times'
            res_final.append(res)
        res_final.sort()
        for i in res_final:
            print(i)

    def add_smiles_string(self, smiles_string):
        self.smiles_list.append(smiles_string)

    def get_smiles_list(self):
        res = []
        for i in self.smiles_list:
            res.append(i.smiles)
        return res

