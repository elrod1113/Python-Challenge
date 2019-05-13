import csv
import os

total_votes_cast = 0
Votes_by_candidate = 0
Percent_of_vote_Candidate = 0
Election_Winner = ""
greatest_vote_candidate = ""
candidate_options = []
candidate_votes = {}

for candidate votes in candidate_votes:
    votes = candidate_votes[candidate]
    vote_percentage = (votes / total_votes) * 100
    print(votes)
    print(total_votes_cast)
    print(vote_percentage)

    if (vote_percentage > greatest_vote_percentage):

        greatest_vote_candidate = candidate
        greatest_vote_percentage = vote_percentage
        
print("Winner" + greatest_vote_candidtate)
print("Greatest_vote_percentage_is: str(greatest_vote_percentage))