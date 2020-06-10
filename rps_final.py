from random import choice as rand_choice
from collections import deque

class rockPaperScissors:
    
    def __init__(self):
        self.member_scores = dict()
        self.player_name = input("Enter your name: ")
        print("Hello, "+self.player_name)
        self.play_with = list(input().split(","))
        if self.play_with == [""]:
            self.play_with = ["scissors", "paper", "rock"]
        self.win_range = int((len(self.play_with) - 1) / 2) + 1
        print("Okay, let's start")
        self.player_choice = ""
        self.player_score = 0
        self.pc_score = 0
        self.draws = 0

    def get_scores(self):
        ##  fill dictionary= with members/players from saved scores/ratings
        with open("/Users/User/Dropbox/Python/SANDBOX/RPS/rating.txt") as member_f:
            for member in member_f:
                name, score = member.split()
                self.member_scores[name] = int(score)
                if member[0] == self.player_name:
                    self.player_score = int(score)
                else:
                    continue
        ##   add new player to dictionary
        if self.player_name not in self.member_scores:
            self.member_scores[self.player_name] = 0
        return self.member_scores

    def moves_dict(self):
        moves = dict()
        d_list = []
        items = deque(self.play_with)
        items_w = items.copy()
        if self.win_range > 2:
            for i in list(items):
                items_w.rotate(self.win_range)
                d_list = list(items_w)
                moves[d_list[0]] = d_list[1:self.win_range]
        else:
##            print(items_w)
            for i in list(items):
                items_w.rotate(-1)
                d_list = list(items_w)
                moves[d_list[0]] = d_list[-1]            
        print(moves)
        return moves

    def play_result(self):
        options = []
        options = self.play_with + ["!rating", "!exit"]
        self.player_choice = input()
        ##  ensure to get the correct input        
        while self.player_choice not in options:
            print("Invalid input")
            self.player_choice = input()
        if self.player_choice not in ["!rating", "!exit"]:
            ##  decide what to do with it >
            pc_choice = rand_choice(self.play_with)
            self.winnings = self.moves_dict()[self.player_choice]
##            print(self.winnings, pc_choice)
            if self.player_choice == pc_choice:
                self.member_scores[self.player_name] += 50
                self.pc_score += 50
                print(f"There is a draw ({self.player_choice})")
            elif pc_choice in self.winnings:
                self.pc_score += 100
                print(f"Sorry, but computer chose {pc_choice}")
            else:
                self.member_scores[self.player_name] += 100
                print(f"Well done. Computer chose {pc_choice} and failed")
        else:
            if self.player_choice == "!exit":
                ##  update player/member score before exit and update/write to the scores-file
                self.member_scores[self.player_name] = self.player_score
                with open("/Users/User/Dropbox/Python/SANDBOX/RPS/rating.txt", "w") as member_f:
                    for name, score in self.member_scores.items():
                        member_f.write("%s %s\n" % (name, score))
                return False
            elif self.player_choice == "!rating":
                self.player_score = self.member_scores[self.player_name]
                print(f"Your rating: {self.player_score}")    
        return True
        
    def play(self):
        self.get_scores()
        continue_play = True
        while continue_play != False:
            continue_play = self.play_result()
        print("Bye")
        
            
game = rockPaperScissors()
game.play()

