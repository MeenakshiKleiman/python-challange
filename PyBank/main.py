import os
import csv

# create file path 
 
file_name = "Resources/budget_data.csv"
file_path = os.path.join(os.getcwd(), file_name)
print(file_path)


with open('/Users/apple/Desktop/python-challange/PyBank/Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#print(csvreader)
    first_row = next(csv_reader)
    print(first_row)



    total_months = 0
    total = 0
    profit_loss = []
    dates = []

 # Store the first row's data for calculations
    first_row = next(csv_reader)
    prev_profit_loss = int(first_row[1])
    total += prev_profit_loss
    total_months += 1

    for row in csv_reader:
        dates.append(row[0])
        total_months += 1
        profit_loss.append(int(row[1]) - prev_profit_loss)
        prev_profit_loss = int(row[1])
        total += int(row[1])

    average_change = sum(profit_loss) / len(profit_loss)  
    greatest_increase = max(profit_loss)
    greatest_decrease = min(profit_loss)
    increase_index = profit_loss.index(greatest_increase)
    decrease_index = profit_loss.index(greatest_decrease)
    
 #Print Values
print("Financial Analysis")
print("--------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {dates[increase_index]} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {dates[decrease_index]} (${greatest_decrease})")

        
# #Exporting to .txt file
with open("output.txt 1", "w") as output:
    output.write("Financial Analysis\n")
    output.write("---------------------\n")
    output.write(f"Total Months: {total_months}\n")
    output.write(f"Total: ${total}\n")
    output.write(f"Average Change: ${round(average_change, 2)}\n")
    output.write(f"Greatest Increase in Profits: {dates[increase_index]} (${greatest_increase})\n")
    output.write(f"Greatest Decrease in Profits: {dates[decrease_index]} (${greatest_decrease})\n")