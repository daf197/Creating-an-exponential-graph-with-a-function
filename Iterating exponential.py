import numpy as np
import matplotlib.pyplot as plt


#Define lists to use: x is the time, y is the output that adds in more chemical, z is the output that doesn't add in more chemical
x = list(range(1,50))
y = list(range(1,50))
z = list(range(1,50))
#counter will be used to move through the times and 'restart' the clock when the dose is added
counter = 0
#i is the overall time that will move through x to create z
i = 1
#sets the first element of y and z to be 12 so it starts on 12
y[0]=12
z[0]=12

#Useless
print(x)

#A while loop that iterates through i to create the list y and z
while i<49:
    #sets the time to the position in x 
    time = x[counter]
    #Creates y using time as it resets and z using i as it doesn't reset
    y[i] = 11.481*np.exp(-0.163*time)
    z[i] = 11.481*np.exp(-0.163*i)
    #If the element in y is less than 5 then it 'adds more chemical' (resets to 12) and resets the time after dose to 0 hours
    if y[i]<5:
        y[i] = 12
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
print(y)
print(z)

#Plots y and z against the time on the same set of axes
plt.figure()
plt.plot(x, y)
plt.plot(x, z)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.xlabel('$Time$')
plt.ylabel('$Concentration$')
plt.show()
