import tkinter as tk
from tkinter import ttk
from scrape import WebScrapeSpider
import pandas as pd
from scrapy.crawler import CrawlerProcess

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Web Scrape")
        self.geometry("800x600")

        self.url_label = tk.Label(self, text="Enter URL:")
        self.url_label.pack()

        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack()

        self.scrape_button = tk.Button(self, text="Scrape", command=self.scrape)
        self.scrape_button.pack()

        self.tree = ttk.Treeview(self)
        self.tree.pack(fill="both", expand=True)

    def scrape(self):
        url = self.url_entry.get()
        process = CrawlerProcess()
        process.crawl(WebScrapeSpider, url=url)
        process.start()
        df = pd.read_csv('data.csv')

        self.tree.delete(*self.tree.get_children())
        self.tree['columns'] = list(df.columns)

        for column in self.tree['columns']:
            self.tree.column(column, anchor="w")
            self.tree.heading(column, text=column)

        for index, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

if __name__ == "__main__":
    app = App()
    app.mainloop()