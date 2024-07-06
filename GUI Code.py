#Libraries
import tkinter as tk
from PIL import Image, ImageTk

##Functions

#List of Fonts 
arial_large = ('Arial', 28)

# Function to load and display the image
def load_and_display_image(root, image_path, scale_factor):
    # Open an image file from the file path specified later
    image = Image.open(image_path)

    # Scale the image
    new_width = int(image.width * scale_factor)
    new_height = int(image.height * scale_factor)
    resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Convert the image to a format Tkinter can use using PIL
    tk_image = ImageTk.PhotoImage(resized_image)

    # Create a label to display the image in
    label = tk.Label(root, image=tk_image)
    label.image = tk_image  # Keep a reference to avoid garbage collection
    label.place(x = 50, y = 50)

#The command executed when the enter button is pressed
def enter_button_action():
        #Get the contents of the text box and store them into 'coordinates'
        coordinates = Coordinate_Entry.get()

        #Outputs after enter is pressed
        


##Main Code
# Create the main window which is going to be called root
root = tk.Tk()
root.geometry("1500x1000")
root.title("Coastal Map of the UK")

# Path to the image file
image_path = r"C:\Users\xarak\OneDrive\School Stuff\A-Level\Inversity Challenge\Inversity_ICLMS\UK Map2.png"

# Scale factor - 45% of the original size
scale_factor = 0.45

# Load and display the image - call the load_and_display_image function
load_and_display_image(root, image_path, scale_factor)

#Make an entry box to enter the grid reference
Coordinate_Entry = tk.Entry(root, 
                            text = "",
                            font = arial_large,
                            width = 7
                            ) 
#Place the entry box 
Coordinate_Entry.place(x = 1000, y = 55)
 
#Make a button to submit the grid reference
Enter_button = tk.Button(root,
                        text = "Enter",
                        command = enter_button_action,
                        font = arial_large)
Enter_button.place(x = 1200, y =50) 

root.mainloop()