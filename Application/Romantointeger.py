import tkinter as tk


def calculte_number(s):

    between = []
    for i in range(len(s)):
        if s[i] == 'I':
            between.append(1)
        if s[i] == 'V':
            between.append(5)
        if s[i] == 'X':
            between.append(10)
        if s[i] == 'L':
            between.append(50)
        if s[i] == 'C':
            between.append(100)
        if s[i] == 'D':
            between.append(500)
        if s[i] == 'M':
            between.append(1000)

    result = 0
    chek = False

    for i in range(len(between)):
        if chek:
            chek = False
            continue
        if i < len(between)-1:
            if between[i] < between[i+1]:
                result  += (between[i+1] - between[i])
                chek = True
            else:
                result += between[i]
        else:
            result += between[i]


    
    result_label.config(text=f'Результат: {result}')


s = []

# Функция, которая управляет кнопками и добавляет буквы
def plus_letter(letter):
    s = []
    if letter == "I": 
        s.append(entry.get())
        s.append('I')
    if letter == "V": 
        s.append(entry.get())
        s.append('V')
    if letter == "X": 
        s.append(entry.get())
        s.append('X')
    if letter == "L": 
        s.append(entry.get())
        s.append('L')
    if letter == "C": 
        s.append(entry.get())
        s.append('C')
    if letter == "D": 
        s.append(entry.get())
        s.append('D')
    if letter == "M": 
        s.append(entry.get())
        s.append('M')
        
    stroka = ''
    for i in range(len(s)):
        stroka += s[i]
    entry.delete(0, tk.END)
    entry.insert(0, str(stroka))

def clear_entry():
    entry.delete(0, tk.END)







root = tk.Tk()
root.title("Калькулятор римских чисел")
root.geometry("600x600")

entry_style = {
    'width': 50,
    'font': ('Arial', 14),
    'fg': '#333333',
    'borderwidth': 2,
    'relief': 'solid'
}


entry = tk.Entry(root,entry_style)
entry.pack(padx=30 ,pady=30)

# Здесь мы создаем кнопку рассчитать, которая берет значение из поля выше
calculte_button = tk.Button(root, text="Посчитать", font=("Arial", 14), width=10,
                            command=lambda:calculte_number(entry.get()))
calculte_button.place(x=400,y=100)


result_label = tk.Label(root, text="Результат: ", font=("Arial", 14))
result_label.place(x=100,y=100)

result_label1 = tk.Label(root, text="Пусть Паша мне напишет, что Ваня ему это показал.\n Чтобы Паша не думал, что мы занимаемся развращением! ", font=("Arial", 10))
result_label1.place(x=100,y=350)

button1 = tk.Button(root, text="I", font=("Arial", 14), width=3,
                            command=lambda:plus_letter('I'))
button1.place(x=100,y=170)
button2 = tk.Button(root, text="V", font=("Arial", 14), width=3,
                            command=lambda:plus_letter('V'))
button2.place(x=150,y=170)
button3 = tk.Button(root, text="X", font=("Arial", 14), width=3,
                            command=lambda:plus_letter('X'))
button3.place(x=200,y=170)
button4 = tk.Button(root, text="L", font=("Arial", 14), width=3,
                            command=lambda:plus_letter('L'))
button4.place(x=250,y=170)
button5 = tk.Button(root, text="C", font=("Arial", 14), width=3,
                            command=lambda:plus_letter('C'))
button5.place(x=300,y=170)
button6 = tk.Button(root, text="D", font=("Arial", 14), width=3,
                            command=lambda:plus_letter('D'))
button6.place(x=350,y=170)
button7 = tk.Button(root, text="M", font=("Arial", 14), width=3,
                            command=lambda:plus_letter('M'))
button7.place(x=400,y=170)


clear_button = tk.Button(root, text="Очистить", font=("Arial", 14), width=10,
                            command=lambda:clear_entry())
clear_button.pack(padx=30 ,pady=140)





root.mainloop()
