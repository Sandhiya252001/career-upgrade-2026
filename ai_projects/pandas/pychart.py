import pandas as pd
import matplotlib.pyplot as plt
departments=["IT","HR","Finance"]
employees=[20,10,25]
plt.pie(employees,labels=departments)
plt.show()
plt.bar(departments,employees)
plt.show()