# 1st
from tkinter import *
import tkinter.font as font

root = Tk()
root.title("Connect 4 Game")
root.geometry("800x600")
root.configure(bg="#2D3142")

# Set custom font
button_font = font.Font(family='Helvetica', size=20, weight='bold')

# Create a container frame for the controls
controls_frame = Frame(root, bg="#2D3142")
controls_frame.pack(pady=50)

# Create a label with a welcome message
page_1 = Label(root, text="Welcome to Connect 4", font=(
    'Helvetica', 30, 'bold'), fg="#F5A962", bg="#2D3142")
page_1.pack(pady=50)

# Create a button to start the game
start_button = Button(controls_frame, text="PLAY", font=button_font,
                      padx=50, pady=10, fg="#2D3142", bg="#F5A962")
start_button.pack(side=LEFT, padx=10)

# Create a button to quit the game
quit_button = Button(controls_frame, text="QUIT", font=button_font,
                     padx=50, pady=10, fg="#2D3142", bg="#F5A962", command=root.quit)
quit_button.pack(side=RIGHT, padx=10)

root.mainloop()
# 2nd

# from tkinter import *
# from tkinter import font
# import tkinter as tk
# root = tk.Tk()
# root.title("Connect 4 Game ")
# root.configure(bg="#2D3142")
# root.geometry("800x600")

# # Set custom font
# button_font = font.Font(family='Helvetica', size=20, weight='bold')
# # Create a container frame for the controls
# controls_frame = Frame(root, bg="#2D3142")
# controls_frame.pack(pady=50)

# page_2 = Label(root, text="Select the algorithm", font=('Helvetica', 30, 'bold'), fg="#F5A962", bg="#2D3142")
# page_2.pack(pady=0)

# # Create a button to start the game
# mmButton = Button(controls_frame, text="MiniMax" , font=button_font,padx=50, pady=10,  fg="#2D3142", bg="#F5A962")
# mmButton.pack(side=LEFT, padx=10)

# abButton = Button(controls_frame, text="Alpha Beta", font=button_font, padx=50, pady=10,  fg="#2D3142", bg="#F5A962")
# abButton.pack(side=RIGHT, padx=10)

# root.mainloop()

# 3rd
# from tkinter import *
# from tkinter import font
# import tkinter as tk
# root = tk.Tk()
# root.title("Connect 4 Game ")
# root.configure(bg="#2D3142")
# root.geometry("800x600")

# # Set custom font
# button_font = font.Font(family='Helvetica', size=20, weight='bold')

# # Create a container frame for the controls
# controls_frame = Frame(root, bg="#2D3142")
# controls_frame.pack(pady=50)

# page_3 = Label(root, text="Select Difficulty Level:", font=('Helvetica', 30, 'bold'), fg="#F5A962", bg="#2D3142")
# page_3.pack(pady=50)

# # Create a button to start the game
# button_easy = Button(controls_frame, text="Easy" , font=button_font,padx=50, pady=10,  fg="#2D3142", bg="#F5A962")
# button_easy.pack(side=LEFT, padx=10)

# button_medium = Button(controls_frame, text="Medium", font=button_font, padx=50, pady=10,  fg="#2D3142", bg="#F5A962")
# button_medium.pack(side=RIGHT, padx=10)

# button_hard = Button(controls_frame, text="Hard", font=button_font, padx=50, pady=10,  fg="#2D3142", bg="#F5A962")
# button_hard.pack(side=RIGHT, padx=10)

# root.mainloop()
