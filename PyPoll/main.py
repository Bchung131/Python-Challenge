#Importing the OS and CSV modules.
import os
import csv

#creates the file path.
csvpath = os.path.join('Resources','election_data.csv')

#Makes the CSV readable and prints out the CSV header.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header =next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Creating variables.
    CCS_votes = 0
    DG_votes = 0
    RAD_votes = 0
    total_votes = 0

    
    for row in csvreader: 
      
      #Counts the total votes.
      total_votes += 1
    
      #Loops through the candidate index and counts the total votes for that candidate.
      if row[2] == "Charles Casper Stockham":
        CCS_votes += 1
      elif row[2] == "Diana DeGette":
        DG_votes += 1
      elif row[2] == "Raymon Anthony Doane":
        RAD_votes += 1
    
   #Testing my variables and values
    print(CCS_votes)
    print(DG_votes)
    print(RAD_votes)
    CCS_vote_percentage = ((CCS_votes/total_votes)*100)
    DG_vote_percentage = ((DG_votes/total_votes)*100)
    RAD_vote_percentage = ((RAD_votes/total_votes)*100)

    print(f"{CCS_vote_percentage:.3f}")
    print(f"{DG_vote_percentage:.3f}")
    print(f"{RAD_vote_percentage:.3f}")

#Prints out the voting results.
print("Election Results")
print("--------------------------")
print(f'Total Votes : {total_votes}')
print("--------------------------")
print()
print("--------------------------")
   