import matplotlib.pyplot as plt
from IPython.display import clear_output
import numpy as np
from time import sleep


class LinearReg:

    def __init__(self, x, y, a=0.001):  # constructor
        self.coeff = [0, 0, 0]
        self.x = x
        self.y = y
        self.a = a

        self.plottingListX = [*range(-90, 100)]
        self.plottingListX = [i * 0.1 for i in self.plottingListX]
        self.plottingListY = [0]*len(self.plottingListX)

        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.plot, = self.ax.plot(self.plottingListX, self.plottingListY)
        plt.scatter(x, y)
        plt.draw()

    def h(self, x):  # returns the current value of the equation for a given x
        return float(self.coeff[0] + self.coeff[1]*x+self.coeff[2]*x**2)

    def gradient0(self):  # gradient that
        sum = 0
        for i in range(len(x)):
            sum += (self.h(x[i])-y[i])
        return sum*(self.a)/len(x)

    def gradient1(self):
        sum = 0
        for i in range(len(x)):
            sum += (self.h(x[i])-y[i])*(x[i])
        return sum*(self.a)/len(x)

    def gradient2(self):
        sum = 0
        for i in range(len(x)):
            sum += (self.h(x[i])-y[i])*(x[i])*(x[i])
        return sum*(self.a)/len(x)

    def cost(self) -> float:
        sum = 0.0
        for i in range(len(x)):
            sum += float(self.h(x[i])-y[i])**2
        return float((sum)/2*(len(x)))

    def find(self):
        while abs(self.cost()) > 0.000001:
            temp0 = self.coeff[0] - self.gradient0()
            temp1 = self.coeff[1] - self.gradient1()
            temp2 = self.coeff[2] - self.gradient2()

            if abs(temp0 - self.coeff[0]) < 0.00000001 and abs(temp1 - self.coeff[1]) < 0.00000001 and abs(temp2 - self.coeff[2]) < 0.00000001:
                break

            self.coeff[0] = temp0
            self.coeff[1] = temp1
            self.coeff[2] = temp2

            self.plottingListY = []
            for x in self.plottingListX:
                self.plottingListY.append(self.h(x))

            print(self.coeff)
            self.updatePlot()

        print("y = " + str(round(self.coeff[0], 2)) + " + " + str(
            round(self.coeff[1], 3)) + "x" + " + " + str(round(self.coeff[2], 2)) + "x²")

    def updatePlot(self):
        
        self.plot.set_ydata(self.plottingListY)
        # self.fig.set_title("y = " + str(round(self.coeff[0], 2)) + " + " + str(round(self.coeff[1], 3)) + "x" + " + " + str(round(self.coeff[2], 2)) + "x²")
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

if __name__ == "__main__":

    y = [1, 4, 9]
    x = [-1, 2, 3]

    lin = LinearReg(x, y, 1)
    lin.find()
