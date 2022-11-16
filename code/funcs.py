from smiles_string_class import SmilesString
from smiles_strings_list_class import SmilesStringsList
import smiles_strings_list_class as s
import constants as c
import re


def print_help_message():
    mes = ['C: count the number of times each sub-string from an external list (given file) occurs in the SMILES strings of the list.',
            'M: Count the number of times each atomic element occurs in the strings in the list and obtain the molecular formula (number of atoms of each element, e.g., C8NO2). The output of the command should appear in the terminal and be in lexicographic order.',
            'D: compare a given pair of molecules from their SMILES representation (calculate their dissimilarity, i.e., sum of squared differences between the number of occurrences of the sub-strings in two SMILES).',
            "I: input a new SMILES string to be added to the current list, if valid (if not, the application reports it found a problem and waits for the user's to input a new command).",
            'H: help - list all commands.',
            'Q: quit - quit the application.']

    for str in mes:
        print(str)


def read_command(text):
    command = input(text)
    return command


def validate_smiles(smiles_list):
    validated_smiles = []
    smiles_list.sort()
    for i in smiles_list:
        smiles = SmilesString(i)
        if smiles.validate():
            validated_smiles.append(smiles)
    if validated_smiles == []:
        smiles_list_class = SmilesStringsList([])
    else:
        smiles_list_class = SmilesStringsList(validated_smiles)
    return smiles_list_class


def open_file(file_name):
    try:
        file_handle = open(file_name, 'r')
        file_handle.close()
        return True
    except:
        return False


def read_from_file(file_name, string_from):
    file_handle = open(str(file_name), 'r')
    all_strings_list = file_handle.readlines()[string_from:] # read from 2nd line
    for i in range(len(all_strings_list)):
        all_strings_list[i] = all_strings_list[i].replace('\n','')
    file_handle.close()
    return all_strings_list


def read_from_terminal(num_of_strings):
    substrings_list = []
    for i in range(int(num_of_strings)):
        smiles = input()
        substrings_list.append(smiles)

    return substrings_list


def write_to_file(smiles_list):
    file_name = read_command(c.PROMPT)
    f = open(str(file_name), 'w')
    for i in smiles_list.get_smiles_list():
        f.write(i.smiles + '\n')
    f.close()


def input_new_smiles(smiles_list):
    string = input()
    string = string.upper()
    regex = re.compile('(BR)')
    string = regex.sub('Br', string)
    regex = re.compile('(CL)')
    string = regex.sub('Cl',string)
    smiles_string = SmilesString(string)
    l = smiles_list.get_list()
    if smiles_string.validate():
        if string not in l:
            smiles_list.add_smiles_string(smiles_string)
            res = 'SMILES list updated: ' + string + ' inserted'
            print(res)
        else:
            res = 'SMILES ' + string + ' already loaded'
            print(res)
    else:
        print('String ' + string + ' is not a valid SMILES')


def obtain_molecular_formula(smiles_list):
    for smiles in smiles_list.smiles_list:
        molecular_formula = smiles.get_molecular_formula()
        result = smiles.smiles + " " + "is" + " " + molecular_formula
        print(result)


def count_occurances(string, substring):
    counter = 0
    occurances = 0
    while counter < len(string):
        if string[counter: counter + len(substring)] == substring:
            occurances += 1
            counter += len(substring)
        else: counter += 1
    return occurances



def count_dissimilarity(str1,str2,substring_list):
        branches1 = s.separate_branches(str1)
        branches2 = s.separate_branches(str2)
        dissimilarity = 0
        for i in substring_list:
            occurences1 = 0
            occurences2 = 0
            for k in branches1:
                occurences1 += count_occurances(k, i)
            for k in branches2:
                occurences2 += count_occurances(k,i)
            dissimilarity += (occurences1 - occurences2)**2
        return dissimilarity


def count_dissimilarity_io():
    structure1 = input()
    structure2= input()
    number_of_substrings = int(input('enter number of substrings'))
    substring_list = []
    for i in range(number_of_substrings):
        substring = input()
        substring_list.append(substring)
    dissimilarity = count_dissimilarity(structure1, structure2, substring_list)
    print('dissimilarity =  ', dissimilarity)
