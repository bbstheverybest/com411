import matplotlib.pyplot as plt

def small():  #Small function.

   x_values = [3,4 ,4,3,3]   #Co-ordinates.
   y_values = [3, 3, 4,4, 3]

   plt.plot(x_values,y_values, "ro--") #Place the plot as "Red, circle, dotted line."



small()  #Display small function.


def medium():  #Medium function.
    x_values = [2,5,5,2,2]
    y_values = [2,2,5,5,2]
    plt.plot(x_values,y_values, "gs--") #Place the plot as "Green, square, dotted line."

medium() #Display medium function.




def large(): #Large function.
    x_values = [1,6,6,1,1]
    y_values = [1,1,6,6,1]
    plt.plot(x_values,y_values, "bx-") #Place the plot as "Blue, X-shape, straight line."



large() #Display large function.
plt.show() #Show all plots.

#"--" = dotted line, "-" = straight line.

