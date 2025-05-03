import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("My first game screen")
root.geometry("500x500")
root.configure(bg='#3A3A3A')  # Grey background using hex code

# Load and resize the image
image = Image.open("my_image.png")  # Replace with your image file
image = image.resize((300, 300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

# Create a label to hold the image and place it in the center
label = tk.Label(root, image=photo, bg='#3A3A3A')
label.place(relx=0.5, rely=0.5, anchor='center')

# Run the Tkinter loop
root.mainloop()
