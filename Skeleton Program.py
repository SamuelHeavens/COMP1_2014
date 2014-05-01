# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014

######test change#############

import random
import datetime
import pickle

NO_OF_RECENT_SCORES = 10

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0
    self.Date = ''
    
Deck = [None]
RecentScores = [None]
Choice = ''
AceRank = False

def GetRank(RankNo):
  Rank = ''
  if RankNo == 1:
    Rank = 'Ace'
  elif RankNo == 2:
    Rank = 'Two'
  elif RankNo == 3:
    Rank = 'Three'
  elif RankNo == 4:
    Rank = 'Four'
  elif RankNo == 5:
    Rank = 'Five'
  elif RankNo == 6:
    Rank = 'Six'
  elif RankNo == 7:
    Rank = 'Seven'
  elif RankNo == 8:
    Rank = 'Eight'
  elif RankNo == 9:
    Rank = 'Nine'
  elif RankNo == 10:
    Rank = 'Ten'
  elif RankNo == 11:
    Rank = 'Jack'
  elif RankNo == 12:
    Rank = 'Queen'
  elif RankNo == 13:
    Rank = 'King'
  elif RankNo == 14:
    Rank = 'Ace'
  return Rank

def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print("5. Options")
  print("6. Save high scores")
  print("7. Load high scores")
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetMenuChoice():
  Valid = False
  while not Valid:
    Choice = input().lower()
    if Choice in ['1','2','3','4','5','6','7','q','quit']:
      Valid = True
    else:
      print("Please enter a valid option.")
      Valid = False
  return Choice

def DisplayOptions():
  print("OPTION MENU")
  print()
  print("1. Set Ace to be HIGH or LOW")
  print()
  
def GetOptionChoice():
  OptionChoice = int(input("Select an option from the menu (or enter q to quit):"))
  return OptionChoice

def SetOptions(OptionChoice):
  Valid = False
  while not Valid:
    if OptionChoice in ['q']:
      Valid = True
    elif OptionChoice == 1:
      SetAceHighOrLow()
      Valid = True
    else:
      Valid = False
      print("Error. Please enter a valid choice from the menu.")
      OptionChoice = int(input("Select an option from the menu (or enter q to quit):"))
      
def SetAceHighOrLow():
    global AceRank
    HighOrLow = input("Do you want the Ace to be (h)igh or (l)ow:").lower()
    HighOrLow = HighOrLow[0]
    Valid = False
    while not Valid:
      if HighOrLow == 'h':
        AceRank = True
        Valid = True
      elif HighOrLow == 'l':
        AceRank = False
        Valid = True
      else:
        print("Invalid Input. Try again.")
        HighOrLow = input(" Do you want the Ace to be (h)igh or (l)ow:").lower()
      print(AceRank)

def LoadDeck(Deck):
  global AceRank
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    if AceRank == True and Deck[Count].Rank == 1:
      Deck[Count].Rank = 14
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  return Higher

def GetPlayerName():
  print()
  PlayerName = input('Please enter your name: ').capitalize()
  print()
  return PlayerName

def GetChoiceFromUser():
  ValidGuess = False
  while not ValidGuess:
    Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ').capitalize()
    if Choice == 'Y' or Choice == 'Yes':
      Choice = 'y'
      ValidGuess = True
    elif Choice == 'N' or Choice == 'No':
      Choice = 'n'
      ValidGuess = True
    else:
      print("Error. Please enter in a valid choice.")
  return Choice

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0

def DisplayRecentScores(RecentScores):
  print()
  print('Recent Scores: ')
  print()
  print("Name".ljust(10),"Date".ljust(10),"Score")
  print()
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    print(RecentScores[Count].Name.ljust(10),RecentScores[Count].Date.ljust(10),RecentScores[Count].Score)
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()

def UpdateRecentScores(RecentScores, Score):
  today = datetime.date.today()
  Date = today.strftime('%d/%m/%y')
  ValidResponse = False
  AddToScoreTable = input("Do you want to add your score to the high score table? (y or n):").capitalize()
  while not ValidResponse:
    if AddToScoreTable == 'Y' or AddToScoreTable == 'Yes':
      ValidResponse = True
      ValidName = False
      PlayerName = ''
      while not ValidName:
        PlayerName = GetPlayerName()
        if not (len(PlayerName) > 0) :
          print("You must enter something for your name!")
        else:
          ValidName = True
      FoundSpace = False
      Count = 1
      while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
        if RecentScores[Count].Name == '':
          FoundSpace = True
        else:
          Count = Count + 1
      if not FoundSpace:
        for Count in range(1, NO_OF_RECENT_SCORES):
          RecentScores[Count].Name = RecentScores[Count + 1].Name
          RecentScores[Count].Score = RecentScores[Count + 1].Score
        Count = NO_OF_RECENT_SCORES
      RecentScores[Count].Name = PlayerName
      RecentScores[Count].Score = Score
      RecentScores[Count].Date = Date
    elif AddToScoreTable == 'N' or AddToScoreTable == 'No': 
      print("Thank you for playing!")
      ValidResponse = True
    else:
      print("Error. Please enter in a valid choice.")  
      ValidResponse = True

def SaveScores(RecentScores):
  with open("save_scores.txt.", mode="wb") as my_file:
    pickle.dump(RecentScores, my_file)

def LoadScores():
  with open("save_scores.txt.", mode="rb") as my_file:
      RecentScores = pickle.load(my_file)      
  return RecentScores

def PlayGame(Deck, RecentScores):
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n'):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard)
    if (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    else:
      GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)

def BubbleSortScores(RecentScores):
    swapped = True
    list_length = len(RecentScores)
    while swapped:
        list_length = list_length - 1
        swapped = False
        print(RecentScores[1].Score)
        for count in range(1,list_length):
            if RecentScores[count].Score < RecentScores[count+1].Score:
                tempScore = RecentScores[count].Score
                tempDate = RecentScores[count].Date
                tempName = RecentScores[count].Name
                RecentScores[count].Score = RecentScores[count+1].Score
                RecentScores[count].Date = RecentScores[count+1].Date
                RecentScores[count].Name = RecentScores[count+1].Name
                RecentScores[count+1].Score = tempScore
                RecentScores[count+1].Date = tempDate
                RecentScores[count+1].Name = tempName                
                swapped = True
    return RecentScores
  
if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())
  Choice = ''
  while Choice != 'q' or Choice != 'quit' :
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      RecentScores = BubbleSortScores(RecentScores)
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == "5":
      DisplayOptions()
      OptionChoice = GetOptionChoice()
      SetOptions(OptionChoice)
    elif Choice == '6':
      SaveScores(RecentScores)
    elif Choice == '7':
      try:
        RecentScores = LoadScores()
      except FileNotFoundError:
        SaveScores(RecentScores)
        print("File not found.")
    elif Choice == 'quit' or Choice == 'q':
      print()
      print("Program shuting down...")
      break
      


