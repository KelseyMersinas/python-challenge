# import csv
import csv

# find and insert into reader
csvpath = "Resources/election_data.csv"

# open the file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip the header row 
    csv_header = next(csvreader)
    # set total votes to 0
    total_votes = 0
    # loop for to count total entries and create new list 
    candidate_list = []
    for row in csvreader:
        total_votes += 1
        candidate_list.append(row[-1])
        
    # loop though that list and create a new list without duplicates only showing the names that received a vote 
    candidate = []
    for name in candidate_list:
        if name not in candidate:
            candidate.append(name) 

    # calulate total votes that each candidate won
    votes_for_candidate1 = candidate_list.count((candidate[0]))
    votes_for_candidate2 = candidate_list.count((candidate[1]))
    votes_for_candidate3 = candidate_list.count((candidate[2]))

    # find the percentage for each candidate and save as variable
    percent_vote_candidate1 = (votes_for_candidate1 / total_votes) * 100
    percent_vote_candidate2 = (votes_for_candidate2 / total_votes) * 100
    percent_vote_candidate3 = (votes_for_candidate3 / total_votes) * 100

    # using if statement return the 
    if (votes_for_candidate1 > votes_for_candidate2) and (votes_for_candidate1 > votes_for_candidate3):
        winner = candidate[0]
    elif (votes_for_candidate2 > votes_for_candidate1) and (votes_for_candidate2 > votes_for_candidate3):
        winner = candidate[1]
    else:
        winner = candidate [2]
    # print to terminal 
    pgbrk = "-------------------------"
    print("Election Results")
    print(f"{pgbrk}")
    print(f"Total votes: {total_votes}")
    print(f"{pgbrk}")
    print(f"{candidate[0]}: {percent_vote_candidate1:.3f}% ({votes_for_candidate1})")
    print(f"{candidate[1]}: {percent_vote_candidate2:.3f}% ({votes_for_candidate2})")
    print(f"{candidate[2]}: {percent_vote_candidate3:.3f}% ({votes_for_candidate3})")
    print(f"{pgbrk}")
    print(f"Winner: {winner}")
    
    # I referenced Xpert Learning to explain how to use the format funtion in f strings
    #output to text file 
    output = (
        "Election Results\n\n"
        f"{pgbrk}\n\n"
        f"Total votes: {total_votes}\n\n"
        f"{pgbrk}\n\n"
        f"{candidate[0]}: {percent_vote_candidate1:.3f}% ({votes_for_candidate1})\n\n"
        f"{candidate[1]}: {percent_vote_candidate2:.3f}% ({votes_for_candidate2})\n\n"
        f"{candidate[2]}: {percent_vote_candidate3:.3f}% ({votes_for_candidate3})\n\n"
        f"{pgbrk}\n\n"
        f"Winner: {winner}\n\n"
        f"{pgbrk}"
    )

    with open("Analysis/pyPoll_text.txt", "w") as f:
        f.write(output)