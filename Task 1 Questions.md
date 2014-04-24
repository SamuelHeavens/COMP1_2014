#Task 1 Validation Questions Answers

##Task 3(a) - Validating the name for a recent score

1.	GetPlayerName
2.	In the UpdateRecentScores function make a Boolean while loop and if the user wants to type in a name, make sure that the length of the username > 0 so it keeps being asked until they answer an appropriate name.
3.	Boolean – ValidResponse.

##Task 3(b) - Deciding whether you want to add your name to the recent score table

1.	ValidName : Boolean
	ValidName <- False
	WHILE NOT ValidName DO
	PlayerName : String
	PlayerName <- GetPlayerName
		IF NOT (len(PlayerName) > 0 THEN
			OUTPUT  “You must enter something for your name!”
			END IF
		ELSE:
			ValidName <- True
			END WHILE

##Task 5 - Adding a date to the recent scores

1.	Import datetime
2.	DisplayRecentScores, UpdateRecentScores and TRecentScore
3.	By using the following code:
  today = datetime.date.today()
  Date = today.strftime('%d-%m-%y')

##Additional Task - Variable roles

Fixed Value - A variable obtained with out any calculation and doesn't change.
Stepper - A variable used to keep a count of the number of repetitions.
Most recent holder - A variable used to store the latest of a series of values.
Most wanted holder - Stores the most appropriate value encountered. e.g. storing the largest value calculated so far.
Gatherer - A variable accumulating the effect of individual values. e.g. calculating a series of values we keep a running total.
Transformation - A variable that gets it's new value from the calculation from another calculation of variables. e.g. conversions.
Follower - A variable that's value is obtained from another variable's OLD value acting like a copy.
Temporary - A variable used for holding a value for a short time. This could be used when swapping values of variables.

Examples of each:

Fixed Value: NO_OF_RECENT_SCORES
Stepper: Count
Most recent holder:  Choice
Most wanted holder: Score
Gatherer: Score
Transformation: Score
Follower:
Temporary: Count 

##Additional Task - Functions And Parameters

1. Describe the difference between passing by value and passing by reference in your own words:

   Only lists and records are passed by value, all other data types are passed by reference. When you pass by value, a copy of the 
   data is passed into the function so you are not working on the original data, this is why we must return the variable at the end
   of a function so that we can update the original. When we pass by reference, you are working on the original data, when you change
   the data within a function you are changing the original so there is no need to return the variable at the end of a function.

2. For each function in the program identify the mechanism using to pass each parameter:

   GetRank Function - RankNo is passed by value
   GetSuit Function - SuitNo is passed by value
   LoadDeck Function - Deck is passed by reference
   ShuffleDeck Function - Deck is passed by reference
   DisplayCard Function - ThisCard is passed by reference
   GetCard Function - ThisCard, Deck and NoOfCardsTurnedOver are all passed by reference 
   IsNextCardHigher Function - LastCard and NextCard both passed by value
   DisplayEndOfGameMessage Function - Score is passed by reference
   DisplayCorrectGuessMessage Function - Score is passed by reference
   ResetRecentScores Function - RecentScores is passed by reference
   DisplayRecentScores Function - RecentScores is passed by reference
   UpdateRecentScores Function - RecentScores and Score are both passed by reference
   PlayGame Function - Deck and RecentScores are bother passed by reference
