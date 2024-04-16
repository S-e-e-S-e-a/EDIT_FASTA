def Merge(file_in, file_out):
    # file_in: Input floder path
    # file_out: Output file path
    import os
    lines_new = []
    i = 0
    files = os.listdir(file_in)
    for file in files:
        position = path + '/' + file
        i = i + 1
        with open(position, "r", encoding='utf-8') as f_in:
            while 1:
                line = f_in.readline()
                lines_new.append(line)
                if not line:
                    break
    with open(file_out, 'w', encoding='utf-8') as f_out:
        file_out.writelines(lines_new)
        file_out.close
    a = print('%d files have been merged' % i)
    return a

def CutID(file_in, file_out, *arg):
    # file_in: Input file path
    # file_out: Output file path
    # arg[0]: An index using to pick lines or just picking all lines
    # arg[1] & arg[2]: two type:
    # str and num: cut lines from the str and keep the first half (0) or the second half(1)
    # num1 and num2: start and end location (num2 can be set as None)
    import re
    lines_new = []
    if arg[0] == None:
        with open(file_in, 'r', encoding='utf-8') as f_in:
            while 1:
                line = f_in.readline()
                if not line:
                    break
                else:
                    if type(arg[1]) == str:
                        if arg[2] == 1:
                            lines_new.append(line.split(arg[1])[int(arg[2])])
                        else:
                            lines_new.append(
                                line.split(arg[1])[int(arg[2])] + '\n')
                    else:
                        if arg[2] == None:
                            lines_new.append(line[arg[1] - 1:arg[2]])
                        else:
                            lines_new.append(line[arg[1] - 1:arg[2]] + '\n')
    else:
        matchPattern = re.compile(arg[0])
        with open(file_in, 'r', encoding='utf-8') as f_in:
            while 1:
                line = f_in.readline()
                if not line:
                    break
                elif matchPattern.search(line):
                    if type(arg[1]) == str:
                        if arg[2] == 1:
                            lines_new.append(line.split(arg[1])[int(arg[2])])
                        else:
                            lines_new.append(
                                line.split(arg[1])[int(arg[2])] + '\n')
                    else:
                        if arg[2] == None:
                            lines_new.append(line[arg[1] - 1:arg[2]])
                        else:
                            lines_new.append(line[arg[1] - 1:arg[2]] + '\n')
                else:
                    lines_new.append(line)

    with open(file_out, 'w', encoding='utf-8') as f_out:
        f_out.writelines(lines_new)
        f_out.close

def CutTail(file_in, file_out):
    # file_in: Input file path
    # file_out: Output file path
    import re
    lines_new = []
    matchPattern = re.compile('>')
    with open(file_in, 'r', encoding='utf-8') as f_in:
        while 1:
            line = f_in.readline()
            if not line:
                break
            elif matchPattern.search(line):
                lines_new.append(line)
            else:
                line_turn = line[::-1]
                aa = re.search('A', line_turn)
                tt = re.search('T', line_turn)
                cc = re.search('C', line_turn)
                gg = re.search('G', line_turn)
                if aa:
                    a = aa.start()
                if tt:
                    t = tt.start()
                if cc:
                    c = cc.start()
                if gg:
                    g = gg.start()
                numnum = min(a, t, c, g)
                lines_new.append(line[:len(line) - numnum] + '\n')

    with open(file_out, 'w', encoding='utf-8') as f_out:
        f_out.writelines(lines_new)
        f_out.close

def ATCG_replace(file_in, file_out):
    # file_in: Input file path
    # file_out: Output file path
    import re
    lines_new = []
    matchPattern = re.compile('>')
    with open(file_in, 'r', encoding='utf-8') as f_in:
        while 1:
            loc = []
            line = f_in.readline()
            if matchPattern.search(line):
                lines_new.append(line)
            else:
                for i in range(len(line)):
                    if ord(line[i]) == 65 or ord(line[i]) == 67 or ord(
                            line[i]) == 71 or ord(line[i]) == 84:
                        pass
                    else:
                        loc.append(i)
                for i in range(len(loc)):
                    line = line.replace(line[loc[i]], '-')
                if not line:
                    break
                lines_new.append(line)

    with open(file_out, 'w', encoding='utf-8') as f_out:
        f_out.writelines(lines_new)
        f_out.close

def Num_format(file_in, file_out, *arg):
    # file_in: Input file path
    # file_out: Output file path
    # arg[0]: Number length
    # arg[1]: Numeric prefix
    import re
    lines_new = []
    matchPattern = re.compile('>')
    with open(file_in, 'r', encoding='utf-8') as f_in:
        while 1:
            line = f_in.readline()
            if not line:
                break
            if matchPattern.search(line):
                if len(arg) == 1:
                    line = line.replace(line[1:-1],
                                        str(line[1:-1]).zfill(arg[0]))
                else:
                    line = line.replace(line[1:-1],
                                        arg[1] + str(line[1:-1]).zfill(arg[0]))
                lines_new.append(line)
            else:
                lines_new.append(line)
    with open(file_out, 'w', encoding='utf-8') as f_out:
        f_out.writelines(lines_new)
        f_out.close

def ID_extract(file_in, file_out):
    # file_in: Input file path
    # file_out: Output file path
    import re
    lines_new = []
    matchPattern = re.compile('>')
    with open(file_in, 'r', encoding='utf-8') as f_in:
        while 1:
            line = f_in.readline()
            if not line:
                break
            if matchPattern.search(line):
                lines_new.append(line[1:])
    with open(file_out, 'w', encoding='utf-8') as f_out:
        f_out.writelines(lines_new)
        f_out.close

def EDIT_FASTA(f_in, f_out, mode, *arg):
    # f_in: Input file path or floder path
    # f_out: Output file path
    # mode:
    # 'Merge': Merge files to one file
    # 'CutID': Cut protein IDs lenth
    # 'CutTail': Cut off the tail alignment
    # 'ATCG_replace': Replace chars that is not 'A' or 'T' or 'C' or 'G' as '-'
    # 'Num_format': Change the protein IDs number format
    # 'ID_extract': Get the protein IDs only
    if mode == 'Merge':
        Merge(f_in, f_out)
    elif mode == 'CutID':
        CutID(f_in, f_out, *arg)
    elif mode == 'CutTail':
        CutTail(f_in, f_out)
    elif mode == 'ATCG_replace':
        ATCG_replace(f_in, f_out)
    elif mode == 'Num_format':
        Num_format(f_in, f_out, *arg)
    elif mode == 'ID_extract':
        ID_extract(f_in, f_out)
    else:
        print('No mode named ' + mode)

# example
# EDIT_FASTA('input floder path', 'output file path', 'Merge')
# EDIT_FASTA('input file path', 'output file path', 'CutID', '>', '_', 0)
# EDIT_FASTA('input file path', 'output file path', 'CutTail')
# EDIT_FASTA('input file path', 'output file path', 'ATCG_replace')
# EDIT_FASTA('input file path', 'output file path', 'Num_format', 4, 'MyProtein_')
# EDIT_FASTA('input file path', 'output file path', 'ID_extract')
