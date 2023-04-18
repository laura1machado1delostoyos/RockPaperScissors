"""
I have written the following code to take user input for each of the 2 players- Person1 and Person2.
Their respective 'choice' (either 'rock', 'paper', or 'scissors') will be saved in choicePerson1 and choicePerson2, respectively.
Then, the function rockPaperScissors will be called onto choicePerson1 and choicePerson2 to yield the outcome: it's a win for Person1, it's a loss for Person1, or it's a draw.
The rockPaperScissors function arrives an at answer by first calling on another function - the hierarchy function.
I designed the hierarchy function to  avoid having to write a bunch of if/elif/else statment for every possible scenario between the players.
The hierarchy function returns a dictionary, where:
    * There are three keys - one for each outcome - "It's a win" / "Sadly, it's a loss" / "It's a draw" for Person 1.
    * There is 1 value per key: given the order of the list_of_choices, ['rock', 'paper', 'scissors'], it follows that, for example, 'rock'
            - Wins over 'scissors', which is one position to the left. So, position of rock - 1 = position of scissors
            - Loses under 'paper', which is one position to the right on the list_of_choices. So, position of rock - 2 = position of paper
            - Draws against itself - so, when the positions match on the list.
    * So, for every choice, we can build a dictionary where there is a key with the string for winning, one for losing, and one for drawing.
    * When we initialise rockPaperScissors, the input for Person1, which is called choicePerson1, is ran using the hierarchy function, and the output dictionary is 
        itemised using a for loop. The values are compared with the input for Person2, choicePerson2, and when it matches, the key (which has the message for winning,
        losing and drawing) is returned.

"""


# Trigger user input and save it onto the respective variables
choicePerson1 = input("Please, enter the choice(rock, paper or scissors) for person 1:")
choicePerson2 = input("Please, enter the choice(rock, paper or scissors) for person 2:")

# The function definitions:

# # hierarchy is a function that returns a dictionary for every choice. 
# # The dictionary for 'rock' is {
#                                   "It's a win for Person1": 'scissors', 
#                                   "Sadly, this is a loss for Person1": 'paper',  
#                                   "It's a draw!": 'rock'
#                                   }
# Each dictionary is automatically generated from a position in list_of_choices
def hierarchy(choice):
#   Define list_of_choices - the point is to have each 'choice' at a specific position.
  list_of_choices = ['rock', 'paper', 'scissors']

  position = list_of_choices.index(choice)
  # The outcome dictionary is computed based on the relative positions of the choice
  # and the rest of the list_of_choices list.
  hierarchy_dict = {
      "It's a win for Person1": list_of_choices[position - 1],
      "Sadly, this is a loss for Person1": list_of_choices[position - 2],
      "It's a draw!": list_of_choices[position]
  }
  return hierarchy_dict




# The purpose of rockPaperScissors is to loop the outcome dictionary from the hierarchy function
# and return the key, which is a string with the outcome
def rockPaperScissors(choicePerson1, choicePerson2):
  list_of_choices = ['rock', 'paper', 'scissors']

#   We first make sure to remove capitalisation
  choicePerson1 = choicePerson1.lower()
  choicePerson2 = choicePerson2.lower()
# We add this if/else clause to make sure no rogue words are used.
  if (choicePerson1 in list_of_choices) and (choicePerson2 in list_of_choices):
    # We are going to load the hierarchy dictionary for the choice made by Person1.

      hierarchy_dict_1 = hierarchy(choicePerson1)

    #   Then, loop through that hierarchy dictionary. When the value of a given key matches the value of the choice for Person2,
    #   return the key value.
    #   As an example, if choicePerson1 was 'rock' and choicePerson2 was 'paper', the for loop would return
    #   "Sadly, this is a loss for Person1", because that's where the value 'paper' was located.
      for key, value in hierarchy_dict_1.items():

        if value == choicePerson2:
          output_string = key
          return output_string
        else:
          continue
  else:
    print("Hey! Their only choices are: rock, paper or scissors. Please enter them as text.")
# This is the main command:
print(rockPaperScissors(choicePerson1, choicePerson2))