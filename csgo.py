with open('raw.txt', 'r') as file, open('autoexec.cfg', 'w') as output:
    output.write('alias "output" "line1"\n')
    data = file.readlines()
    for row in range(len(data)):
        if (row == len(data) - 1):
            output.write('alias "line%d" "say %s; alias output line 1"\n' %(row + 2, data[row].strip()))
        else:
            output.write('alias "line%d" "say %s; alias output line%d"\n' %(row + 2, data[row].strip(), row + 3))
    output.write('bind "." "output"\n')
    



