import re
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from wordcloud import WordCloud, STOPWORDS


CSV_PATH = 'data/susceptible_users.csv'

# load txt
df = pd.read_csv(CSV_PATH)


# tfidf / subtract common words from normal tweets
df = df.dropna()
df["(u.description)"] = df["(u.description)"].apply(lambda s: re.sub("\d+", " ", str(s)))
corpus = df["(u.description)"].array

pipe = Pipeline([('count', CountVectorizer()),
                 ('tfid', TfidfTransformer())]).fit(corpus)

stopwords = set(STOPWORDS)
idx_to_word = {v:k for k,v in pipe['count'].vocabulary_.items()}
word_freq = {idx_to_word[k]: v for k, v in enumerate(pipe['tfid'].idf_) if (idx_to_word[k]).lower() not in stopwords}

# plot word cloud
words = " ".join(list(corpus))
wordcloud = WordCloud(
      background_color='white',
      stopwords=stopwords,
      max_words=200,
      max_font_size=40,
      random_state=42
     #).generate_from_frequencies(word_freq)
    ).generate(words)


fig = plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
fig.savefig("susceptible_users_wordcloud.png", dpi=900)