
# # from tkinter import *

# # root = Tk()
# # root.title("Connect 4 Game")
# # root.geometry("800x600")
# # root.configure(bg="#f2f2f2")  # set the background color of the root window

# # # Create a frame for the difficulty level selection
# # frame_difficulty = Frame(root, bg="#f2f2f2", padx=20, pady=20)  # set the background color of the frame
# # frame_difficulty.pack(side=LEFT, anchor=N)

# # # Add a label for the difficulty level selection
# # label_difficulty = Label(frame_difficulty, text="Select Difficulty Level:")
# # label_difficulty.pack(side=TOP, padx=10, pady=10)

# # # Add buttons for each difficulty level
# # button_easy = Button(frame_difficulty, text="Easy", padx=50, pady=10, fg="white", bg="blue")
# # button_medium = Button(frame_difficulty, text="Medium", padx=40, pady=10, fg="white", bg="blue")
# # button_hard = Button(frame_difficulty, text="Hard", padx=50, pady=10, fg="white", bg="blue")
# # button_easy.pack(side=TOP, padx=10, pady=10)
# # button_medium.pack(side=TOP, padx=10, pady=10)
# # button_hard.pack(side=TOP, padx=10, pady=10)

# # # Add a frame for the game board
# # frame_board = Frame(root, bg="#f2f2f2")
# # frame_board.pack(side=LEFT, anchor=N, padx=20, pady=20)

# # # Add the game board widgets here...

# # root.mainloop()

# from tkinter import *
# import tkinter.font as font

# root = Tk()
# root.title("Connect 4 Game")
# root.geometry("800x600")
# root.configure(bg="#2D3142")

# # Set custom font
# button_font = font.Font(family='Helvetica', size=20, weight='bold')

# # Create a container frame for the controls
# controls_frame = Frame(root, bg="#2D3142")
# controls_frame.pack(pady=50)

# # Create a label with a welcome message
# welcome_label = Label(root, text="Welcome to Connect 4", font=('Helvetica', 30, 'bold'), fg="#F5A962", bg="#2D3142")
# welcome_label.pack(pady=50)

# # Create a button to start the game
# start_button = Button(controls_frame, text="PLAY", font=button_font, padx=50, pady=10, fg="#2D3142", bg="#F5A962")
# start_button.pack(side=LEFT, padx=10)

# # Create a button to quit the game
# quit_button = Button(controls_frame, text="QUIT", font=button_font, padx=50, pady=10, fg="#2D3142", bg="#F5A962", command=root.quit)
# quit_button.pack(side=RIGHT, padx=10)

# root.mainloop()



from tkinter import *

from tkinter import font
root = Tk()
root.title("Connect 4 Game ")
root.configure(bg="#2D3142")
root.geometry("800x600")

# Set custom font
button_font = font.Font(family='Helvetica', size=20, weight='bold')

# Create a container frame for the controls
controls_frame = Frame(root, bg="#2D3142")
controls_frame.pack(pady=50)

page_4 = Label(root, text="Congratulations !", font=('Helvetica', 30, 'bold'), fg="#F5A962", bg="#2D3142")
page_4.pack(pady=50)

endGameButton = Button(controls_frame, text="End Game" , font=button_font,padx=50, pady=10,  fg="#2D3142", bg="#F5A962")
endGameButton.pack(side=LEFT,padx=10) 

root.mainloop()