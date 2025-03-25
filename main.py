import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if not os.path.exists('charts'):
    os.makedirs('charts')

df = pd.read_csv('dataset/vgsales.csv')

df = df.dropna()
df['Year'] = df['Year'].astype(int)

sales_by_year = df.groupby('Year')['Global_Sales'].sum()

top_platforms = df['Platform'].value_counts().head(10)

regions = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
sales_by_region = df[regions].sum()


sns.set_palette("husl")

plt.figure(figsize=(10, 6))
plt.plot(sales_by_year.index, sales_by_year.values, marker='o', linestyle='-')
plt.title('Динамика продаж видеоигр по годам', fontsize=16)
plt.xlabel('Год', fontsize=12)
plt.ylabel('Продажи (млн копий)', fontsize=12)
plt.savefig('charts/sales_by_year.png')
plt.show()

plt.figure(figsize=(10, 6))
top_platforms.plot(kind='bar')
plt.title('Топ-10 платформ по количеству игр', fontsize=16)
plt.xlabel('Платформа', fontsize=12)
plt.ylabel('Количество игр', fontsize=12)
plt.savefig('charts/top_platforms.png')
plt.show()

plt.figure(figsize=(8, 8))
plt.pie(sales_by_region, labels=regions, autopct='%1.1f%%', startangle=140)
plt.title('Распределение продаж по регионам', fontsize=16)
plt.savefig('charts/sales_by_region.png')
plt.show()