#add the dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save a file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To Do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read and print the header row 
    headers = next(file_reader)
    print(headers)

    # print each row in the CSV file
    for row in file_reader:
        print(row)


#The ddata we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

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

