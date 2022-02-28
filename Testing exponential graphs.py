import numpy as np
import matplotlib.pyplot as plt


def main():
    x = np.linspace(0, 20, 100)
    y = 11.481*np.exp(-0.163*x)

    plt.figure()
    plt.plot(x, y)
    plt.xlabel('$Time$')
    plt.ylabel('$Concentration$')

##    plt.figure()
##    plt.plot(x, -np.exp(-x))
##    plt.xlabel('$x$')
##    plt.ylabel('$-\exp(-x)$')

    plt.show()

if __name__ == '__main__':
    main()

    
##equation = 11.481e^(-0163x)
