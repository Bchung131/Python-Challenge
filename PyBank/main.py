#Importing the OS and CSV modules.
import os
import csv

#Creates the file path.
csvpath = os.path.join('Resources','budget_data.csv')

#Makes the CSV readable and prints the CSV Header.
with open(csvpath) as finanical_data:
    csvreader = csv.reader(finanical_data, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Creating the variables.
    profit_loss_rev = []
    month_counter = []
    profit_loss_diff = []
    
    
    for row in csvreader:
        month_counter.append(row[0])
        profit_loss_rev.append(int(row[1]))

#Counts the entire sum of months.
total_months = len(month_counter)

#Calculates the net total profit/loss for entire period.
net_total = sum(profit_loss_rev)

#Creates calculations for the profit/loss changes.
for x in range(1, total_months):
    profit_loss_change = profit_loss_rev[x] - profit_loss_rev[x-1]
    profit_loss_diff.append(profit_loss_change)

#Calcuation for the average of the changes in profit/loss over entire period.
average_change = sum(profit_loss_diff) / len(profit_loss_diff)

#Calculates the greatest increase in profits and date over the entire period.
greatest_increase = max(profit_loss_diff)
greatest_increase_date = month_counter[profit_loss_diff.index(greatest_increase) + 1]

#Calculates the greatest decrease in profits and date over the entire period.
greatest_decrease = min(profit_loss_diff)
greatest_decrease_date = month_counter[profit_loss_diff.index(greatest_decrease) + 1]

#Prints out the financial analysis results
print("Financial Analysis")
print("--------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

#Creates an outpath to a text file
csv_output_path = os.path.join("analysis", "Financial Analysis")
  
with open(csv_output_path, 'w') as csvfile:

     csvwriter = csv.writer(csvfile,)

  #Writes analysis results to a text file

     csvwriter.writerow(["Financial Analysis"])
     csvwriter.writerow(["--------------------------------------"])
     csvwriter.writerow([(f"Total Months: {total_months}")])
     csvwriter.writerow([(f"Total: ${net_total}")])
     csvwriter.writerow([f"Average Change: ${average_change:.2f}"])
     csvwriter.writerow([(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")])
     csvwriter.writerow([(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")])   