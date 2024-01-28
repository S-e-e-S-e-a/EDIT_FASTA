# "EDIT_FASTA" 

The .py and .ipynb files are offered, which providing the following five functions:

## 'Merge'

Merge files(.txt, .fasta, or other text files) in the same folder into the same new file.

example:
  EDIT_FASTA('input floder path', 'output file path', 'Merge')
  
## 'CutID'

Cut protein IDs lenth, e.g. selecting the line with '>' and keeping only the part of the ID before '_'.

example:
  EDIT_FASTA('input file path', 'output file path', 'CutID', '>', '_', 0) # 0 means the first half; 1 means the second half.
  
## 'CutTail'

Cut off the tail alignment. After processing, the file will end with either A, T, C or G.

example:
  EDIT_FASTA('input file path', 'output file path', 'CutTail')
  
## 'ATCG_replace'

Replace chars that is not 'A' or 'T' or 'C' or 'G' as '-'.

example:
  EDIT_FASTA('input file path', 'output file path', 'ATCG_replace')
  
## 'Num_format'

Change the protein IDs number format and can also be prefixed with ID. By default, lines with '>' are selected.

example:
  EDIT_FASTA('input file path', 'output file path', 'Num_format', 4, 'MyProtein_') # 4 means number length = 4, e.g. 1 --> 0001, 11 --> 0011.

# !!! My major is neither biology nor computers, so there may be errors in the code. I hope you will correct me.
