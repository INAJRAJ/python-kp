import tkinter as tk


def write_slogan(T,t):
    t.insert(tk.END,'\n')
    t.insert(tk.END,T.get(1.0, tk.END))
    
    t.insert(tk.END,"just typing something")
    t.tag_add("BOLD",)
    T.delete(1.0, tk.END)
   

top = tk.Tk()
# Code to add widgets will go here...
w = tk.Label(top, text="Hello Tkinter!")
w.pack()

frame1 = tk.Frame(top)
frame1.pack(side=tk.TOP, padx=5, pady=5)



S = tk.Scrollbar(frame1)
T = tk.Text(frame1, height=14, width=50)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)

frame2 = tk.Frame(top)
frame2.pack(side=tk.TOP)
t2 = tk.Text(frame2, height=3, width=50)
t2.pack(side=tk.BOTTOM,fill=tk.Y, padx=5, pady=5 )

frame = tk.Frame(top)
frame.pack(side=tk.BOTTOM)

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Add",
                   command=lambda : write_slogan(t2,T))
slogan.pack(side=tk.BOTTOM)






top.mainloop()


