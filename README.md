# Election_Analysis

## Project Overview
The following tasks were completed as requested by the Colorado Board of Elections for an election audit using recent local congressional election data.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who recieved votes.
3. Calculate the total number of votes each cnadidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the elcetion based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.66.2

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the votes and 85,213 votes.
    - Diana DeGette received 73.8% of the votes and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the votes and 11,606 votes.
- The winner of the elcetion was:
    - Diana DeGette who received 73.8% of the votes and 272,892 votes.

## Challenge Overview
Additional analysis was completed in order to better understand county statistics in the local election audit. The following items were completed to gain insight into county voting details.

1. Calculate voter turnout for each county.
2. Calculate the percentage of votes from each county out of the total vote count.
3. Determine the county with the highest voter turnout.

## Challenge Results
In the 369,711 votes that were cast in this election each county received the following number of votes:
    - Jefferson county turned out 38,855 votes.
    - Denver county turned out 306,055 votes.
    - Arapahoe county turned out 24,801 votes.
The full election details are seen in the follow data from the election_analysis.txt file:
![Election Details](https://github.com/Trevor-Jackson94/Election_Analysis/blob/main/election_analysis.PNG)


## Challenge Summary
This script has proven very versatile and can and should be used to help quickly calculate and analyze local election results across the country. To return data in a similar format, we would only need to obtain a .csv file with the election results and make a few minor adjustments to column notation. Using our Python script you can easily adjust the notation to work for any variety of election including statewide elections or even nationwide elections. We could extrapolate the script to contain all counties in a state and even set electoral college votes to each state to determine presidential votes and elections. Very few modifications would be needed to support any number of candidates or counties in the script as is. 
