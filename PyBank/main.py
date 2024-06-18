
import csv
import os

budget_data_csv = os.path.join("C:/Users/admin/Desktop/Python-challenge/PyBank/Resources/budget_data.csv")

with open(budget_data_csv, 'r') as file:
    data_budget = csv.reader(file)
    next(data_budget)  

    # Set up of 3 empties list to save the result
    count_month = []
    profit = []
    blocks = []
   
    for row in data_budget:
        count_month.append(row[0])
        profit.append(int(row[1]))
        
#The total number of months included in the dataset
total_count = len(count_month)

# The net total amount of "Profit/Losses" over the entire period
net_profit = sum(profit)


for item in range(1, total_count):
    periode = profit[item] - profit[item-1]
    blocks.append(periode)

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
average_periode = sum(blocks) / len(blocks)

# The greatest increase in profits (date and amount) over the entire period
increase = max(blocks)
increase_date = count_month[blocks.index(increase) + 1]

#The greatest decrease in profits (date and amount) over the entire period
decrease = min(blocks)
decrease_date = count_month[blocks.index(decrease) + 1]


result = "C:/Users/admin/Desktop/Python-challenge/PyBank/Analysis/budget_result.txt"

with open(result, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write(f"Total Months: {total_count}\n")
    file.write(f"Total: ${net_profit}\n")
    file.write(f"Average Change: ${round(average_periode,2)}\n")
    file.write(f"Greatest Increase in Profits: {increase_date} (${increase})\n")
    file.write(f"Greatest Decrease in Profits: {decrease_date} (${decrease})\n")