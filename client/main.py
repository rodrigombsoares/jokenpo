from tkinter import *
import tkinter as tk
from tkinter import font as tkfont  # python 3
from client import Client
from client_utils import *

BUTTON_WIDTH = 25
WINDOW_GEOMETRY = "1000x600"


class Application:
    root = None

    def __init__(self, root, master=None):
        self.root = root

    # def get_image(self, choice):
    #     img_rock = PhotoImage(file="../assets/rock3.png")
    #     img_paper = PhotoImage(file="../assets/paper3.png")
    #     img_scissors = PhotoImage(file="../assets/scissors3.png")
    #     if(choice == 'p'):
    #         return tk.Label(image=img_paper)
    #     elif(choice == 'r'):
    #         return tk.Label(image=img_rock)
    #     elif(choice == 's'):
    #         return tk.Label(image=img_scissors)

    def handle_choice(self, choice):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry(WINDOW_GEOMETRY)
        client = Client(choice)
        computer_hand, winner = get_results(client.get_data())
        img_rock = PhotoImage(file="../assets/rock3.png")
        img_paper = PhotoImage(file="../assets/paper3.png")
        img_scissors = PhotoImage(file="../assets/scissors3.png")
        page_title = tk.Label(self.root, text="Pedra, papel e tesoura",)
        page_title.place(relx=0.5, rely=0.0, anchor=N)
        page_title.config(font=("Courier", 35))
        choice_title = tk.Label(self.root, text="Você escolheu:",)
        choice_title.place(relx=0.2, rely=0.3, anchor=E)
        choice_title.config(font=("Courier", 20))
        image_player = tk.Label(image=(
            img_paper if choice == "paper" else img_rock if choice == "rock" else img_scissors))
        image_player.place(relx=0.3, rely=0.3, anchor=CENTER)
        computer_choice_title = tk.Label(self.root, text="Eu escolhi:",)
        computer_choice_title.place(relx=0.2, rely=0.6, anchor=E)
        computer_choice_title.config(font=("Courier", 20))
        image_computer = tk.Label(image=(
            img_paper if computer_hand == "paper" else img_rock if computer_hand == "rock" else img_scissors))
        image_computer.place(relx=0.3, rely=0.6, anchor=CENTER)
        winner_text = tk.Label(self.root, text=(
            "Você ganhou" if winner == choice else "Eu ganhei!" if winner == computer_hand else "Empate!"))
        winner_text.place(relx=0.2, rely=0.9, anchor=E)
        winner_text.config(font=("Courier", 20))
        button_start = tk.Button(
            text="Jogar novamente", command=self.start_page, width=BUTTON_WIDTH)
        button_start.place(relx=0.4, rely=0.9, anchor=W)
        button_start = tk.Button(
            text="Sair", command=lambda: self.root.destroy(), width=BUTTON_WIDTH)
        button_start.place(relx=0.7, rely=0.9, anchor=W)
        self.root.mainloop()

    def start_page(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry(WINDOW_GEOMETRY)
        main_page_title = tk.Label(self.root, text="Pedra, papel e tesoura",)
        main_page_title.place(relx=0.5, rely=0.0, anchor=N)
        main_page_title.config(font=("Courier", 35))
        main_page_title = tk.Label(self.root, text="Escolha sua jogada",)
        main_page_title.place(relx=0.5, rely=0.2, anchor=N)
        main_page_title.config(font=("Courier", 20))
        img_rock = PhotoImage(file="../assets/rock3.png")
        img_paper = PhotoImage(file="../assets/paper3.png")
        img_scissors = PhotoImage(file="../assets/scissors3.png")
        button_rock = tk.Button(
            image=img_rock, command=lambda: self.handle_choice("rock"))
        button_rock.place(relx=0.1, rely=0.6, anchor=CENTER)
        button_paper = tk.Button(
            image=img_paper, command=lambda: self.handle_choice("paper"))
        button_paper.place(relx=0.5, rely=0.6, anchor=CENTER)
        button_scissors = tk.Button(
            image=img_scissors, command=lambda: self.handle_choice("scissors"))
        button_scissors.place(relx=0.9, rely=0.6, anchor=CENTER)
        self.root.mainloop()

    def rules_page(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.geometry("600x300")
        main_page_title = tk.Label(self.root, text="Pedra, papel e tesoura",)
        main_page_title.place(relx=0.5, rely=0.0, anchor=N)
        main_page_title.config(font=("Courier", 35))
        self.root.mainloop()
        return "rules"

    def main_screen(self):
        main_page_title = tk.Label(self.root, text="Pedra, papel e tesoura",)
        main_page_title.place(relx=0.5, rely=0.0, anchor=N)
        main_page_title.config(font=("Courier", 35))
        button_start = tk.Button(
            text="Começar Jogo", command=self.start_page, width=BUTTON_WIDTH)
        button_start.place(relx=0.5, rely=0.4, anchor=CENTER)
        button_rules = tk.Button(
            text="Regras do Jogo", command=self.rules_page, width=BUTTON_WIDTH)
        button_rules.place(relx=0.5, rely=0.6, anchor=CENTER)
        button_quit = tk.Button(text="Sair do Jogo",
                                command=self.root.destroy, width=BUTTON_WIDTH)
        button_quit.place(relx=0.5, rely=0.8, anchor=CENTER)

    def game(self):
        self.main_screen()
        self.root.mainloop()


root = tk.Tk()
root.geometry("600x300")
app = Application(root)

app.game()
