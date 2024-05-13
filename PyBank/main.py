# import csv
import csv

# get path
csvpath = "Resources/budget_data.csv"

# read 
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # store the header row
    csv_header = next(csvreader)
    # define new dictionary
    profit_data = {}
    # loop throught the csv to make the dictionary of months and profit/losses
    for row in csvreader:
        date = row[0]
        profit = int(row[1])

        profit_data[date] = profit
    # get total months from length of dictionary 
    total_months = len(profit_data)
    
    # sum of values to get total profit
    total_profit = (sum(profit_data.values()))

    # make empty lists
    months = []
    profit_loss = []
    list_of_change = []
    # now split the dictionary into the lists for some list comprehension
    for key in profit_data:
        months.append(key)
    for values in profit_data.values():
        profit_loss.append(values)
    # find the change in profits from month to month and enter into new list
    list_of_change = [profit_loss[i] - profit_loss[i - 1] for i in range(1, len(profit_loss))]

    # find the max and min of the changes in profit and losses
    max_change = max(list_of_change)
    min_change = min(list_of_change)
    max_index = list_of_change.index(max_change)
    min_index = list_of_change.index(min_change)
    max_month = months[max_index + 1]
    min_month = months[min_index + 1]
    
    average_change = (sum(list_of_change)/len(list_of_change))

    # print the data findings to the terminal
    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {max_month} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

    # output the data
    output = (
        "Financial Analysis\n\n"
        "--------------------------\n\n"
        f"Total Months: {total_months}\n\n"
        f"Total: ${total_profit}\n\n"
        f"Average Change: ${average_change:.2f}\n\n"
        f"Greatest Increase in Profits: {max_month} (${max_change})\n\n"
        f"Greatest Decrease in Profits: {min_month} (${min_change})"
    )

    #print output to the Anaylsis folder
    with open("Analysis/pyBank_text.txt", "w") as f:
        f.write(output)