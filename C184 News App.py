from tkinter import *
import requests
import json

root=Tk()
root.overrideredirect(True)
root.title("My News App")
root.geometry("900x600")

title = Label(root, text="BBC News Update", font=("Ink Free", 25, "bold"))
title.place(relx=0.5,rely=.1,anchor=CENTER)

news1 = Label(root, text="Title 1: ", fg = "red", wraplength=500, justify=LEFT,font=("Ink Free", 20))
news1.place(relx=0.1,rely=0.2,anchor=W)
news_desc1 = Label(root, text="Description: ", wraplength=700, justify=LEFT,font=("Ink Free", 10))
news_desc1.place(relx=0.1,rely=0.25)

news2 = Label(root, text="Title 2: ", fg = "red", wraplength=500, justify=LEFT,font=("Ink Free", 20))
news2.place(relx=0.1,rely=0.35,anchor=W)
news_desc2 = Label(root, text="Description: ", wraplength=700, justify=LEFT,font=("Ink Free", 10))
news_desc2.place(relx=0.1,rely=0.4)

news3 = Label(root, text="Title 3: ", fg = "red", wraplength=500, justify=LEFT,font=("Ink Free", 20))
news3.place(relx=0.1,rely=0.5,anchor=W)
news_desc3 = Label(root, text="Description: ", wraplength=700, justify=LEFT,font=("Ink Free", 10))
news_desc3.place(relx=0.1,rely=0.55)

news4 = Label(root, text="Title 4 ", fg = "red", wraplength=500, justify=LEFT,font=("Ink Free", 20))
news4.place(relx=0.1,rely=0.65,anchor=W)
news_desc4 = Label(root, text="Description: ", wraplength=700, justify=LEFT,font=("Ink Free", 10))
news_desc4.place(relx=0.1,rely=0.7)

news5 = Label(root, text="Title 5: ", fg = "red", wraplength=500, justify=LEFT,font=("Ink Free", 20))
news5.place(relx=0.1,rely=0.8,anchor=W)
news_desc5 = Label(root, text="Description: ", wraplength=700, justify=LEFT,font=("Ink Free", 10))
news_desc5.place(relx=0.1,rely=0.85)


api_request = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=488948909d0445de8ccce4c389adb00e")
open_bbc_page = json.loads(api_request.content)
title1 = open_bbc_page['articles'][0]['title']
desc1 = open_bbc_page['articles'][0]['description']
title2 = open_bbc_page['articles'][1]['title']
desc2 = open_bbc_page['articles'][1]['description']
title3 = open_bbc_page['articles'][2]['title']
desc3 = open_bbc_page['articles'][2]['description']
title4 = open_bbc_page['articles'][3]['title']
desc4 = open_bbc_page['articles'][3]['description']
title5 = open_bbc_page['articles'][4]['title']
desc5 = open_bbc_page['articles'][4]['description']
news1["text"] = title1
news_desc1["text"] = desc1
news2["text"] = title2
news_desc2["text"] = desc2
news3["text"] = title3
news_desc3["text"] = desc3
news4["text"] = title4
news_desc4["text"] = desc4
news5["text"] = title5
news_desc5["text"] = desc5

root.mainloop()