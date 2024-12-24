import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "D:/Sri Nithilan/Documents/InfoProdigy/archive/twitter_training.csv"
df = pd.read_csv(file_path, delimiter='\t', header=None, names=['ID', 'Topic', 'Sentiment', 'Tweet'])

print(df.head())

sentiment_counts = df['Sentiment'].value_counts()
print(sentiment_counts)

plt.figure(figsize=(10, 6))
sns.countplot(x='Sentiment', data=df)
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()