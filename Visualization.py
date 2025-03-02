

link = "https://raw.githubusercontent.com/swapnilsaurav/MachineLearning/refs/heads/master/4_Position_Salaries.csv"
import numpy as np
import pandas as pd
df = pd.read_csv(link)
print(df)

import matplotlib.pyplot as plt

data = {
    "Position": ["Business Analyst", "Junior Consultant", "Senior Consultant", "Manager",
                 "Country Manager", "Region Manager", "Partner", "Senior Partner",
                 "C-level", "CEO"],
    "Level": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Salary": [45000, 50000, 60000, 80000, 110000, 150000, 200000, 300000, 500000, 1000000]
}

df = pd.DataFrame(data)


df = pd.DataFrame(data)

#creating scatter plot

#plt.figure(figsize=(10, 6))
#plt.scatter(df["Level"], df["Salary"], color='blue', marker='o')

#plt.show()

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df["Level"], df["Salary"], color='blue', marker='o')

# Add labels and title
plt.title("Salary vs. Level", fontsize=16)
plt.xlabel("Level", fontsize=12)
plt.ylabel("Salary", fontsize=12)
plt.grid(True)
plt.xticks(df["Level"])  # Set x-axis ticks for each level
plt.show()


