'''
How to use: create a file named 'raw.txt' containing the lines of text you want
to be bound. This file should be in the same directory as the .py file. Run the script,
and the autoexec.cfg file should be created in the same directory.
'''

with open('raw.txt', 'r') as file, open('autoexec.cfg', 'w') as output:
    output.write('alias "output" "line1"\n')
    data = file.readlines()
    for row in range(len(data)):
        if (row == len(data) - 1):
            output.write('alias "line%d" "say %s; alias output line 1"\n' %(row + 1, data[row].strip()))
        else:
            output.write('alias "line%d" "say %s; alias output line%d"\n' %(row + 1, data[row].strip(), row + 2))
    output.write('bind "." "output"\n')
    



