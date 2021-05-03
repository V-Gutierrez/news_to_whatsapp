import pyautogui
import time


from browser_navigate import access_url_inbrowser
from fetch_news import fetch_news


def send_news(webwhatsapp_url, newsapi_personal_key, news_language, news_country, news_category, search_terms='', news_amount_limit=5, news_offset=0):
    news_list = fetch_news(
        newsapi_personal_key, news_language, news_country, news_category, search_terms
    )['articles']

    access_url_inbrowser(webwhatsapp_url)

    break_line = "\n"

    if len(news_list) > 0:
        for article_index, value in enumerate(news_list, news_offset):
            title = value['title']
            description = value['description']
            source = value['source']['name']

    # Interact with GUI
            content = format(
                break_line +
                '*' + title + '*'
                + break_line +
                '_' + description + '_'
                + break_line
                + 'Fonte: ' + source
            )

            pyautogui.write(content)
            pyautogui.press('enter')
            time.sleep(5)

            if article_index == news_amount_limit:
                break
    else:
        pyautogui.write('Sem notícias por hoje')

    if len(news_list) > 0:
        pyautogui.write('Fim das notícias do dia')
        pyautogui.press('enter')
