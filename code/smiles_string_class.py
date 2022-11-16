#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:36:22 2022

@author: mac
"""
import re
class SmilesString:

    def __init__(self, smiles_string):
        self.smiles = smiles_string

    def validate(self):
        regex = re.compile('((Cl)|(Br)|[CNIFSBrlOPscno])+((\[C@{0,2}H\])*@{0,2}[0-9]{0,1}\({0,1}[\\\=\-\:#\/]{0,1}((Cl)|(Br)|[CNIFSBOPscno])*\){0,1}[0-9]{0,1})*')
        match = regex.match(self.smiles)
        dic = {'1' : 0, '2': 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0, '(' : 0, ')' : 0}
        for i in self.smiles:
            if i in dic:
                dic[i] += 1
        check = True
        for i in dic:
            if dic[i] % 2 != 0 and i != '(' and i != ')':
                check = False
                break
        if dic['('] != dic[')']:
            check = False
        if self.smiles[len(self.smiles)-1] in '=/\\#':
            check = False
        for i in range(len(self.smiles) - 1 ):
            if self.smiles[i] in '-/1234567890=#\\' and self.smiles[i] == self.smiles[i+1]:
                check = False
        if bool(match) and check:
            return self.smiles == match.group()
        else:
            return False


    def get_slice(self, start, end):
        return self.smiles[start:end]



    def get_molecular_formula(self):
        elements = {"B": 0,
                    "C": 0,
                    "N": 0,
                    "O": 0,
                    "P": 0,
                    "S": 0,
                    "F": 0,
                    "Cl": 0,
                    "Br": 0,
                    "I": 0}

        molecular_formula = ""

        for i in range(len(self.smiles)):
            if self.get_slice(i, i+2) in elements:
                elements[self.get_slice(i, i+2)] += 1

            else:
                if self.smiles[i].upper() in elements and self.get_slice(i, i+2) != "Br" and self.get_slice(i, i+2) != "Cl":
                    elements[self.smiles[i].upper()] += 1
        keys = list(elements.keys())
        keys.sort()
        for key in keys:
            if elements[key] != 0:
                if elements[key] == 1:
                    molecular_formula += key
                else:
                    molecular_formula += key
                    molecular_formula += str(elements[key])

        return molecular_formula