import pandas as pd
import matplotlib.pyplot as plt
import os
print("Current working directory:", os.getcwd())
# CSV فائل پڑھیں (اپنی فائل کا نام یا path یہاں دیں)
df = pd.read_csv('test.csv')
df = pd.read_csv(r'C:\Users\ali nawaz\Desktop\Python work\test.csv')

# ڈیٹا کا پہلا پانچ ریکارڈ دکھائیں تاکہ تصدیق ہو جائے
print(df.head())
print(df.dtypes)

# تمام numeric کالمز کا plot بنائیں
df.plot()

# plot دکھائیں
plt.show()