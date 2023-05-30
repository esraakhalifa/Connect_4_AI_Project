
import tkinter as tk
import ptest
import p2
import p3
import p4


class Connect4App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Connect 4")

        # Create a container to hold the pages
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        # Create a dictionary to store the pages
        self.pages = {}

        # Create and add pages to the dictionary
        page1 = WelcomePage(self.container, self)
        page2 = AlgorithmPage(self.container, self)
        page3 = LevelPage(self.container, self)
        page4 = CongratulationsPage(self.container, self)
        self.pages["welcome"] = ptest
        self.pages["algorithm"] = p2
        self.pages["level"] = p3
        self.pages["congratulations"] = p4

        # Show the welcome page initially
        self.show_page("welcome")

    def show_page(self, page_name):
        # Hide the current page
        current_page = self.pages.get(page_name)
        if current_page:
            current_page.tkraise()


class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Add widgets to the welcome page
        label = tk.Label(self, text="Welcome to Connect 4",
                         font=("Helvetica", 18))
        label.pack(pady=20)

        # Add buttons for play and quit
        play_button = tk.Button(
            self, text="Play", command=lambda: controller.show_page("algorithm"))
        play_button.pack(pady=10)

        quit_button = tk.Button(self, text="Quit", command=self.quit)
        quit_button.pack(pady=10)


class AlgorithmPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Add widgets to the algorithm page
        label = tk.Label(self, text="Select an Algorithm",
                         font=("Helvetica", 18))
        label.pack(pady=20)

        # Add buttons for Minmax and Alpha-Beta
        minmax_button = tk.Button(
            self, text="Minmax", command=lambda: controller.show_page("level"))
        minmax_button.pack(pady=10)

        alphabeta_button = tk.Button(
            self, text="Alpha-Beta", command=lambda: controller.show_page("level"))
        alphabeta_button.pack(pady=10)


class LevelPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Add widgets to the level page
        label = tk.Label(self, text="Select a Level", font=("Helvetica", 18))
        label.pack(pady=20)

        # Add buttons for easy, medium, and hard
        easy_button = tk.Button(
            self, text="Easy", command=lambda: controller.show_page("congratulations"))
        easy_button.pack(pady=10)

        medium_button = tk.Button(
            self, text="Medium", command=lambda: controller.show_page("congratulations"))
        medium_button.pack(pady=10)

        hard_button = tk.Button(
            self, text="Hard", command=lambda: controller.show_page("congratulations"))
        hard_button.pack(pady=10)


class CongratulationsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Add widgets to the congratulations page
        label = tk.Label(self, text="Congratulations!", font=("Helvetica", 18))
        label.pack(pady=20)

        # Add a button to end the game
        end_button = tk.Button(self, text="End Game", command=self.quit)
        end_button.pack(pady=10)


# Create an instance of the Connect4App and run the GUI
app = Connect4App()
app.mainloop()
