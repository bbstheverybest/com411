import matplotlib.pyplot as plt

def display_line(x,y):     #Function named display line.
    plt.plot(x, y)   #Plants the plot x and y.


def runtask1():
    x_values = [1,2,3,4,5]
    y_values = [1,4,9,16,25]

    display_line(x=x_values,y=y_values)  #Called first function whilst passing the x an y values through.
    plt.show()   #Shows the plots.

runtask1()