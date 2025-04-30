#MapPlot.py
#Name: Bennett McDonald
#Date: 4/30/25
#Assignment: matplot

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('movies.csv')

print(df[['Title', 'Genres', 'IMDB.Rating', 'BoxOffice.Revenue']].head())

df['BoxOffice.Revenue'] = pd.to_numeric(df['BoxOffice.Revenue'], errors='coerce')

df_clean = df.dropna(subset=['IMDB.Rating', 'BoxOffice.Revenue'])

df_clean = df_clean[df_clean['BoxOffice.Revenue'] < 1_000_000_000]

plt.figure(figsize=(10, 6))
plt.scatter(df_clean['IMDB.Rating'], df_clean['BoxOffice.Revenue'] / 1_000_000, alpha=0.5, c='green')
plt.title('IMDB Rating vs Box Office Revenue')
plt.xlabel('IMDB Rating')
plt.ylabel('Box Office Revenue (in millions)')
plt.grid(True)
plt.tight_layout()
plt.show()

df_clean['PrimaryGenre'] = df_clean['Genres'].str.split(',').str[0]
genre_avg = df_clean.groupby('PrimaryGenre')['BoxOffice.Revenue'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
genre_avg.plot(kind='bar', color='skyblue')
plt.title('Average Box Office Revenue by Genre')
plt.xlabel('Genre')
plt.ylabel('Average Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
