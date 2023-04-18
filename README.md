# RockPaperScissors
This is a Rock-Paper-Scissors Game based on User Input

I have written the following code to take user input for each of the 2 players- Person1 and Person2.

Their respective 'choice' (either 'rock', 'paper', or 'scissors') will be saved in choicePerson1 and choicePerson2.

Then, the function rockPaperScissors will be called onto choicePerson1 and choicePerson2 to yield the outcome: it's a win for Person1, it's a loss for Person1, or it's a draw.

The rockPaperScissors function arrives an at answer by first calling on another function - the hierarchy function.

I designed the hierarchy function to  avoid having to write a bunch of if/elif/else statment for every possible scenario between the players.

The hierarchy function returns a dictionary, where:
* There are three keys - one for each outcome - "It's a win" / "Sadly, it's a loss" / "It's a draw" for Person 1.
    - There is 1 value per key: given the order of the list_of_choices, ['rock', 'paper', 'scissors'], it follows that, for example, 'rock'
            - Wins over 'scissors', which is one position to the left. So, position of rock - 1 = position of scissors
            - Loses under 'paper', which is one position to the right on the list_of_choices. So, position of rock - 2 = position of paper
            - Draws against itself - so, when the positions match on the list.
    - So, for every choice, we can build a dictionary where there is a key with the string for winning, one for losing, and one for drawing.
    - When we initialise rockPaperScissors, the input for Person1, which is called choicePerson1, is ran using the hierarchy function, and the output dictionary is 
        itemised using a for loop. The values are compared with the input for Person2, choicePerson2, and when it matches, the key (which has the message for winning,
        losing and drawing) is returned.
