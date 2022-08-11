import requests
import tkinter as tk

def get_news():
    API = "d23e8121015a45518cd7bc5850d0b1d7"
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + API
    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = ""

    for articles in articles:
        my_articles.append(articles["title"])

    for i in range(10):
        my_news += my_articles[i] + "\n"

    label.config(text=my_news)
    #print(my_news)

canvas = tk.Tk()
canvas.geometry("1080x720")
canvas.title("News App")

button = tk.Button(canvas, font = 30, text="Get News", command=get_news)
button.pack(pady = 20)

label = tk.Label(canvas, font = 30, text="News:", justify = "center", wraplength = 1000, anchor = "center", bg = "light blue")
label.pack(pady = 20)

get_news()

canvas.mainloop()
