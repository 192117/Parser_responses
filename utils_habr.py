import asyncio
import aiohttp
import pandas as pd
from bs4 import BeautifulSoup

URL_TEMPLATE = 'https://career.habr.com/responses?page={}'


async def fetch(session, url, headers):
    async with session.get(url, headers=headers) as response:
        return await response.text()


async def get_responses(page, headers):
    async with aiohttp.ClientSession() as session:
        url = URL_TEMPLATE.format(page)
        response = await fetch(session, url, headers)
        soup = BeautifulSoup(response, 'html.parser')
        rows = soup.find('table', class_='my_responses').find_all('tr')
        responses = []
        for row in rows:
            response = []
            data = row.find_all('td')
            if data:
                response.append(data[2].find('div', class_='status').text)
                response.append(data[0].find('div', class_='title').text.split(':')[-1])
                response.append(data[0].find('span', class_='comapny').text)
                response.append(data[1].text)
            if response:
                responses.append(response)
        return responses


def create_excel_file(values):
    df = pd.DataFrame(values, columns=['Cтатус', 'Вакансия', 'Компания', 'Дата отклика'])
    return df.to_csv(index=False, encoding='utf8')


async def main_habr(headers, number_pages):
    tasks = [asyncio.create_task(get_responses(page, headers)) for page in range(number_pages)]
    pages = await asyncio.gather(*tasks)
    values = [response for page in pages for response in page]
    return create_excel_file(values)
