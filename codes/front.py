from tkinter import *
from tkinter import ttk
import PIL
from PIL import ImageGrab
from tensorflow.keras.models import load_model
import ctypes
import numpy as np

# My own codes import
import directory
import predict
import normalize_image as ni

color1 = 'white'
color2 = 'BLACK'

# English alphabet mapping
english_alphabet = {i: chr(65 + i) for i in range(26)}

class gui:   
    
    
    def __init__(self, info):
        
        self.info = info
        self.root = Tk()
        self.root.title(self.info['name'])
        self.root.geometry('600x500')
        self.root.resizable(width=False, height=False) # user cant resize window
    
        self.main_frame = Frame(self.root, bg=color2, pady=40)
        self.main_frame.place(relwidth=1, relheight=1)
        
        # Create a Notebook widget (tab control)
        self.tab_control = ttk.Notebook(self.root)

        # Create tabs
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        
        style = ttk.Style()
        style.configure("Custom.TFrame", background=color2)  # Set the desired background color

        # Create the frame using the custom style
        self.tab1 = ttk.Frame(self.tab_control, style="Custom.TFrame")
        self.tab_control.add(self.tab1, text="Tab 1")
        self.tab_control.add(self.tab2, text="Tab 2")

        L1 = Label(self.tab1, text="Handwritten Prediction project", font=('Arial', 16, 'bold'), fg=color1 , bg=color2) 
        L1.place(x=108, y=10) 
        
        L2 = Label(self.tab1, text="-"*79, font=('Arial', 16), fg=color1 , bg=color2) 
        L2.place(x=21, y=38) 
        
        L3 = Label(self.tab1, text="----------------------------", font=('Arial', 16), fg=color1 , bg=color2) 
        L3.place(x=370, y=155) 
                
        t1 = Label(self.tab1, text="_"*25, font=('Arial', 16), fg=color1 , bg=color2, bd=0, highlightthickness=0,) 
        t1.place(x=26.5, y=55)
        
        t2 = Label(self.tab1, text=("|"+' '*50+'|'+'\n')*13, font=('Arial', 16), fg=color1 , bg=color2, bd=0, highlightthickness=0,) 
        t2.place(x=23, y=78)
        
        t3 = Label(self.tab1, text="_"*25, font=('Arial', 16), fg=color1 , bg=color2, bd=0, highlightthickness=0,) 
        t3.place(x=26.5, y=365)
        
        self.cv = Canvas(self.tab1, width=300, height=300, bg=color2, bd=0, highlightthickness=0, relief='ridge')
        self.cv.place(x=30,y=85)
        
        self.cv.bind('<Button-1>', self.event_activation) #start to draw when user left click with mouse
        self.drawing_complete = False
        self.cv.bind('<ButtonRelease-1>', lambda event: self.center_drawing())
        
        L5 = Label(self.tab1, text="-"*79, font=('Arial', 16), fg=color1 , bg=color2) 
        L5.place(x=21, y=405) 
        
        self.L6 = Label(self.tab1, text="Prediction is: ---", font=('Arial', 16), fg=color1 , bg=color2) 
        self.L6.place(x=165, y=430)    
        
        self.tab_control.pack(expand=1, fill="both")
    #==================================================================================
    
    def start(self):
    
        button1 = self.button("1. PREDICTION", self.save_image)
        button2 = self.button("2. Erase board", self.clear_cv)
        
        button1.place(x=370,y=80)
        button2.place(x=370,y=198)
        
        self.model = load_model(self.info['h5'])
        
        self.root.mainloop()
        

    #==================================================================================
    #button make section
    #==================================================================================
    
    def button(self, text="", comand=None):
        
        temp = Button(
                self.tab1,
                background=color2,
                foreground=color1,
                width=15,
                height=2,
                cursor='hand2',
                text=text,
                font=('Arial', 16, 'bold'),
                command=comand,)
        
        return temp
        
       
    #==================================================================================
    # drawing section
    #==================================================================================
    
    def event_activation(self,event): 
        self.lastx, self.lasty = event.x, event.y # hold cordinante of place that mouse clicked on it
        self.cv.bind('<B1-Motion>', self.draw_on_canvas) 

    #==================================================================================
        
    def draw_on_canvas(self, event):
        x, y = event.x, event.y
        # Add a tag 'drawing' to each line
        self.cv.create_line((self.lastx, self.lasty, x, y), width=25, fill=color1, capstyle=ROUND, smooth=TRUE, splinesteps=100, tags='drawing')
        self.lastx, self.lasty = x, y


    #==================================================================================
    
    # Clears the canvas 
    def clear_cv(self): 
        self.cv.delete("all") 
        self.drawing_complete = False
        self.make_lable("Prediction is: ---")

    #==================================================================================
    
    def center_drawing(self):
        if not self.drawing_complete:
            return  # Do not center if the drawing is not complete
        
        self.check_save = True  #make saving new image possible
        
        ctypes.windll.user32.SetProcessDPIAware()
        # Get the bounding box of all items with the tag 'drawing'
        bbox = self.cv.bbox('drawing')
        if not bbox:  # Check if the bounding box is not None
            return

        # Calculate the center of the canvas
        canvas_center_x = self.cv.winfo_width() / 2
        canvas_center_y = self.cv.winfo_height() / 2

        # Calculate the center of the bounding box
        bbox_center_x = (bbox[0] + bbox[2]) / 2
        bbox_center_y = (bbox[1] + bbox[3]) / 2

        # Calculate the offset needed to center the drawing
        x_offset = canvas_center_x - bbox_center_x
        y_offset = canvas_center_y - bbox_center_y

        # Move all items with the tag 'drawing' to the center of the canvas
        self.cv.move('drawing', x_offset, y_offset)

    
    #==================================================================================
    
    def make_lable(self, newtext=''):
        self.L6.config(text=newtext)
        
    #==================================================================================
    # prediction section
    #==================================================================================

    def save_image(self):
        try:
            if self.table == True:
                self.tree.destroy()
        except:
            pass
        # Make the application DPI aware
        ctypes.windll.user32.SetProcessDPIAware()
        
        self.drawing_complete = True
        self.center_drawing()
        self.cv.update()

        # Calculate the coordinates without scaling
        x = self.tab1.winfo_rootx() + self.cv.winfo_x()
        y = self.tab1.winfo_rooty() + self.cv.winfo_y()
        x1 = x + self.cv.winfo_width()
        y1 = y + self.cv.winfo_height()

        # Grab the image and resize
        self.img = ImageGrab.grab(bbox=(x, y, x1, y1)).resize((28, 28), PIL.Image.LANCZOS)
        
        self.predict(self.model)

    #==================================================================================
    def predict(self, model):
        
        self.img_temp = ni.main(self.img)
        self.number = predict.find(self.img_temp, model)
        
        self.make_lable(f"Prediction is: {english_alphabet[self.number[0]]}") 
        
        self.percentage(self.number)
        self.drawing_complete = False
                 
    #==================================================================================
    def percentage(self, number):
        self.table = True
        percentages = []
        
        l = list(english_alphabet.values())
        for i in range(26):
            percentages.append((l[i],number[1][i]))
        
        style = ttk.Style(self.tab2)
        
        style.configure("Treeview",
            background=color2,
            fieldbackground=color2,
            font=("Arial", 12, "bold"), 
        )

        style.map("Treeview",
            background=[('selected', color2)]
        )

        self.tree = ttk.Treeview(self.tab2, columns=("1.Class", "2.Value", "3.Class", "4.Value"), show="headings", style="Treeview")
        
        self.tree.column("1.Class", width=110)
        self.tree.column("2.Value", width=110)
        self.tree.column("3.Class", width=110)
        self.tree.column("4.Value", width=110)
        
        self.tree.heading("1.Class", text="Class")
        self.tree.heading("2.Value", text="Value")
        self.tree.heading("3.Class", text="Class")
        self.tree.heading("4.Value", text="Value")
        
        self.tree.tag_configure('evenrow', background='white')
        self.tree.tag_configure('oddrow', background='lightblue')
        
        for i in range(0,len(percentages)//2):
            row_values = percentages[i] + percentages[len(percentages)//2+i]
            if i % 2 == 0:
                self.tree.insert("", "end", values=row_values, tags=("oddrow",))
            else:
                self.tree.insert("", "end", values=row_values, tags=("evenrow",))
        
        for col in ("1.Class", "2.Value", "3.Class", "4.Value"):
            self.tree.column(col, anchor='center')
        
        # Pack the Treeview
        self.tree.pack(fill="both", expand=True, pady=40, anchor=E)