import pyautogui
import webbrowser
import time

from newsapi import NewsApiClient

# Target number
number = 00_0_00_0000_000


# Fetch news

newsapi_personal_key = 'your_api_key'
news_language = 'pt'
news_country = 'br'
news_category = 'general'

newsapi = NewsApiClient(api_key=newsapi_personal_key)

top_headlines = newsapi.get_top_headlines(
    category=news_category,
    language=news_language,
    country=news_country,
)


# Load webpage in browser
webbrowser.open("https://web.whatsapp.com/send?phone=" + str(number), 0, 1)

news_list = top_headlines['articles']
break_line = "\n"


if len(news_list) > 0:
    for article_index, value in enumerate(news_list):
        author = value['author']
        title = value['title']
        description = value['description']
        source = value['source']['name']

# Interact with GUI
        content = format(
            break_line + '*' + title + '*' + '  ' +
            description + break_line + 'Fonte: '+source
        )

        pyautogui.write(content)
        pyautogui.press('enter')
        time.sleep(5)

        if article_index == 5:
            break
else:
    pyautogui.write('Sem notícias por hoje')

if len(news_list) > 0:
    pyautogui.write('Fim das notícias do dia')
    pyautogui.press('enter')
