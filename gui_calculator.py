#This is surely not the cleanest way to do, but I wanted to learn how to create, call and use class.
import tkinter as tk

#GUI
root = tk.Tk()
root.title('Calculator')

#global
nbr1 = ''
nbr2 = ''
operator = ''

#Creating the GUI
class CalcGui(tk.Frame):
    def __init__(self,master=None, **kwargs):
        super().__init__(master)
        self.master = master
        self.body(master)
    
    #print the numbers on the entry
    def button_click(self, e, g_nbr):
        current = e.get()
        e.delete(0, tk.END)
        e.insert(0, str(current) + str(g_nbr))

   #clear the entry
    def button_clear(self,e):
        global nbr1
        global nbr2 
        global operator
        nbr1 = ''
        nbr2 = ''
        operator = ''
        e.delete(0, tk.END)
    
   #store the first part
    def button_operation(self,e,g_operator):
        global nbr1
        global nbr2
        global operator
        #handling of multiple operation like (1+2+3 etc..)
        if nbr1 == '' :
            operator = g_operator
            nbr1 = e.get()
            e.delete(0, tk.END)
        else :
            nbr2 = e.get()
            e.delete(0, tk.END)
            result = Calculator.calc(self,nbr1, nbr2, operator)
            nbr1 = result
            operator = g_operator
            
    #handle operation and call the calculation class    
    def button_equal(self,e):
        global nbr1
        global nbr2 
        global operator
        nbr2 = e.get()
        e.delete(0, tk.END)
        e.insert(0, Calculator.calc(self,nbr1, nbr2, operator))

    #generate entry fields and buttons  
    def body(self,master):

        #generate the grid
        e = tk.Entry(master, width=50, borderwidth=3)
        e.grid(row=0, column=0, columnspan=3) 

        #button creation
        b1 = tk.Button(master, text= '1', padx=45, pady=20, command=lambda: self.button_click(e,1))
        b2 = tk.Button(master, text= '2', padx=45, pady=20, command=lambda: self.button_click(e,2))
        b3 = tk.Button(master, text= '3', padx=45, pady=20, command=lambda: self.button_click(e,3))
        b4 = tk.Button(master, text= '4', padx=45, pady=20, command=lambda: self.button_click(e,4))
        b5 = tk.Button(master, text= '5', padx=45, pady=20, command=lambda: self.button_click(e,5))
        b6 = tk.Button(master, text= '6', padx=45, pady=20, command=lambda: self.button_click(e,6))
        b7 = tk.Button(master, text= '7', padx=45, pady=20, command=lambda: self.button_click(e,7))
        b8 = tk.Button(master, text= '8', padx=45, pady=20, command=lambda: self.button_click(e,8))
        b9 = tk.Button(master, text= '9', padx=45, pady=20, command=lambda: self.button_click(e,9))
        b0 = tk.Button(master, text= '0', padx=45, pady=20, command=lambda: self.button_click(e,0))
        b_plus = tk.Button(master, text= '+', padx=43, pady=20, command=lambda: self.button_operation(e, '+'))
        b_minus = tk.Button(master, text= '-', padx=44, pady=20, command=lambda: self.button_operation(e,'-'))
        b_divide = tk.Button(master, text= '/', padx=44, pady=20, command=lambda: self.button_operation(e, '/'))
        b_multiply = tk.Button(master, text= 'X', padx=43, pady=20, command=lambda: self.button_operation(e, '*'))
        b_equal = tk.Button(master, text= '=', padx=44, pady=20, command=lambda: self.button_equal(e))
        b_clear = tk.Button(master, text= 'C', padx=45, pady=20, command=lambda: self.button_clear(e))

        #Button on screen
        b7.grid(row=1, column=0)
        b8.grid(row=1, column=1)
        b9.grid(row=1, column=2)

        b4.grid(row=2, column=0)
        b5.grid(row=2, column=1)
        b6.grid(row=2, column=2)

        b1.grid(row=3, column=0)
        b2.grid(row=3, column=1)
        b3.grid(row=3, column=2)
    
        b0.grid(row=4, column=1)
        b_equal.grid(row=4, column=2)
        b_clear.grid(row=4, column=0)
        
        b_divide.grid(row=1, column=4)
        b_multiply.grid(row=2, column=4)
        b_plus.grid(row=3, column=4)
        b_minus.grid(row=4, column=4)


#Class fo all the calculation
class Calculator:
    def __init__ (self, nbr1, nbr2,operator):
        self.nbr1 = nbr1
        self.nbr2 = nbr2
        self.operator = operator

    def calc (self, nbr1, nbr2,operator):
        nbr1 = int(nbr1)
        nbr2 = int(nbr2)

        if (operator == '+') :
            result = nbr1 + nbr2
            return(result)

        elif (operator == '-') :
            result = nbr1 - nbr2
            return(result)

        elif (operator == '*') :
            result = nbr1 * nbr2
            return(result)

        elif (operator == '/') :
            result = nbr1 / nbr2
            return(result)
    
calc_gui = CalcGui(master=root)
calc_gui.mainloop()
