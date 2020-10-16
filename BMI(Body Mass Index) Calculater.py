#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import messagebox


def get_height():
    '''
       This function gets height value from Entry field
    '''
    height = float(ENTRY2.get())
    return height


def get_weight():
    '''
       This function gets weight value from Entry field
    '''
    weight = float(ENTRY1.get())
    return weight


# "a" is there because the bind function gives an argument to the function....
def calculate_bmi(a=""):
    print(a)
    '''
      This function calculates the result
    '''
    ResultBMI.delete("1.0",END)
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Please enter positive height!!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid data!")
        
    else:

        if bmi <= 15.0:
            ResultBMI.insert(
                END, str(bmi) + "\nRemarks = Very severely underweight!!")
        elif 15.0 < bmi <= 16.0:
            ResultBMI.insert(
                END, str(bmi) + "\nRemarks = Severely underweight!")
        elif 16.0 < bmi < 18.5:
            ResultBMI.insert(END, str(bmi) + "\nRemarks = Underweight!")
        elif 18.5 <= bmi <= 25.0:
            ResultBMI.insert(END, str(bmi) + "\nRemarks = Normal.")
        elif 25.0 < bmi <= 30:
            ResultBMI.insert(END, str(bmi) + "\nRemarks = Overweight.")
        elif 30.0 < bmi <= 35.0:
            ResultBMI.insert(END, str(bmi) + "\nRemarks = Moderately obese!")
        elif 35.0 < bmi <= 40.0:
            ResultBMI.insert(END, str(bmi) + "\nRemarks = Severely obese!")
        else:
            ResultBMI.insert(END, str(bmi) + "\nRemarks = Super obese!!")


def iExit():
    iExit = messagebox.askyesno("Body Mass Index", "Confirm if you want to exit")
    if iExit > 0:
        window.destroy()
        return


def iReset():
    var1.set("")
    var2.set("")
    ResultBMI.delete("1.0",END)


if __name__ == '__main__':
    window = Tk()
    window.bind("<Return>", calculate_bmi)
    window.geometry("400x400")
    window.configure(background="#34495E")
    window.title("BMI(Body Mass Index) Calculator")
    window.resizable(width=False, height=False)

    
    var1 = StringVar()
    var2 = StringVar()

    
    LABLE = Label(window, bg="#34495E", fg="white", text="Welcome to BMI Calculator",
                  font=("Helvetica", 15, "bold"), pady=10)
    LABLE.place(x=70, y=10)
    LABLE11 = Label(window, bg="#34495E", fg="white",
                    text="-------------------------------------------------------------------------------")
    LABLE11.place(x=0, y=48)
    
    
    
    LABLE1 = Label(window, bg="#34495E", fg="white", text="Enter Weight (in kg):", bd=4,
                   font=("Helvetica", 12, "bold"), pady=5)
    LABLE1.place(x=70, y=80)
    ENTRY1 = Entry(window, bd=6, textvariable=var1, width=10 ,font=('Roboto 11',15,'normal'),justify="center")
    ENTRY1.place(x=240, y=80)
    
    
    
    LABLE2 = Label(window, bg="#34495E", fg="white", text="Enter Height (in cm):", bd=4,
                   font=("Helvetica", 12, "bold"), pady=5)
    LABLE2.place(x=70, y=131)
    ENTRY2 = Entry(window, bd=6, textvariable=var2, width=10, font=('Roboto 11',15,'normal'),justify="center")
    ENTRY2.place(x=240, y=131)
   


    BUTTON = Button(window, bg="brown", fg="white", bd=10, text="Reset", width=5, padx=5,  command=iReset,
                    font=("Helvetica", 15, "bold"))
    BUTTON.grid(row=1, column=0)
    BUTTON.place(x=55, y=210)
    BUTTON1 = Button(window, bg="orange", fg="white", bd=10, text="BMI", width=5, padx=5,  command=calculate_bmi,
                     font=("Helvetica", 15, "bold"))
    BUTTON1.grid(row=1, column=1)
    BUTTON1.place(x=160, y=210)
    BUTTON2 = Button(window, bg="red", fg="white", bd=10, text="Exit", width=5, padx=5,  command=iExit,
                     font=("Helvetica", 15, "bold"))
    BUTTON2.grid(row=1, column=1)
    BUTTON2.place(x=265, y=210)
    
    

    LABLE3 = Label(window, bg="#34495E", fg="white", text="Your BMI", bd=6,
                   font=("Helvetica", 15, "bold"), pady=5)
    LABLE3.place(x=150, y=280)
    ResultBMI = Text(window, bg="sky blue", bd=6, width=33,
                     font=("Roboto 11",12,"bold"), height=2, pady=5)
    ResultBMI.place(x=47, y=320)
    

    
    window.mainloop()

