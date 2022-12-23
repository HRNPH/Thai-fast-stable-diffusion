# read file in dataset
import glob
import os
import tkinter as tk
from random import randint
from PIL import Image

# root = './datasets'
# naming_rule = 'charin_polpanumas ([index]).jpg'
# file_name = os.listdir(root)
# for index in range(1, len(file_name) + 1):
#     path = os.path.join(root, file_name[index - 1])
#     # rename file
#     os.rename(path, os.path.join(root, naming_rule.replace('[index]', str(index))))


class RenamerApp:
    def __init__(self, window):
        # window setting
        window.title('Renamer')
        window.geometry('400x150')
        window.resizable(0,0)
        # self.magic_number = self.new_random
        self.question = tk.Label(window, font=('Times', 11), text='ตั้งชื่อไฟล์ใหม่(นำไฟล์ไปวางในโฟลเดอร์ datasets)')
        self.status = tk.Label(window, font=('Times', 11))
        # Entry
        self.entry_name = tk.Entry(window)
        self.entry_name.insert(0, 'คีย์เวิร์ด(ภาษาอังกฤษ)')
        self.entry_name.pack()
        # placing widgets
        self.guess_button = tk.Button(window, text='ตั้งชื่อใหม่', bg='red', command=self.rename_n_process)
        self.question.place(x=20, y=20)
        self.entry_name.place(x=120, y=50)
        self.guess_button.place(x=140, y=80)
        self.status.place(x=100, y=120)

        # init ./datasets in case it doesn't exist
        if not os.path.exists('./datasets'):
            os.mkdir('./datasets')

    def process_image(self, image_path) -> None:
        # open image
        image = Image.open(image_path)
        #use PIL to convert to RGB scale and save as jpg
        image = image.convert('RGB')
        # overwrite the image
        image.save(image_path, 'JPEG', quality=100)

    def rename_n_process(self, root='./datasets', naming_rule='data ([index]).jpg') -> None:
        get_name = self.entry_name.get()
        naming_rule = naming_rule.replace('data', get_name)
        # print(naming_rule)
        file_name = os.listdir(root)
        
        # cheeck if there is no file
        if len(file_name) == 0:
            self.status.config(text='ไม่พบไฟล์ในโฟลเดอร์', fg='red')
            return

        for index in range(1, len(file_name) + 1):
            path = os.path.join(root, file_name[index - 1])
            # process all images
            self.process_image(path)
            # rename file
            os.rename(path, os.path.join(root, naming_rule.replace('[index]', str(index))))
        
        # update result
        self.status.config(text=f'เสร็จสิ้น ทั้งหมด {len(file_name)} ไฟล์', fg='green')

window = tk.Tk()
app = RenamerApp(window)
window.mainloop()