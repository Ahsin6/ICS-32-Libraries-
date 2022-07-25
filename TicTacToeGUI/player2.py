from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import askyesno
from tkinter.simpledialog import askstring
from gameboard import BoardClass
import socket
import threading

HOST = '127.0.0.1'
PORT = 50007
RECV_SIZE = 1024

class gui():

    def __init__(self, host, port, gb=BoardClass()):

        self.link_to_server = None

        
        self.socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.conn = None
        self.addr = None

        self.is_connected = False
        self.did_close = False
        self.socket_input = ''
        self.socket_output = ''



        self.gb = gb
        

        self.root = Tk()
        self.root.geometry("600x600")
        self.root.title(" Tic Tac Toe ser")

        
        

        self.b1 = Button(self.root, text=self.gb.board[0][0], font = ("Arial", 10), height=6, width = 6, command=lambda: self.click1())
        self.b1.place(x=0, y=10)
        self.b2 = Button(self.root, text=self.gb.board[0][1], font = ("Arial", 10), height=6, width = 6, command=lambda: self.click2())
        self.b2.place(x=70, y=10)
        self.b3 = Button(self.root, text=self.gb.board[0][2], font = ("Arial", 10), height=6, width = 6, command=lambda: self.click3())
        self.b3.place(x=140, y=10)


        self.b4 = Button(self.root, text=gb.board[1][0], font = ("Arial", 10), height=6, width = 6, command=lambda: self.click4())
        self.b4.place(x=0, y=80)
        self.b5 = Button(self.root, text=gb.board[1][1], font = ("Arial", 10), height=6, width = 6, command=lambda: self.click5())
        self.b5.place(x=70, y=80)
        self.b6 = Button(self.root, text=gb.board[1][2], font = ("Arial", 10), height=6, width = 6, command=lambda: self.click6())
        self.b6.place(x=140, y=80)

        self.b7 = Button(self.root, text=gb.board[2][0], font = ("Arial", 10), height=6, width = 6, command=lambda: self.click7())
        self.b7.place(x=0, y=150)
        self.b8 = Button(self.root, text=gb.board[2][1], font = ("Arial", 10), height=6, width = 6, command=lambda: self.click8())
        self.b8.place(x=70, y=150)
        self.b9 = Button(self.root, text=gb.board[2][2], font = ("Arial", 10), height=6, width = 6, command=lambda: self.click9())
        self.b9.place(x=140, y=150)

    def updateGameBoard(self, user):
            
        if user == '1':
            self.gb.board[0][0] = 'X'
            self.b1['text'] = 'X'
            self.gb.turn += 1 
        elif user == '2':
            self.gb.board[0][1] = 'X'
            self.b2['text'] = 'X'
            self.gb.turn += 1 
        elif user == '3':
            self.gb.board[0][2] = 'X'
            self.b3['text'] = 'X'
            self.gb.turn += 1 
        elif user == '4':
            self.gb.board[1][0] = 'X'
            self.b4['text'] = 'X'
            self.gb.turn += 1 
        elif user == '5':
            self.gb.board[1][1] = 'X'
            self.b5['text'] = 'X'
            self.gb.turn += 1 
        elif user == '6':
            self.gb.board[1][2] = 'X'
            self.b6['text'] = 'X'
            self.gb.turn += 1 
        elif user == '7':
            self.gb.board[2][0] = 'X'
            self.b7['text'] = 'X'
            self.gb.turn += 1 
        elif user == '8':
            self.gb.board[2][1] = 'X'
            self.b8['text'] = 'X'
            self.gb.turn += 1 
        elif user == '9':
            self.gb.board[2][2] = 'X'
            self.b9['text'] = 'X'
            self.gb.turn += 1 
            
    def create_thread(self):
        print('hello')
        thread = threading.Thread(target=self.setup)
        thread.daemon = True
        thread.start()

        


    def setup(self):
        '''setups up connection (via bind, listen, accept)'''
        self.socket.bind((self.host, self.port))
        self.socket.listen(0)
        self.conn, self.addr = self.socket.accept()
        print("Connected")
        self.recieve_loop()

            


    def display(self):
        label = Label(self.root, text=("Make a move:", self.gb.namePlayer1))
        label.place(x=240, y=230)
        if self.gb.turn % 2 == 0:
            label['text'] = ("Make a move:", self.gb.namePlayer1)
        else:
            label['text'] = ("Make a move:", self.gb.namePlayer2)   

    def Quit(self):
        MsgBox = messagebox.askquestion ('Play again','Do you want to quit?',icon = 'info')
        if MsgBox == 'yes':
            self.root.destroy()
        else:
            pass

    def button(self):
        ttk.Button(
            self.root,
            text='Quit',
            command=self.Quit).place(x=0, y=230)

    def askname1(self):
        name = askstring('Name', 'What is Player 1 name?')
        self.gb.namePlayer1 = name

    def askname2(self):
        name = askstring('Name', 'What is Player 2 name?')
        self.gb.namePlayer2 = name


    def reset(self):
        self.gb.turn = 0
        self.display()
        self.gb.board[0][0] = " "
        self.gb.board[0][1] = " "
        self.gb.board[0][2] = " "

        self.gb.board[1][0] = " "
        self.gb.board[1][1] = " "
        self.gb.board[1][2] = " "

        self.gb.board[2][0] = " "
        self.gb.board[2][1] = " "
        self.gb.board[2][2] = " "
        
        self.b1['text'] = " "
        self.b2['text'] = " "
        self.b3['text'] = " "
        self.b4['text'] = " "
        self.b5['text'] = " "
        self.b6['text'] = " "
        self.b7['text'] = " "
        self.b8['text'] = " "
        self.b9['text'] = " "

        print(self.gb.board)
        print(self.gb.turn)

        self.b1.config(state=NORMAL)
        self.b2.config(state=NORMAL)
        self.b3.config(state=NORMAL)

        self.b4.config(state=NORMAL)
        self.b5.config(state=NORMAL)
        self.b6.config(state=NORMAL)

        self.b7.config(state=NORMAL)
        self.b8.config(state=NORMAL)
        self.b9.config(state=NORMAL)
        
    def disableboard(self):
        self.b1.config(state=DISABLED)
        self.b2.config(state=DISABLED)
        self.b3.config(state=DISABLED)

        self.b4.config(state=DISABLED)
        self.b5.config(state=DISABLED)
        self.b6.config(state=DISABLED)

        self.b7.config(state=DISABLED)
        self.b8.config(state=DISABLED)
        self.b9.config(state=DISABLED)

    def playAgain(self):
        self.gb.updateGamesPlayed()
        MsgBox = messagebox.askquestion ('Play again','Do you want to play again?',icon = 'info')
        if self.gb.turn % 2 == 0:
            self.gb.lastPlayer = self.gb.namePlayer2
        elif self.gb.turn % 2 != 0:
            self.gb.lastPlayer = self.gb.namePlayer1
        if MsgBox == 'yes':
           self.reset()
        else:
            messagebox.showinfo('Return','Thanks for playing' + '\n' + 'Player1 Name:' + self.gb.namePlayer1 + '\n' + 'Player with the last move:' + self.gb.lastPlayer + '\n' +  'Player2 Name:' + self.gb.namePlayer2
                                + '\n' + 'Games played:' + str(self.gb.games) + '\n' + self.gb.namePlayer1 + ' Wins:' + str(self.gb.player1wins) + '\n' + self.gb.namePlayer2 + ' Wins:' + str(self.gb.player2wins) + '\n'
                                 + self.gb.namePlayer1 + " losses:" + str(self.gb.player1losses) + '\n' + self.gb.namePlayer2 + " losses:" + str(self.gb.player2losses) + '\n' + 'Games tied:' + str(self.gb.ties))
            self.root.destroy()
    def recieve_loop(self):
        '''primary socket thread loop'''
        while True:
            self.socket_input = self.conn.recv(RECV_SIZE).decode()
            self.updateGameBoard(self.socket_input)
            if self.gb.isWinner(self.gb.turn) == False:
                    messagebox.showinfo("TC", "Win X!")
                    self.disableboard()
                    self.playAgain()
            elif self.gb.Boardfull(self.gb.turn) == False:
                    self.display()
                    messagebox.showinfo("TC", "TIE!")
                    self.disableboard()
                    self.playAgain()
          
    def click1(self):
        print(self.gb.board)
        print(self.gb.turn)
        if self.gb.turn % 2 != 0  and self.gb.board[0][0] == ' ':
            self.gb.turn += 1
            self.display()
            self.gb.board[0][0] = self.gb.player2
            self.b1['text'] = self.gb.board[0][0]
            data = '1'
            self.conn.sendall(data.encode())
            if self.gb.isWinner(self.gb.turn) == False:
                messagebox.showinfo("TC", "Win O!")
                self.disableboard()
                self.playAgain()
            elif self.gb.Boardfull(self.gb.turn) == False:
                self.display()
                messagebox.showinfo("TC", "TIE!")
                self.disableboard()
                self.playAgain()
        elif self.gb.turn % 2 == 0:
            messagebox.showerror("Move", "Not your turn")
        else:
            messagebox.showerror("Move", "Choose a different location")
        

    def click2(self):
        if self.gb.turn % 2 != 0  and self.gb.board[0][1] == ' ':
            self.gb.turn += 1
            self.display()
            self.gb.board[0][1] = self.gb.player2
            self.b2['text'] = self.gb.board[0][1]
            data = '2'
            self.conn.sendall(data.encode())
            if self.gb.isWinner(self.gb.turn) == False:
                messagebox.showinfo("TC", "Win O!")
                self.disableboard()
                self.playAgain()
            elif self.gb.Boardfull(self.gb.turn) == False:
                messagebox.showinfo("TC", "TIE!")
                self.disableboard()
                self.playAgain()
        elif self.gb.turn % 2 == 0:
            messagebox.showerror("Move", "Not your turn")
        else:
            messagebox.showerror("Move", "Choose a different location")

    def click3(self):
        if self.gb.turn % 2 != 0  and self.gb.board[0][2] == ' ':
            self.gb.turn += 1
            self.display()
            data = '3'
            self.conn.sendall(data.encode())
            self.gb.board[0][2] = self.gb.player2
            self.b3['text'] = self.gb.board[0][2]
            if self.gb.isWinner(self.gb.turn) == False:
                messagebox.showinfo("TC", "Win O!")
                self.disableboard()
                self.playAgain()
            elif self.gb.Boardfull(self.gb.turn) == False:
                messagebox.showinfo("TC", "TIE!")
                self.disableboard()
                self.playAgain()
        elif self.gb.turn % 2 == 0:
            messagebox.showerror("Move", "Not your turn")
        else:
            messagebox.showerror("Move", "Choose a different location")


    def click4(self):
        if self.gb.turn % 2 != 0  and self.gb.board[1][0] == ' ':
            self.gb.turn += 1
            self.display()
            data = '4'
            self.conn.sendall(data.encode())
            self.gb.board[1][0] = self.gb.player2
            self.b4['text'] = self.gb.board[1][0]
            if self.gb.isWinner(self.gb.turn) == False:
                messagebox.showinfo("TC", "Win O!")
                self.disableboard()
                self.playAgain()
            elif self.gb.Boardfull(self.gb.turn) == False:
                messagebox.showinfo("TC", "TIE!")
                self.disableboard()
                self.playAgain()
        elif self.gb.turn % 2 == 0:
            messagebox.showerror("Move", "Not your turn")
        else:
            messagebox.showerror("Move", "Choose a different location")
        

    def click5(self):
        if self.gb.turn % 2 != 0  and self.gb.board[1][1] == ' ':
            self.gb.turn += 1
            self.display()
            data = '5'
            self.conn.sendall(data.encode())
            self.gb.board[1][1] = self.gb.player2
            self.b5['text'] = self.gb.board[1][1]
            if self.gb.isWinner(self.gb.turn) == False:
                messagebox.showinfo("TC", "Win O!")
                self.disableboard()
                self.playAgain()
            elif self.gb.Boardfull(self.gb.turn) == False:
                messagebox.showinfo("TC", "TIE!")
                self.disableboard()
                self.playAgain()
        elif self.gb.turn % 2 == 0:
            messagebox.showerror("Move", "Not your turn")
        elif self.gb.turn % 2 == 0:
            messagebox.showerror("Move", "Not your turn")
        else:
            messagebox.showerror("Move", "Choose a different location")

    def click6(self):
        if self.gb.turn % 2 != 0  and self.gb.board[1][2] == ' ':
            self.gb.turn += 1
            self.display()
            data = '6'
            self.conn.sendall(data.encode())
            self.gb.board[1][2] = self.gb.player2
            self.b6['text'] = self.gb.board[1][2]
            if self.gb.isWinner(self.gb.turn) == False:
                messagebox.showinfo("TC", "Win O!")
                self.disableboard()
                self.playAgain()
            elif self.gb.Boardfull(self.gb.turn) == False:
                messagebox.showinfo("TC", "TIE!")
                self.disableboard()
                self.playAgain()
        elif self.gb.turn % 2 == 0:
            messagebox.showerror("Move", "Not your turn")
        else:
            messagebox.showerror("Move", "Choose a different location")

    def click7(self):
        if self.gb.turn % 2 != 0  and self.gb.board[2][0] == ' ':
            self.gb.turn += 1
            self.display()
            data = '7'
            self.conn.sendall(data.encode())
            self.gb.board[2][0] = self.gb.player2
            self.b7['text'] = self.gb.board[2][0]
            if self.gb.isWinner(self.gb.turn) == False:
                messagebox.showinfo("TC", "Win O!")
                self.disableboard()
                self.playAgain()
            elif self.gb.Boardfull(self.gb.turn) == False:
                messagebox.showinfo("TC", "TIE!")
                self.disableboard()
                self.playAgain()

        elif self.gb.turn % 2 == 0:
            messagebox.showerror("Move", "Not your turn")
        else:
            messagebox.showerror("Move", "Choose a different location")

    def click8(self):
        if self.gb.turn % 2 != 0  and self.gb.board[2][1] == ' ':
            self.gb.turn += 1
            self.display()
            data = '8'
            self.conn.sendall(data.encode())
            self.gb.board[2][1] = self.gb.player2
            self.b8['text'] = self.gb.board[2][1]
            if self.gb.isWinner(self.gb.turn) == False:
                messagebox.showinfo("TC", "Win O!")
                self.disableboard()
                self.playAgain()
            elif self.gb.Boardfull(self.gb.turn) == False:
                messagebox.showinfo("TC", "TIE!")
                self.disableboard()
                self.playAgain()
        elif self.gb.turn % 2 == 0:
            messagebox.showerror("Move", "Not your turn")
        else:
            messagebox.showerror("Move", "Choose a different location")

    def click9(self):
        if self.gb.turn % 2 != 0  and self.gb.board[2][2] == ' ':
            self.gb.turn += 1
            self.display()
            data = '9'
            self.conn.sendall(data.encode())
            self.gb.board[2][2] = self.gb.player2
            self.b9['text'] = self.gb.board[2][2]
            if self.gb.isWinner(self.gb.turn) == False:
                messagebox.showinfo("TC", "Win O!")
                self.disableboard()
                self.playAgain()
            elif self.gb.Boardfull(self.gb.turn) == False:
                messagebox.showinfo("TC", "TIE!")
                self.disableboard()
                self.playAgain()
        elif self.gb.turn % 2 == 0:
            messagebox.showerror("Move", "Not your turn")
        else:
            messagebox.showerror("Move", "Choose a different location")

    def run(self):
        self.create_thread()
        self.askname1()
        self.askname2()
        self.display()
        self.button()
        self.root.mainloop()
       

if __name__ == "__main__":
    w = gui(HOST,PORT)
    w.run()

