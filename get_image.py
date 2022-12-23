from icrawler.builtin import GoogleImageCrawler
import tkinter as tk
from threading import Thread
import os

class Google_downloader:
    def __init__(self, window):
        # window setting
        window.title('Google_downloader')
        window.geometry('400x200')
        window.resizable(0,0)
        # self.magic_number = self.new_random
        self.question = tk.Label(window, font=('Times', 11), text='ค้นหาไฟล์แล้วดาวน์โหลดจาก Google')
        self.status = tk.Label(window, font=('Times', 11))
        # Entry
        self.entry_search = tk.Entry(window)
        self.entry_search.insert(0, 'คำค้นหา')
        self.amount = tk.Entry(window)
        self.amount.insert(0, 'จำนวน')
        self.entry_search.pack()
        self.amount.pack()
        # placing widgets
        self.guess_button = tk.Button(window, text='Download', bg='green', command=self.get_image)
        self.question.place(x=20, y=20)
        self.entry_search.place(x=120, y=50)
        self.amount.place(x=120, y=80)
        self.guess_button.place(x=140, y=120)
        self.status.place(x=120, y=160)

        # init ./google_downloaded in case it doesn't exist
        root = './google_downloaded'
        if not os.path.exists(root):
            os.mkdir(root)
        else:
            # clear the folder
            for file in os.listdir(root):
                os.remove(os.path.join(root, file))

        # crawler setting
        self.google_crawler = GoogleImageCrawler(storage={'root_dir': root})

    def crawler_thread(self, keyword, max_num):
        t2 = Thread(target=self.google_crawler.crawl, args=(keyword, max_num))
        t2.start()

    def check_progress(self, max_num):
        while True:
            if len(os.listdir('./google_downloaded')) >= max_num:
                break
            self.status.config(text='กำลังดาวน์โหลด...', fg='blue')
        # finished    
        self.status.config(text='ดาวน์โหลดเสร็จสิ้น', fg='green')

    def check_progress_thread(self, max_num) -> None:
        t1 = Thread(target=self.check_progress, args=(max_num))
        t1.start()
        return
        # self.status.config(text='ดาวน์โหลดเสร็จสิ้น', fg='green')

    def get_image(self) -> None:
        # get search keyword
        search_keyword = self.entry_search.get()
        amount = self.amount.get()
        # check if there is no keyword
        if search_keyword == '' or amount.isdigit() == False:
            self.status.config(text='กรุณาใส่คำค้นหา และ จำนวน', fg='red')
            return

        # crawl
        amount = int(amount)
        # start a progress tracking thread
        self.check_progress_thread(amount)
        # self.google_crawler.crawl(keyword=search_keyword, max_num=amount)
        self.crawler_thread(search_keyword, amount)
        


window = tk.Tk()
app = Google_downloader(window)
window.mainloop()





