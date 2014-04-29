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
		Valid <- False
		WHILE NOT Valid THEN
			IF OptionChoice in ['q'] THEN
				Valid <- True
			ELIF OptionChoice == 1 THEN
				SetAceHighOrLow()
				Valid <- True
			ELSE THEN
				Valid <- False
				OUTPUT "Error. Please enter a valid choice from the menu."
				OptionChoice <- INT(INPUT("Select an option from the menu (or enter q to quit)"))
			
	FUNCTION SetAceHighOrLow()
		global AceRank
		AceRank: Boolean
		HighOrLow <- INPUT ("Do you want the Ace to be (h)igh or (l)ow:").lower()
		HighOrLow <- HighOrLow[0]
		Valid : Boolean
		Valid <- False
		WHILE NOT Valid THEN
			IF HighOrLow == 'h' THEN
				AceRank <- True
				Valid <- True
			ELIF HighOrLow == 'l' THEN
				AceRank <- False
				Valid <- True
			ELSE THEN
				OUTPUT "Invalid Input. Try again."
				HighOrLow <- INPUT ("Do you want the Ace to be (h)igh or (l)ow:").lower()
			OUTPUT AceRank

