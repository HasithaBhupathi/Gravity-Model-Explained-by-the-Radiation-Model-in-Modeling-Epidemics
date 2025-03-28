import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams['font.family'] = 'Times New Roman'    #### Graph font type

c = 1.5

##### Constant exponent k such that k > 0
k = 0.5  
##### Independent variable
x = np.linspace(0,5,num = 200)
##### Dependent variable
y = c*x**k

plt.plot(x,y,label = r'$\alpha = 0.5$')
plt.title(r'Power-law function with $\alpha > 0$',fontsize = 15)
plt.xlabel("Independent variable",fontsize = 13)
plt.ylabel("Dependent variable",fontsize = 13)
plt.legend()
plt.show()                



##### Constant exponent k such that -1 < k < 0
k = -0.5 
##### Independent variable
x = np.linspace(0.1,5,num = 200)
##### Dependent variable
y = c*x**k

plt.plot(x,y,label = r'$\alpha = -0.5$')
plt.title(r'Power-law function with $-1 \leq \alpha < 0$',fontsize = 15)
plt.xlabel("Independent variable",fontsize = 13)
plt.ylabel("Dependent variable",fontsize = 13)
plt.legend()
plt.show()


##### Constant exponent k such that k < -1 
k = -1.5 
##### Independent variable
x = np.linspace(0.1,5,num = 200)
##### Dependent variable
y = c*x**k

plt.plot(x,y,label = r'$\alpha = -1.5$')
plt.title(r'Power-law function with $\alpha < -1$',fontsize = 15)
plt.xlabel("Independent variable",fontsize = 13)
plt.ylabel("Dependent variable",fontsize = 13)
plt.legend()
plt.show()



