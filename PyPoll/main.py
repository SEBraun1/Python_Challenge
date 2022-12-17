import csv
import os

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')
# Path to output data to text file in the Analysis folder
output_path = os.path.join('Analysis', 'Election_Analysis.txt')

print('Election File:',election_csv)

from collections import Counter

#Open file
with open(election_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    votes = []
    candidates = []
  
    for d in csvreader:
        vt, co, cd = d
        votes.append(vt)
        candidates.append(str(cd))
    
    counter = dict(Counter(candidates))
    print('Candidates:', counter)

    print("Election Analysis")
    print('Total votes:', len(votes))

    print("DeGette won: " + str(counter['Diana DeGette']) + ' | ' + str(counter['Diana DeGette']/len(votes)*100) + "%" )
    print("Stockham won: " + str(counter['Charles Casper Stockham'])  + ' | ' +  str(counter['Charles Casper Stockham']/len(votes)*100) + "%" )
    print("Doane won: " + str(counter['Raymon Anthony Doane'])  + ' | ' +  str(counter['Raymon Anthony Doane']/len(votes)*100) + "%" )
    print("DeGette wins.")

    # Get the report as a text file
with open(output_path, 'w') as text:   
    text.write("  Election Analysis"+ "\n")
    text.write("--------------------------------\n")
    text.write("Total votes: " + str(len(votes)) + "\n")
    text.write("Candidates: " + str(counter.keys()) +"\n")
    text.write("DeGette won: " + str(counter['Diana DeGette']) + ' | ' + str(counter['Diana DeGette']/len(votes)*100) + "%" + "\n")
    text.write("Stockham won: " + str(counter['Charles Casper Stockham'])  + ' | ' +  str(counter['Charles Casper Stockham']/len(votes)*100) + "%" + "\n")
    text.write("Doane won: " + str(counter['Raymon Anthony Doane'])  + ' | ' +  str(counter['Raymon Anthony Doane']/len(votes)*100) + "%" + ")\n")
    text.write("DeGette wins.")
    text.close()

    