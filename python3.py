import tinker as tk 
from tinker import strftime


window = tk.Tk()
label = t.Label(window,
				text=strftime("%H:%M:%S"),
				font=("Tahoma", 100))
				
def refresh():
	label.config(text=strftime("%H:%M:%S"))
	
button = tk.Button(window,
					text="Odśwież",
					commaand=refresh,
					font=("Tahoma", 36))

label.pack(side=tk.TOP)
button.pack(side=th.BOTTOM)
tk.mainloop()