#The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score

from datetime import datetime

# as a temporary, i just take input from user, and store it in a game score file
game_sc = input("Enter Game Score : ")
current_datetime = datetime.now()

game_score = f"{current_datetime} : {game_sc} \n"
with open("gamescor.txt", "a") as f:
    f.write(game_score)
