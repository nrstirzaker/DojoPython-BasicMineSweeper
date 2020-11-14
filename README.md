**Learning Python**

I help run a CoderDojo. I wanted to create a "learning" project to help our learners learn python. Knowing the syntax is time consumer but doable. But the real skill is learning things like Decomposition. Taking a big idea/problem and then breaking it down into small enough parts so that you can get your head round it and code it. I'm sure the code could be optimised in many ways, but its purpose is to help the learners take the constructs they know and enable them to create a game

When the game is run the player is shown a board and

    A B B D
1   O O O O
2   O O O O
3   O O O O
4   O O O O

There are hidden mines. The user has to guess and input the coordinates to try and find the mines. There is currently no score and no way to loose

Things the code needs to do

Data
    1) A Data structure that holds the 0 and X that are displayed
    2) A Data Structure that holds the hidden mines


Program flow
1) "A game loop"  -  a loop that continues until all mines are found
    2) Display the top line A B C D
    3) Display all the other rows 
    4) Take user input
    5) Validate user input
    6) Has user found a mine?
        7) Updated the displayed data structure
        8) diplay a message
    else
        9)dislay a message
    10) Has user found all the mines?
        11) end the game loop and a message


