##Task 6 Questions:

1. In it's own function so it can easily be found.
2. The def DisplayMenu(): function.
3. The def GetRank(RankNo): function.

##Task 6 Pseudo-code:

	FUNCTION DisplayMenu()
		OUTPUT "OPTION MENU"
		OUTPUT ""
		OUTPUT "1. Set Ace to be HIGH or LOW"
		OUTPUT ""

	FUNCTION GetOptionChoice()
		OptionChoice <- INT(INPUT("Select an option from the menu (or enter q to quit)"))
		RETURN OptionChoice
	
	FUNCTION SetOptions(OptionChoice:String/Integer)
		Valid : Boolean
		ARRAY ['q']: String [1]
		Valid <- FALSE
		WHILE NOT Valid THEN
			IF OptionChoice in ['q'] THEN
				Valid <- TRUE
				END IF
			ELIF OptionChoice == 1 THEN
				SetAceHighOrLow()
				Valid <- TRUE
				END ELIF
			ELSE THEN
				Valid <- FALSE
				OUTPUT "Error. Please enter a valid choice from the menu."
				OptionChoice <- INT(INPUT("Select an option from the menu (or enter q to quit)"))
				END ELSE
		END WHILE
		
	FUNCTION SetAceHighOrLow()
		global AceRank
		AceRank: Boolean
		HighOrLow <- INPUT ("Do you want the Ace to be (h)igh or (l)ow:").lower()
		HighOrLow <- HighOrLow[0]
		Valid : Boolean
		Valid <- FALSE
		WHILE NOT Valid THEN
			IF HighOrLow == 'h' THEN
				AceRank <- TRUE
				Valid <- TRUE
				END IF
			ELIF HighOrLow == 'l' THEN
				AceRank <- FALSE
				Valid <- TRUE
				END ELIF
			ELSE THEN
				OUTPUT "Invalid Input. Try again."
				HighOrLow <- INPUT ("Do you want the Ace to be (h)igh or (l)ow:").lower()
				END ELSE
			OUTPUT AceRank
		END WHILE

##Test Table:

|TestNumber|Test Description|Test Data|Type|Expected Result|Actual Result|
|----------|----------------|---------|----|---------------|-------------|
|1| |quit|normal|The user enters 'quit' or 'q' to end the game.|
##Task 7 - Pseudo-code

	FUNCTION BubbleSortScores(RecentScores:String)
		swapped : Boolean
		swapped <- TRUE
		list_length <- len(RecentScores)
		WHILE swapped THEN
			list_length <- list_length -1
			swapped <- FALSE
			OUTPUT (RecentScores[1].Score)
			FOR Count IN range(1,list_length) THEN
				IF RecentScore[count].Score < RecentScores[count+1].Score THEN
					tempScore <- RecentScore[count].Score
					tempDate <- RecentScores[count].Data
					tempName <- RecentScores[count].Name
					RecentScore[count].Score <- recentScores[count+1].Score
					RecentScore[count].Date <- RecentScore [count+1].Date
					RecentScore[count].Name <- RecentScores[count+1].Name
					RecentScores[count+1].Score <- tempScore
					RecentScores[count+1].Date <- tempDate
					RecentScores[count+1].Name <- tempName
					swapped <- TRUE
					END IF
		END WHILE
