# Election Analysis

## Project Overview
A Colorado Board of Elections employee gave the following tasts to complete the election audit of a recent local congressional election:

1. Calculate the total number of votes cast in the congressional election
2. Get a complete list of candidates who received votes
3. Calculate the total nmber of votes each candidate received in the election.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on the popular vote.
6. Calculate voter turnout for each county
7. Calculate percentage of votes from each county out of the total count
8. Determine the county with the highest voter turnout

## Resources
- Data Source: election_results.csv
-Software: Python 3.7.6, Visual Studio Code, 1.38.1

## Election-Audit Results
The analysis of the congressional election show that:
- There were 369,711 total votes in the congressional election.
- The votes per county were:
    - 10.5% of the votes or 38,855 number of votes came from Jefferson County.
    - 82.8% of the votes or 306,055 number of votes came from Denver County.
    - 6.7% of the votes or 24,801 number of votes came from Arapahoe County.
- The majority of the votes came from Denver County.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doanne
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes
    - Raymon Anthony Doane received 3.1% of the votes and 11,606 nunber of votes
- The winner of the election was Diana DeGette who received 73.8% of the total vote and 272,892 number of votes.

## Election Audit Summary
In the case that a state is using electronic polling in their elections (city, county, state, etc.) this algorithm can be used to tabulate the results of said election at a faster speed and reduce human bias and error when determening the results. If the Board of Elections would like to understand election audit results through a city perspective, they would need to collect such data and then replace county related variables in this algorithm for city related variables (to make reading the code easier). Additionally, this algorithm can reduce audit times for those jurisdictions that continue to tabulate votes by hand. 





