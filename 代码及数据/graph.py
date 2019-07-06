import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file_name = 'train_validation.xlsx'

df = pd.read_excel(file_name)
# print(df)
plt.style.use('seaborn-whitegrid')

fig = plt.figure(figsize=(8, 4), dpi=200)
plt.subplot(121)
plt.scatter(x=129, y=df[df['Step'] == 129].VA, marker='*', s=150, c='r')
plt.plot(df['Step'], df['TA'], c='r')
plt.plot(df['Step'], df['VA'], c='c')
plt.ylim([0.8, 1.01])

plt.xlabel('Iterations')
plt.title('Accuracy')

plt.subplot(122)
plt.scatter(x=129, y=df[df['Step'] == 129].VL, marker='*', s=150, c='r', label='Early Stop')
plt.plot(df['Step'], df['TL'], c='r', label='Train')
plt.plot(df['Step'], df['VL'], c='c', label='Validation')
plt.ylim([0.9, 1.2])
plt.xlabel('Iterations')
plt.legend()
plt.title('Loss')

plt.savefig('figure.png', dpi=200)
plt.show()
