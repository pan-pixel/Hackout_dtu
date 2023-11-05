from pygooglenews import GoogleNews
import openai
import datetime

API_KEY = "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"
openai.api_key = API_KEY

company = input("Enter company name : ")

def get_news(company):
    gn = GoogleNews()
    s = gn.search(company + ' Stock')

    stringNews = ""
    s["entries"] = s["entries"][:15]
    for entry in s["entries"]:
        text = entry['title']
        position = text.find('-')
        if position != -1:
            result = text[:position]
        else:
            result = text
        stringNews += result + " published on " + entry['published'] + "\n"

    return stringNews


def gpt_analysis(company):
    news = get_news(company=company)
    current_date = datetime.date.today()
    prompt = "Assume today is " + str(current_date) + " and below are listed 15 news that are supposed to be news affecting stocks of the company- " + company + ". Read the headlines given along with their published date and select top 3 news which you really think are going to affect the stock prices in future and specially not which has already affected. Also give the sentimantel analysis of those 3 selected titles, wether it will effect it in positive, negative or have neutral impact. here are the titles - " + news + ". In the output only write me the title without the published date and only the sentiment, nothing else"
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    print(response['choices'][0]['message']['content'])

get_news(company)