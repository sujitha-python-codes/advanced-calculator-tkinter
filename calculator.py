import tkinter as tk
import math

root=tk.Tk()
root.title("Calculator")
root.geometry("340x540")
root.config(bg="#E3F2FD")

equation_text=''
equation_label = tk.StringVar()

label = tk.Label(root,                
                 textvariable = equation_label,
                 font =("Segoe UI", 18, "bold"),
                 anchor='e',
                 height=2)
label.pack(fill="x", padx=8, pady=8, ipady=12)

frame=tk.Frame(root,bg='#E3F2FD')
frame.pack(expand=True, fill="both")

symbols = [
    ["%", "CE", "C", "⌫"],
    ["1/x", "x²", "√x", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["+/-", "0", ".", "="]
    ]

def click(v):
    
    global equation_text
    
    if v== 'C':
        equation_label.set('')
        equation_text = ""
        
    elif v == '=':
        try :
            result = str(eval(equation_text))
            equation_label.set(result)
            equation_text = result
        except SyntaxError :
            equation_label.set("Syntax Error")
            equation_text = ''
        except ZeroDivisionError :
            equation_label.set("Arithmetic Error")
            equation_text =''
        
    elif v == '%':
        try:
            equation_text = str(float(equation_text)/100)
            equation_label.set(equation_text)
        except :
            equation_label.set("Error")
            equation_text = ''
    
    elif v == 'CE':
        equation_label.set("")
        equation_text =''
            
    elif v== '⌫' :
        equation_text = equation_text [:-1]
        equation_label.set(equation_text )
        
    elif v == 'x²':
        try:
            value = eval(equation_text)
            equation_text = str(value ** 2)
            equation_label.set(equation_text)
        except:
            equation_label.set("Error")
            equation_text = ''        
    elif v == '√x':
        try:
            equation_text = str(math.sqrt(float(equation_text)))
            equation_label.set(equation_text)
        except:
            equation_label.set("Error")
            equation_text = ''
        
    elif v == '1/x':
        try:
            value = eval(equation_text)
            equation_text = str(1/value)
            equation_label.set(equation_text)
        except ZeroDivisionError :
            equation_label.set("Arithmetic Error")
            equation_text =''
        except:
            equation_label.set("Error")
            equation_text = ''
            
    elif v == '+/-' :
        try:
            value = -eval(equation_text)
            equation_text = str(value)
            equation_label.set(equation_text)
        except :
            equation_label.set("Error")
            equation_text=''
                               
    else:
        equation_text += str(v)
        equation_label.set(equation_text)
    
#-----Creating buttons-----           
for i in range(6):
    frame.grid_rowconfigure(i, weight=1)

for j in range(4):
    frame.grid_columnconfigure(j, weight=1)

for i in range(6):
    for j in range(4):
        tk.Button(frame,
                  text=symbols[i][j],
                  font =("Segoe UI" ,14,'bold'),
                  command=lambda v =symbols[i][j]:click(v),
                  bg='white',
                  fg='black'
                 ).grid(row=i,
                       column=j,
                       pady=3,
                       padx=3,
                       sticky = 'nsew')
              
root.mainloop()