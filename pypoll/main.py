import os 
import csv

#Requirements:

#total number of votes cast
#list of canidates who recieved votes
#percentage of votes each canidate won
#total number of votes each canidate won
#The winner of the election based on popular vote.
#Cycle through["Kahn", "Correy", "Li", "O'Tooley"]

candidateTallyRecord = {}
with open(election_data_csv, newline="") as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csv_reader)	
	for row in csv_reader:
		voterId = row[0]
		county = row[1]
		canidateName = row[2] each row. Start with the 2nd to exclude the header row





#For i = 2 to lastrow
	
	# Add 1 to a sum of all previous votes

totalNumberOfVotes = 0 
candidateList = 

		#print("voterId is " )

		if canidateName != None
			if county != None
				if int(voterId) > 0
					totalnumberOfVotes += 1

	


		#print(row)

print(totalnumberOfVotes)

Data_Stats_Message = print(F"""""""""""
	  		Election Results
  		 -------------------------
  	  Total Votes: {totalnumberOfVotes}
  		 -------------------------
 		  Khan: 63.000% (2218231)
  		 Correy: 20.000% (704200)
  		   Li: 14.000% (492940)
 		 O'Tooley: 3.000% (105630)
 		 -------------------------
 			 Winner: {winner}
  		 -------------------------
""""""""""")





