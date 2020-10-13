# this program converts the Farenheit to Celsius and vice versa
# it is tested on python 3.4
# modifications are needed to get it working on python 2.xx
from tkinter import *
from tkinter.simpledialog import askfloat , askinteger
from tkinter import messagebox
import sys
root = Tk()
root.title('temperature converter')
text = Text(root , width = 80 , height = 30)
text.config(bg = 'blue', fg = 'yellow' , font=('Arial', 12, 'bold', 'italic'))
text.pack()
def to_write( s):
    '''
       this function will print to text widget
    '''

    text.insert(END,s)
def cel_to_far():
    '''
        this function asks for a number in Celsius
        and converts it to Farenheit
     '''
    clus = askfloat('Celsius','Please enter the temperature in Celsius :')
    far = (clus*(9/5.0)) + 32
    print('\n{} Celsius is equal to {:.1f} Farenheit '.format(clus,far) )

def far_to_cel():
    '''
        this function asks for a number in Farenheit
        and converts it to Celsius
     '''

    far = askfloat('Farenheit','Please enter the temperature in Farenheit : ')
    clus = (far - 32) * (5/9.0)

    print('\n{} Farenheit is equal to {:.1f} Celsius '.format(far,clus) )
def to_exit():


    quit()

sys.stdout.write = to_write
while True:
    result=askinteger('options',(' Farenheit to Celsius press 1',
                                        '\n Celsius to Farenheit press 2',
                                        '\n Exit  press 3 '))

    if result == 1:
        far_to_cel()
    elif result == 2:
        cel_to_far()
    elif result == 3:
        to_exit()
    elif result is None:
        to_exit()
    else:
        messagebox.showerror('wrong input','the choice should be either 1 , or 2 or 3 ')
root.mainloop()
