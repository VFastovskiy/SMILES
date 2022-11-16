# PAB-porject-SMILES


* **C:** count the number of times each sub-string from an external list (given file) occurs in the SMILES strings of the list.
* **M:** Count the number of times each atomic element occurs in the strings in the list and obtain the molecular formula (number of atoms of each element, e.g., C8NO2). The output of the command should appear in the terminal and be in lexicographic order.
* **D:** compare a given pair of molecules from their SMILES representation (calculate their dissim- ilarity, i.e., sum of squared differences between the number of occurrences of the sub-strings in two SMILES).
* **S:** select all SMILES strings in the list containing a given (set of) sub-structure(s). The set may be given by the user or read from a file (one substructure per line). The output of the command should appear in the terminal and be in lexicographic order.
* **I:** input a new SMILES string to be added to the current list, if valid (if not, the application reports it found a problem and waits for the user’s to input a new command).
* **H:** help – list all commands.
* **Q:** quit – quit the application.
