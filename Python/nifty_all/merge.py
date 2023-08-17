import pandas as pd
import csv
import numpy as np

input_files = ['nifty.csv' , 'bankNifty.csv', 'finNifty.csv']
output_file = 'merged.csv'

output = None
j = 0
for infile in input_files:
    with open(infile, 'r') as fh:
        if output:
            for i,l in enumerate(fh.readlines()):
                if j == 0:
                    j = j + 1
                    output[i] = 'Index'
                    # print("if", output[i])
                    # j = j+1
                    # output[i] = "{}".format(output[i])
                    # print("if", output[i])
                else:
                    output[i] = "{}{}".format(output[i],l)

        else:
            output = fh.readlines()

with open(output_file, 'w') as fh:
    for line in output:
        fh.write(line)







# import csv
# import pandas as pd
# files = ['nifty.csv' , 'bankNifty.csv']

# # with open('nifty.csv', mode='r') as file:
# #     csvFile = csv.reader(file)
# #     for lines in csvFile:
# #         print(lines)

# # with open('nifty.csv') as f1, open('bankNifty.csv') as f2:
# #     print(f1.flush)

# newDf = pd.concat(
#     map(pd.read_csv, ['nifty.csv' , 'bankNifty.csv']), ignore_index = True)
# print(newDf)
# newDf.to_csv('merged.csv', index=False)
