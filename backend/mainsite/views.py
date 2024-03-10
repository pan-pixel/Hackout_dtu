import google.generativeai as genai
import os
from django.shortcuts import render, redirect
from time import sleep
import requests


# p = os.environ["GOOGLE_API_KEY"]
p = 'AIzaSyD9AKMOvsfcwN-YIB-1cxwrffCqKGE5j8o'
genai.configure(api_key=p)

generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

modelInitialContent = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
convoInitialContent = modelInitialContent.start_chat(history=[
  {
    "role": "user",
    "parts": ["generate me a detailed equity investment report of a company name I will tell, it shall comprise all key values - Live Stock Price, CMP, Target Value, Target Period; Brief Description of the stock including its profile in 30 words, approx growth and leading margins, ROCE and payouts percentage; Last quarter details including QoQ, YoY, EBIT Margin and other major highlights; What should investors do as per analysis of past 5 years to buy, sell or hold the stock and the target Particular values of  - Market Capitalization,  Total Debt, Cash and equivalents, EV, 52 week H/L, Equity capital Shareholding Pattern and its value for past 3 months; Key triggers for future price performance; Recent event and key risks; Alternate stock idea. The output must be formatted as per markdown file format"]
  },
  {
    "role": "model",
    "parts": ["**Equity Investment Report**\n\n**Company Name:** [Company Name]\n\n**Live Stock Price: **[Live Stock Price]\n\n**CMP:** [Current Market Price]\n\n**Target Value:** [Target Value]\n\n**Target Period:** [Target Period]\n\n**Brief Description of the Stock:**\n\n[Company Name] is a leading provider of [industry/sector] with a strong market share of [percentage]%. The company has consistently delivered [growth percentage]% revenue growth and [margin percentage]% EBITDA margins. It has a robust ROCE of [percentage]% and a dividend payout ratio of [percentage]%.\n\n**Last Quarter Details:**\n\n* QoQ Revenue Growth: [Percentage]%\n* YoY Revenue Growth: [Percentage]%\n* EBIT Margin: [Percentage]%\n\n**Major Highlights:**\n\n* [Highlight 1]\n* [Highlight 2]\n* [Highlight 3]\n\n**Historical Analysis (Past 5 Years):**\n\nBased on the analysis of the past 5 years, investors should consider the following actions:\n\n* **Buy:** If the stock price falls below [buy price].\n* **Sell:** If the stock price rises above [sell price].\n* **Hold:** Otherwise, continue to hold the stock.\n\n**Target Particulars:**\n\n* Market Capitalization: [Value]\n* Total Debt: [Value]\n* Cash and Equivalents: [Value]\n* EV: [Value]\n* 52 Week H/L: [High Value] / [Low Value]\n* Equity Capital: [Value]\n\n**Shareholding Pattern (Past 3 Months):**\n\n| Shareholder | Value |\n|---|---|\n| Promoters | [Percentage]% |\n| Institutions | [Percentage]% |\n| Retail Investors | [Percentage]% |\n\n**Key Triggers for Future Price Performance:**\n\n* [Trigger 1]\n* [Trigger 2]\n* [Trigger 3]\n\n**Recent Events and Key Risks:**\n\n* [Recent Event 1]\n* [Recent Event 2]\n\n**Key Risks:**\n\n* [Risk 1]\n* [Risk 2]\n* [Risk 3]\n\n**Alternate Stock Idea:**\n\n* [Alternative Stock Name]"]
  },
])

modelTabularDataContent = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
convoTabularDataContent = modelTabularDataContent.start_chat(history=[
  {
    "role": "user",
    "parts": ["generate me a equity investment tables of a company name I will tell, it shall comprise tables with the following details - Table 1 named - Key Financial Summary with columns of past 3 FY, 2 year CAGR and 5 year CAGR with rows of Net sales, EBITDA, EBITDA Margins, Net Profit, EPS, RoNW, RoCE; Table 2 of ESG Disclosure Score; Table 3 of Variance Analysis; Table 4 of Change in estimates; Table 5 of Peer Comparision against metrics of CMP, TP, Rating, MCap, Past 3 years of EPS, P/E, RoCE and RoE"]
  },
  {
    "role": "model",
    "parts": ["Sure I will do that!"]
  },
])

modelTabularDataContent2 = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
convoTabularDataContent2 = modelTabularDataContent.start_chat(history=[
  {
    "role": "user",
    "parts": ["generate me a equity investment tables of a company name I will tell, it shall comprise tables with the following details - Table 6 Profit and Loss Statement; Table 7 of Cash Flow Statement and Table 8 of Balance Sheet, all these tables of 2 years with 2 Expected Financial Years"]
  },
  {
    "role": "model",
    "parts": ["Sure I will do that!"]
  },
])

modelTexttoMD = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
convoTextToMD = modelTexttoMD.start_chat()

def save_as_md_file(text, file_path):
    with open(file_path, 'w') as file:
        # file.write(f"![Image](file://{image_path})\n\n")
        file.write(text)

    

def userInputCompany(com):
    totalMD = ""
    finalText = ""

    convoInitialContent.send_message(com)
    text = convoInitialContent.last.text
    finalText += text
    
    convoTabularDataContent.send_message(com)
    text = convoTabularDataContent.last.text
    finalText += text

    finalText = finalText.replace("₹", "Rs ")
    
    prompt =  "For the given text convert it to suitable .md (markdown file) syntax and remove any disclaimer lines-  " + finalText
    convoTextToMD.send_message(prompt)
    text = convoTextToMD.last.text
    
    totalMD += text
    finalText =""

    convoTabularDataContent2.send_message(com)
    text = convoTabularDataContent2.last.text
    finalText += text

    finalText = finalText.replace("₹", "Rs ")
    
    prompt =  "For the given text convert it to suitable .md (markdown file) syntax and remove any disclaimer lines-  " + finalText
    convoTextToMD.send_message(prompt)
    text = convoTextToMD.last.text

    totalMD += text

    


    save_as_md_file(text=totalMD, file_path="/Users/prathamarora/Documents/glb_hack/backend/static/assests/report.md");
    

# def callInput():
#     com = input("Enter Company name : ")
#     userInputCompany(com)

# modelStockRec = genai.GenerativeModel(model_name="gemini-1.0-pro",
#                               generation_config=generation_config,
#                               safety_settings=safety_settings)

# convoStockRec = modelStockRec.start_chat()


# def stockRec():
#     initial = int(input("Enter initial investment : "))
#     monthly = int(input("Enter monthly investment : "))
#     final = int(input("Enter your final goal amount : "))
#     years = int(input("Enter the time in which you want to attain that goal : "))
#     r = rorCal.caller(initial, monthly, final, years)
#     print("You need min this SIP interest rate : ", r)
#     p = "Recommned me top 5 investment SIP/Mutual Fund or Stocks which will give interest above {}% \encompassed in a single list in innerHTML format".format(r)
#     convoStockRec.send_message(p)
#     print(convoStockRec.last.text)

# stockRec()

def home(request):
    if request.method == 'POST':
        company = request.POST['company']
        print(company)
        userInputCompany(company)
        return redirect('search')
    
    return render(request, 'main.html')


def about(request):
    return render(request,"about.html")

def search(request):
    if request.method == 'POST':
        company = request.POST['company']
        print(company)
        userInputCompany(company)
        return redirect('search')
    return render(request,'aftersearch.html')


def gameLearn(request):
    return render(request,"learn.html")

def goal_analyser(request):
    return render(request, 'goal.html')


def syllabus(request):
    return render(request,'syllabus.html')

def lesson(request):
    return render(request, 'lesson.html')