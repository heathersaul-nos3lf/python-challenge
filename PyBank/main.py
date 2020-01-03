import os
import csv
import numpy as np 

csvpath = os.path.join('/Users/hsaul/Documents/GitHub/PythonChallenge/python-challenge/PyBank/','budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    
    data=[]
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        data.append(row)
print(data[0])
array = np.array(data)

duration = len(array[:,0])
print("Total Months:"+ str(duration))
perf = array[:,1].astype(np.float)
total = np.sum(array[:,1].astype(np.float))
print("Total:"+str(total))
diff = [perf[i + 1] - perf[i] for i in range(len(perf)-1)]
print(len(diff))
aver = np.sum(diff)/len(diff)
print("Average Change:",str(aver))
gr_incr = max(diff)
gr_decr = min(diff)

ind_max = diff.index(gr_incr)
ind_min= diff.index(gr_decr)
print("Greatest Increase in Profits:",str(array[ind_max+1][0]),str(max(diff)))
print("Greatest Decrease in Profits:",str(array[ind_min+1][0]),str(min(diff)))


text_file = open("/Users/hsaul/Documents/GitHub/PythonChallenge/python-challenge/PyBank/Output.txt", "w")
text_file.write("Total Months: "+ str(duration)+ '\n')
text_file.write("Total: $"+ str(total)+ '\n')
text_file.write("Average Change: $"+ str(aver)+ '\n')
text_file.write("Greatest Increase in Profits:"+str(array[ind_max+1][0])+" "+"$"+str(max(diff))+'\n')
text_file.write("Greatest Decrease in Profits:"+str(array[ind_min+1][0])+" "+"$"+str(min(diff))+'\n')
text_file.close()


