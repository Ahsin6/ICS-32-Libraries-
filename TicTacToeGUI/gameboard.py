

class BoardClass():
    def __init__(self, player1: str = '', player2: str = '', player1wins: int = 0, player2wins: int = 0, ties: int = 0, player1losses: int = 0, player2losses: int = 0, turn: int = 0, games: int = 0, namePlayer1: str = '', namePlayer2: str = ''):
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.player1 = "X"
        self.player2 = "O"
        self.namePlayer1 = ''
        self.namePlayer2 = ''
        self.player1wins = player1wins
        self.player2wins = player2wins
        self.ties = ties
        self.player1losses = player1losses
        self.player2losses = player2losses
        self.turn = 0
        self.games = games
        self.lis2 = []
        self.lastPlayer = ''
    
    def printboard(self):
        for i in range(3):
            print(self.board[i][0], '|', self.board[i][1], '|', self.board[i][2])
            if i < 2:
                print("-"*10)

    def resetGameBoard(self):
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.lis2 = []


    def updateGamesPlayed(self):
        self.games += 1
        
        
        

    def Boardfull(self, turn):
        if ' ' not in self.board[0] and ' ' not in self.board[1] and ' ' not in self.board[2]:
            print("Tie!")
            self.ties += 1
            return False
        return True

    
    def updateGameBoard(self, user, turn):
        if turn % 2 == 0:
            player = self.player1
        else:
            player = self.player2
            
        if user == '1':
            self.board[0][0] = player
        elif user == '2':
            self.board[0][1] = player
        elif user == '3':
            self.board[0][2] = player
        elif user == '4':
            self.board[1][0] = player
        elif user == '5':
            self.board[1][1] = player
        elif user == '6':
            self.board[1][2] = player
        elif user == '7':
            self.board[2][0] = player
        elif user == '8':
            self.board[2][1] = player
        elif user == '9':
            self.board[2][2] = player
        else:
            print("Not a valid input:\n")

            
    def isWinner(self, turn):
        if ((self.board[0][0] != ' ') and (self.board[1][1] != ' ') and (self.board[2][2] != ' ')) or ((self.board[0][2] != ' ') and (self.board[1][1] != ' ') and (self.board[2][0] != ' ')):
            if (self.board[0][2] == "X" and self.board[1][1] == "X" and self.board[2][0] == "X"):
                print("win X")
                self.player1wins += 1
                self.player2losses += 1
                return False
            elif self.board[0][0] == "X" and self.board[1][1] == "X" and self.board[1][1] == self.board[2][2]:
                print("win X")
                self.player1wins += 1
                self.player2losses += 1
                return False
            if (self.board[0][2] == "O" and self.board[1][1] == "O" and self.board[2][0] == "O"):
                print("win O")
                self.player2wins += 1
                self.player1losses += 1
                return False
            elif self.board[0][0] == "O" and self.board[1][1] == "O" and self.board[2][2] == "O":
                print("win O")
                self.player2wins += 1
                self.player1losses += 1
                return False
        for index, rows in enumerate(self.board):
            if rows[0] != ' ':
                if rows[0] == "X" and rows[1] == "X" and rows[1] == rows[2]:
                    print("WIN X")
                    self.player1wins += 1
                    self.player2losses += 1
                    return False
                elif rows[0] == "O" and rows[1] == "O" and rows[1] == rows[2]:
                    print("WIN O")
                    self.player2wins += 1
                    self.player1losses += 1
                    return False
        for index in range(3):
            if index == 0:
                if self.board[0][0] != ' ':
                    if self.board[0][0] == "X" and self.board[1][0] == "X" and self.board[1][0] == self.board[2][0]:
                        print("WIN X")
                        self.player1wins += 1
                        self.player2losses += 1
                        return False
                    elif self.board[0][0] == "O" and self.board[1][0] == "O" and self.board[1][0] == self.board[2][0]:
                        print("WIN O")
                        self.player2wins += 1
                        self.player1losses += 1
                        return False
                    else:
                        continue
                else:
                    continue
            if index == 1:
                if self.board[0][1] != ' ':
                    if self.board[0][1] == "X" and self.board[1][1] == "X" and self.board[1][1] == self.board[2][1]:
                        print("WIN X")
                        self.player1wins += 1
                        self.player2losses += 1
                        return False
                    elif self.board[0][1] == "O" and self.board[1][1] == "O" and self.board[1][1] == self.board[2][1]:
                        print("WIN O")
                        self.player2wins += 1
                        self.player1losses += 1
                        return False
                    else:
                        continue
                else:
                    continue
            if index == 2:
                if self.board[0][2] != ' ':
                    if self.board[0][2] == "X" and self.board[1][2] == "X" and self.board[1][2] == self.board[2][2]:
                        print("WIN X")
                        self.player1wins += 1
                        self.player2losses += 1
                        return False
                    elif self.board[0][2] == "O" and self.board[1][2] == "O" and self.board[1][2] == self.board[2][2]:
                        print("WIN O")
                        self.player2wins += 1
                        self.player1losses += 1
                        return False
                    else:
                        continue
                else:
                    continue
        return True
    

    def printStats(self):
        print('\n' + self.namePlayer1, '\n')
        print("Player with the last move:", self.lastPlayer, '\n')
        print(self.namePlayer2, '\n')
        print("Games played:", self.games, '\n')
        print(self.namePlayer1, "Wins:", self.player1wins, '\n')
        print(self.namePlayer2, "Wins:", self.player2wins, '\n')
        print(self.namePlayer1, "losses:", self.player1losses, '\n')
        print(self.namePlayer2, "losses:", self.player2losses, '\n')
        print("Games tied:", self.ties, '\n')



        
        
       
