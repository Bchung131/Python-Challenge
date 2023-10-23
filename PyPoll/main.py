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
    winner = []

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
    
    #Calcuating the voting percentage for each candidate.
    CCS_vote_percentage = ((CCS_votes/total_votes)*100)
    DG_vote_percentage = ((DG_votes/total_votes)*100)
    RAD_vote_percentage = ((RAD_votes/total_votes)*100)

    total_results = [CCS_votes, DG_votes, RAD_votes]

    #Prints out the winner.
    if CCS_votes == max(total_results):
      winner = "Charles Casper Stockham"
    elif DG_votes == max(total_results):
      winner = "Diana DeGette"
    elif RAD_votes == max(total_results):
      winner = "Raymon Anthony Doane"

#Prints out the voting results.
print("Election Results")
print("--------------------------")
print(f'Total Votes: {total_votes}')
print("--------------------------")
print(f'Charles Casper Stockham: {f"{CCS_vote_percentage:.3f}"}% ({CCS_votes})')
print(f'Diana DeGette: {f"{DG_vote_percentage:.3f}"}% ({DG_votes})')
print(f'Raymon Anthony Doane: {f"{RAD_vote_percentage:.3f}"}% ({RAD_votes})')
print("--------------------------")
print(f'Winner: {winner}')
print("--------------------------")

#Creates an outpath to a text file.
csv_output_path = os.path.join("analysis", "Election Results")
  
with open(csv_output_path, 'w') as csvfile:

    csvwriter = csv.writer(csvfile,)

  #Writes election results to a text file.

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["--------------------------"])
    csvwriter.writerow([f'Total Votes: {total_votes}'])
    csvwriter.writerow(["--------------------------"])
    csvwriter.writerow([f'Charles Casper Stockham: {f"{CCS_vote_percentage:.3f}"}% ({CCS_votes})'])
    csvwriter.writerow([f'Diana DeGette: {f"{DG_vote_percentage:.3f}"}% ({DG_votes})'])
    csvwriter.writerow([f'Raymon Anthony Doane: {f"{RAD_vote_percentage:.3f}"}% ({RAD_votes})'])
    csvwriter.writerow(["--------------------------"])
    csvwriter.writerow([f'Winner: {winner}'])
    csvwriter.writerow(["--------------------------"])