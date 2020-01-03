import os
import csv
import numpy as np 

csvpath = os.path.join('/Users/hsaul/Documents/GitHub/PythonChallenge/python-challenge/PyPoll/','election_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    
    data=[]
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

     # Read each row of data after the header
    for row in csvreader:
        #print(row)
        data.append(row)        
array = np.array(data)

#The total number of votes cast
total = len(array[:,0])
print("Total Votes Cast:"+ str(total))

#A complete list of candidates who received votes
names = np.unique(array[:,2])
print(names)

#The total number of votes each candidate won
from collections import Counter
num_votes= Counter(array[:,2])
print(num_votes)


#The percentage of votes each candidate won

#obtain the names from the num_votes dictionary
key=list(num_votes.keys())
#obtain the numerical values from the num_votes dictionary
value=list(num_votes.values())
#printkey
print(key)
#calculate the percentages of each vote
newList = [round(100*x / total,4) for x in value]
print(newList)

#The winner of the election based on popular vote.

#find the maximum in the percentage list
max_indx = newList.index(max(newList))

#print whos the winner
print("The winner of the election is "+str(key[max_indx]))
#create a text file 
text_file = open("/Users/hsaul/Documents/GitHub/PythonChallenge/python-challenge/PyPoll/Output.txt", "w")
text_file.write("Election Results" + '\n')
text_file.write('-'*20  +'\n')
text_file.write("Total number of votes cast: "+ str(total)+ '\n')
text_file.write('-'*20  +'\n')
for y in range(4) :
    text_file.write(str(key[y])+" : " + str(newList[y])+ "%"+ " ("+str(value[y])+")"'\n' )
text_file.write('-'*20  +'\n')
text_file.write("The Winner of the Election is: " + str(key[max_indx]))

text_file.close()


