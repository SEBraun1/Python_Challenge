import csv
import os

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')
# Path to output data to text file in the Analysis folder
output_path = os.path.join('Analysis', 'Financial_Analysis.txt')

print('Budget File:',budget_csv)

#Open file
with open(budget_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    dates = []
    profits_loss = []
    for d in csvreader:
        dt, pl = d
        dates.append(dt)
        profits_loss.append(int(pl))
    print(dates)

    print("Financial Analysis")
    print('Total months:', len(dates))
    # print(profits_loss)
    print('Total Profit:', sum(profits_loss))
    print('Average Change:', sum(profits_loss)/len(profits_loss))

    profits = []
    losses = []
    for val in profits_loss:
        if val>0:
            profits.append(val)
        else:
            losses.append(val)
    # print('Profits:',profits)
    # print('Losses:',losses)

    
    max_ind = profits_loss.index(max(profits_loss))
    print('Date with maximum profit:', dates[max_ind])
    print('Maximum profit:', profits_loss[max_ind])

    min_ind = profits_loss.index(min(profits_loss))
    print('Date with maximum loss:', dates[min_ind])
    print('Maximum loss:', profits_loss[min_ind])
   
   
   # Get the report as a text file
with open(output_path, 'w') as text:   
    text.write("  Financial Analysis"+ "\n")
    text.write("--------------------------------\n")
    text.write("  Total Months: " + str(len(dates)) + "\n")
    text.write("  Total Profits: " + "$" + str(sum(profits_loss)) +"\n")
    text.write("  Average Change: " + '$' + str(sum(profits_loss)/len(profits_loss)) + "\n")
    text.write("  Greatest Increase in Profits: " + str(dates[max_ind]) + " ($" + str(profits_loss[max_ind]) + "\n")
    text.write("  Greatest Decrease in Profits: " + str(dates[min_ind]) + " ($" + str(profits_loss[min_ind]) + ")\n")
    text.close()