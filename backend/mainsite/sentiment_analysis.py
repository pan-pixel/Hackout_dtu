import nltk
from textblob import TextBlob 
from newspaper import Article



# company_name = input("Enter a company name: ")
# first_link = get_first_news_link(company_name)

# article = Article(first_link)
# article.download() # Downloads Article
# article.parse() # Removes HTML and other elements 
# article.nlp() #Prepares it for natural language processing 
# text =article.summary # creates a summary of the article 


text = "I feel bad today!!"
blob= TextBlob(text)  # Textblob object is created for nlp
sentiment=blob.sentiment.polarity # Finds the sentiment between -1 and 1 
if sentiment >=0.25:
  print("Positive")
elif sentiment >=0:
  print("Neutral Sentiment")
else: 
  print("Bad")