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
		Gatherer - Keeps a total of a series of values.
		Transformation - A variable that gets it's new value from the calculation from another calculation of variables. e.g. conversions.
		Follower - Keeps track of a previous value of a variable.
		Temporary - A variable used for holding a value for a short time. This could be used when swapping values of variables.

Examples of each:

		Fixed Value: NoOfSwaps line 98
		Stepper: Count line 94
		Most recent holder:  Choice 197
		Most wanted holder: LineFromFile line 87, LastCard line 187
		Gatherer: - (None in program) 
		Transformation: Higher line 124, FoundSpace 171
		Follower: LastCard line 187
		Temporary: Swap space line 97

##Additional Task - Functions And Parameters

1. Describe the difference between passing by value and passing by reference in your own words:

		When you pass by value, a copy of the data is passed into the function so you are not working on the original data.
		When we pass by reference, you are working on the original data.

2. For each function in the program identify the mechanism using to pass each parameter:

		GetRank Function - RankNo is passed via value
		GetSuit Function - SuitNo is passed via value
		DisplayEndOfgameMessage - Score is passed via value
		LoadDeck Function - Deck is passed by reference
		ShuffleDeck Function - Deck is passed by reference
		DisplayCard Function - ThisCard is passed by reference - record
		GetCard Function - ThisCard, Deck and NoOfCardsTurnedOver are all passed by reference 
		IsNextCardHigher Function - LastCard and NextCard both passed by value
		DisplayEndOfGameMessage Function - Score is passed by reference
		DisplayCorrectGuessMessage Function - Score is passed by reference
		ResetRecentScores Function - RecentScores is passed by reference
		DisplayRecentScores Function - RecentScores is passed by reference
		UpdateRecentScores Function - RecentScores and Score are both passed by reference
		PlayGame Function - Deck and RecentScores are bother passed by reference