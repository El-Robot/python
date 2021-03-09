class LinearReg:

    def __init__(self, x, y, a = 0.001):
        self.coeff = [0,0]
        self.x = x
        self.y = y
        self.a = a

    
    def h(self, x):
        return float(self.coeff[0] + self.coeff[1]*x)

    def gradient1(self):
        sum = 0
        for i in range(len(x)):
            sum += (self.h(x[i])-y[i])*(x[i])
        return sum*(self.a)/len(x)

    def gradient0(self):
        sum = 0
        for i in range(len(x)):
            sum += (self.h(x[i])-y[i])
        return sum*(self.a)/len(x)

    def cost(self) -> float:
        sum = 0.0
        for i in range(len(x)):
            sum += float(self.h(x[i])-y[i])**2
        return float((sum)/2*(len(x)))

    def find(self):
        while abs(self.cost()) > 0.001 :
            temp0 = self.coeff[0] - self.gradient0()
            temp1 = self.coeff[1] - self.gradient1()

            if abs(temp0 - self.coeff[0]) < 0.00001 and abs(temp1 - self.coeff[1]) < 0.00001:
                break

            self.coeff[0] = temp0
            self.coeff[1] = temp1

            

            print(self.coeff)

        print("Y = " + str(self.coeff[0]) + " + " + str(self.coeff[1]) + "*X")


if __name__ == "__main__":
    
    x = [1, 3, 5, 7]
    y = [0, 2, 4, 6]

    lin = LinearReg(x, y)
    lin.find()