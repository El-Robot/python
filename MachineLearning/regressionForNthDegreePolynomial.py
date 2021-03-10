import matplotlib.pyplot as plt
from IPython.display import clear_output
import numpy as np
from time import sleep


class LinearReg:

    def __init__(self, x, y, n, a=4):  # constructor
        self.coeff = [0]*(n+1)
        self.n = n
        self.x = x
        self.y = y
        self.a = a

        xRange = max(x) - min(x)
        yRange = max(y) - min(y)
        self.plottingListX = np.arange(min(
            x) - 0.2*xRange, max(x) + 0.2*xRange, ((max(x) + 0.2*xRange) - (min(x) - 0.2*xRange))/100)
        self.plottingListX = self.plottingListX.tolist()
        self.plottingListY = [0]*len(self.plottingListX)

        plt.ion()
        self.fig, self.ax = plt.subplots()

        plt.xlim(min(x) - 0.2*xRange, max(x) + 0.2*xRange)
        plt.ylim(min(y) - 0.2*yRange, max(y) + 0.2*yRange)

        self.plot, = self.ax.plot(self.plottingListX, self.plottingListY)
        plt.scatter(x, y)

        plt.draw()

    def h(self, x):  # returns the current value of the equation for a given x
        sum = 0
        for i in range((self.n+1)):
            sum += float(self.coeff[i]*x**i)
        return sum

    def gradientNth(self, n):  # gradient that
        sum = 0
        for i in range(len(x)):
            sum += (self.h(x[i])-y[i])*(x[i])**n
        return sum*(self.a)/len(x)

    def cost(self) -> float:
        sum = 0.0
        for i in range((self.n+1)):
            sum += float(self.h(x[i])-y[i])**2
        return float((sum)/2*(len(x)))

    def find(self):
        strikes = 10
        minCost = abs(self.cost())

        try:
            while abs(self.cost()) > 0.0001:

                if minCost > abs(self.cost()):
                    minCost = abs(self.cost())
                    strikes = 10
                else:
                    strikes -= 1

                if strikes == 0:
                    raise OverflowError

                temp = [0]*(self.n+1)
                for i in range(len(self.coeff)):
                    temp[i] = self.coeff[i] - self.gradientNth(i)

                # flag = False
                # for i in range(len(self.coeff)):
                #     if abs(temp[i] - self.coeff[i]) > 0.00000001:
                #         flag = True
                # if not flag:
                #     break

                for i in range(self.n+1):
                    self.coeff[i] = temp[i]

                self.plottingListY = []
                for x in self.plottingListX:
                    self.plottingListY.append(self.h(x))

                print(self.coeff)
                print("a = " + str(self.a))
                self.updatePlot()

        except OverflowError:
            self.coeff = [0]*(self.n+1)
            self.a /= 1.1
            self.find()

        eqString = "y = " + str(round(self.coeff[0], 2))

        for i in range(1, self.n + 1):
            eqString += (" + " + str(round(self.coeff[i], 2)) + "x^" + str(i))

        print(eqString)

    def updatePlot(self):

        self.plot.set_ydata(self.plottingListY)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


if __name__ == "__main__":

    y = [3, 4, 8]
    x = [1, 2, 3]

    lin = LinearReg(x, y, 2)
    lin.find()
