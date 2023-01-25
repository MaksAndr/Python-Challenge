
import os, csv
from pathlib import Path 

csv_file_path = Path("Desktop/Python-Challenge/PyPoll/Resources/election_data.csv")

total_votes = 0
stocham_votes = 0
degette_votes = 0
doane_votes = 0

with open(csv_file_path,newline="", encoding="utf-8") as elections:

    csvreader = csv.reader(elections,delimiter=",") 

    header = next(csvreader)     

    for row in csvreader: 

        total_votes +=1

  
        if row[2] == "Charles Casper Stockham": 
         stocham_votes +=1
        
        
        elif row[2] == "Diana DeGette":
          degette_votes +=1
             
             
        elif row[2] == "Raymon Anthony Doane": 
         doane_votes +=1
        
 
candidates = ["Stocham", "DeGette", "Doane"]
votes = [stocham_votes, degette_votes,doane_votes,]

 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

stocham_percent =(stocham_votes/total_votes) *100
degette_percent = (degette_votes/total_votes) * 100
doane_percent = (doane_votes/total_votes)* 100

print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {stocham_percent:.3f}% {stocham_votes})")
print(f"Diana DeGette: {degette_percent:.3f}% ({degette_votes})")
print(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

output_file = Path("Desktop/Python-Challenge/PyPoll/Analysis/Election_Results.txt")

with open(output_file,"w") as file:

    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {stocham_percent:.3f}% {stocham_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {degette_percent:.3f}% ({degette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")



