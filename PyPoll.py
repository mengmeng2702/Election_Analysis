#add the dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save a file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

#add vote counter and initialize it to zero to start with
total_votes = 0

#initialize a new list with all candidates in it
candidate_options =[]

#declare the empty dictionary
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To Do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read the header row 
    headers = next(file_reader)


    # print each row in the CSV file
    for row in file_reader:
        # add to the total vote count
        total_votes+=1

        #if candidate name is already in the list, then do not add, if it's not then append to the list
        if row[2] not in candidate_options:
            
            #append the candidate name to the empty list candidate_options, candidate name is in row[2]
            candidate_options.append(row[2])

            #begin tracking that candidates' vote count
            candidate_votes[row[2]] = 0

        #add a vote to that candidate's count
        candidate_votes[row[2]] += 1


    #print out the total votes
    #print(total_votes)
    #print all the candidates list
    #print(candidate_options)
    #print out the candidate vote dictionary.
    #print(candidate_votes)

#Winning candidate and winning count tracker, this should be initialized before we loop thru each candidate and their votes
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#determine the percentage of the votes for each candidates
#1. iterate thru the candidate options list
for cn in candidate_options:
    #retrive the vote counts:
    votes = candidate_votes[cn]
    #vote_percentage for the candidate calc
    vote_percentage = float(votes/total_votes) *100
    #print the candidate name and percentage of votes
    print(f"{cn}: {vote_percentage:.1f}% ({votes:3,})\n")


    #if vote count is greater than zero - the initial winning count, put the candidate to winner
    if votes>winning_count and vote_percentage>winning_percentage:
        winning_candidate = cn
        winning_count = votes
        winning_percentage = vote_percentage

#printing the winning summary
winning_candidate_summary = (
    f"-------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------------\n"
)
print(winning_candidate_summary)

#create a new folder in the election analysis folder with terminal
#create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")
#Using the with statement open the file as a text file.
with open(file_to_save,"w") as txt_file:
    #write some data to the file
    txt_file.write("Counties in the Election\n------------------------")

    #write three counties to the file.
    txt_file.write("\nArapahoe\nDenver\nJefferson")

txt_file.close()

#read the excel file open it

