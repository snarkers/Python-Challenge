import ast
import csv
import statistics

fix_type = {'Date': str, 'Profit/Losses': int}

with open("C:\\Users\\samhr\\classwork\\Homework Assignments\\Python Homework\\budget_data.csv", "r") as in_file:
    csv_reader = csv.DictReader(in_file)
    header = next(csv_reader)
    data = list(csv_reader)
    
    # of months in dataset
    # len(data)
      
    #sum of Profits/Losses
    profit_and_losses = [int(d["Profit/Losses"]) for d in data]   
  
    total_profit_and_losses = (sum(profit_and_losses))
    
    
    #Average Change in P/L 
    profit_change = []
    for i in range(1, len(data)):
        profit_change.append(profit_and_losses[i] - profit_and_losses[i-1])
        avg_profit_change = sum(profit_change)/len(profit_change)
        max_profit_change = max(profit_change)
        min_profit_change = min(profit_change)

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months : ", (len(data)))
    print("Total: " + str(total_profit_and_losses))
    print("Average Change:", (avg_profit_change))
    print("Greatest Increase in Profits:", (max_profit_change))
    print("Greatest Decrease in Profits:", (min_profit_change))
                




    
  
    
    
    