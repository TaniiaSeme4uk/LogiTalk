from customtkinter import *
from PIL import Image

class MainWin(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('700x400')
        self.title('Вхід')

        self.left_frame = CTkFrame(self)
        self.left_frame.pack(side="left", fill='both')

        img = Image.open('img/bg.png')
        img_ctk = CTkImage(light_image=img, size=(450, 400))
        self.img_label = CTkLabel(self.left_frame, image=img_ctk,
                                  text= 'Welcome', 
                                  font=("Helvetica",60,'bold'),
                                  text_color='pink')
        self.img_label.pack()

        self.right_frame = CTkFrame(self, fg_color="white")
        self.right_frame.pack()

        self.text = CTkLabel(self.right_frame, text='LogiTalk',
                             font=('Helvetica', 20, 'bold'),
                             text_color='purple')
        self.text.pack(pady=50)

        

win = MainWin()
win.mainloop()