class LinearReg:

    def __init__(self, x, y, a=0.001):  # constructor
        self.coeff = [0, 0, 0]
        self.x = x
        self.y = y
        self.a = a

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

            print(self.coeff)

        print("y = " + str(round(self.coeff[0], 2)) + " + " + str(
            round(self.coeff[1], 2)) + "x" + " + " + str(round(self.coeff[2], 2)) + "x²")

if __name__ == "__main__":

    y = [1, 4, 9]
    x = [1, 2, 3]

    # y = [1, 0, 1, 4]
    # x = [-1, 0, 1, 2]

    lin = LinearReg(x, y, 0.001)
    lin.find()
