import numpy as np
import matplotlib.pyplot as plt

#Warn about using the correct parameters so the outputs are as expected
print('When calling the function, the first parameter should be a positive real number ideally between 10 and 20 and the second parameter should be a negative  real number between -1 and 0')
print('The third parameter should be the value to stay above and fourth parameter should be the starting value for each administration')

#Define function that will use data_1 as the first part of the equation and data_2 as the second part and data_3 as the value to stay above and data_4 as the starting value
def creation(data_1, data_2, data_3, data_4):
    #Define lists to use: x is the time, y is the output that adds in more chemical, z is the output that doesn't add in more chemical
    #Define globally so they can be used to form the plots later
    global x
    global y
    global z
    x = list(range(1,50))
    y = list(range(1,50))
    z = list(range(1,50))
    #counter will be used to move through the times and 'restart' the clock when the dose is added
    counter = 0
    #i is the overall time that will move through x to create z
    i = 1
    #sets the first element of y and z to be 12 so it starts on 12
    y[0]=data_4
    z[0]=data_4
    #A while loop that iterates through i to create the list y and z
    while i<49:
        #sets the time to the position in x 
        time = x[counter]
        #Creates y using time as it resets and z using i as it doesn't reset
        y[i] = data_1*np.exp(data_2*time)
        z[i] = data_1*np.exp(data_2*i)
        #If the element in y is less than 5 then it 'adds more chemical' (resets to 12) and resets the time after dose to 0 hours
        if y[i]<data_3:
            y[i] = data_4
            print(y[i])
            ##x = list(range(1,50))
            counter = 0
        else:
            ##time = x[counter]
            ##y[counter] = 11.481*np.exp(-0.163*time)
            print(y[counter])
        #Adds 1 to time and time after dose
        i = i + 1
        counter = counter + 1

#Just to check the outputs are correct
#print(y)
#print(z)
counter = 0
i = 1
firstInput = float(input('Please input the first parameter: '))
secondInput = float(input('Please input the second parameter: '))
thirdInput = float(input('Please input the third parameter: '))
fourthInput = float(input('Please input the fourth parameter: '))
creation(firstInput, secondInput, thirdInput, fourthInput)

#Plots y and z against the time on the same set of axes
plt.figure()
plt.plot(x, y)
plt.plot(x, z)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.xlabel('$Time$')
plt.ylabel('$Concentration$')
plt.show()
