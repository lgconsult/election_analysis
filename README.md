# election_analysis

## Overview of Election Audit
The Board of Elections has requested this report to verify certain statistics for the election. These variables include the total voter turnout for each county, the percentage of votes for each county out of the total vote count, and the county with the highest turnout. In the following picture you can see the variables we initialize to begin calculating our results
![Initializing New Variables](https://github.com/lgconsult/election_analysis/blob/main/initialize_new_variables.png)

## Election-Audit Results
- There were 369,711 votes cast total.
- Arapahoe county had 24,801 votes, the lowest share at just 6.7% of the total vote count. Jefferson county had the next highest voter share with 38,855 although still only making up 10.5% of the vote total. Denver County had by far the largest voter share with 306,055 votes and 82.3% of total votes. We used a for loop to iterate through the county rows and produce a new county list for each unique county and then tally the votes within each county
![Printing the Electon Results by County](https://github.com/lgconsult/election_analysis/blob/main/county_results.png)

- Denver County had the largest number of votes and by far the largest voter share (306,055 and 82.3% of vote total)
- Diana DeGette had the most votes with 272,892 and 73.8% of the vote. Charles Casper Stockham came in second with 85,213 votes and 23.0% of the vote while Raymon Anthony Doane came in third with 11,606 votes and only 3.1% of the total vote. Below is same for loop we used to calculate the county list and vote totals, where we also use it to calculate our candidate vote totals. By switching the county_name variable with candidate_name, and the other associated variables, we can calculate both within the same for loop.
  ![Candidate Vote Totals and Calculation](https://github.com/lgconsult/election_analysis/blob/main/candidate_results.png)
- Diana DeGette won the election with 272,892 and 73.8% of the vote. Charles Casper Stockham came in second with 85,213 votes and 23.0% of the vote.

## Election-Audit Summary
The code provided is versatile and can be used for different types of elections. For example, we could manipulate the code to calculate a county council election, simultaneously calculating multiple districts at once. First, we would calculate the total number of votes for all candidates regardless of district much like the beginning of the code presented, than sort their vote tallies by district using another for loop, and calculate the winner for each district in the same for loop with an if statement. We could also use this code to audit a local city council race, where there are no weighted dsitricts. We would simply remove the code related to calculating the county vote totals.
