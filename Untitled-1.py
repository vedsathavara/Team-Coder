import matplotlib.pyplot as plt
import pandas as pd
Aieduction = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\2015_16_Statewise_Secondary.csv")
print(Aieduction)
plt.scatter(Aieduction['statname'], Aieduction["sexratio"], color='black', marker="x")
plt.xticks(rotation=45, ha='right')
plt.grid(True)
plt.title('gender ratio in school state wise - Injury Graph')

plt.show()
