import tkinter as tk
from PIL import Image, ImageTk

##Functions

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

def enter_action():
        coordinates = Coordinate_Entry.get()
        print("Entered coordinates:", coordinates)


##Main Code
# Create the main window which is going to be called root
root = tk.Tk()
root.geometry("1500x1000")
root.title("Coastal Map of the UK")

# Path to the image file
image_path = r"C:\Users\xarak\OneDrive\School Stuff\A-Level\Inversity Challenge\UK Map.png"

# Scale factor - 65% of the original size
scale_factor = 0.65

# Load and display the image - call the load_and_display_image function
load_and_display_image(root, image_path, scale_factor)

#Make an entry box to enter the grid reference
Coordinate_Entry = tk.Entry(root, text="") 
#Place the entry box 
Coordinate_Entry.place(x = 1000, y = 50)
 
#Make a button to submit the grid reference
Enter_button = tk.Button(root, text="Enter", command=enter_action)
Enter_button.place(x = 1200, y =50)
 
root.mainloop()