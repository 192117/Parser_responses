import asyncio
import re
from datetime import date, timedelta

import aiohttp
import pandas as pd
from babel.dates import format_date
from bs4 import BeautifulSoup

URL_TEMPLATE = 'https://hh.ru/applicant/negotiations?filter=all&page={}'


async def fetch(session, url, headers):
    async with session.get(url, headers=headers) as response:
        return await response.text()


async def get_responses(page, headers):
    async with aiohttp.ClientSession() as session:
        url = URL_TEMPLATE.format(page)
        response = await fetch(session, url, headers)
        soup = BeautifulSoup(response, 'html.parser')
        rows = soup.select('tbody.responses-table-tbody--GA5nMRIjZv1vAE3pRtUZ tr.responses-table-row--nt2CTesRhLfQSD4j36rt')
        responses = []
        for row in rows:
            response = []
            for tag in row.find_all(['span', 'button'], {'data-qa': re.compile('^negotiations-item')}):
                text = tag.text.strip().replace('\xa0', ' ')
                dates = ['сегодня', 'вчера', 'позавчера']
                format_text = text.replace(dates[0], format_date(date.today(), format='long', locale='ru'))
                format_text = format_text.replace(dates[1],
                                                  format_date(date.today()-timedelta(days=1), format='long', locale='ru')
                                                  )
                format_text = format_text.replace(dates[2],
                                                  format_date(date.today()-timedelta(days=2), format='long', locale='ru')
                                                  )
                response.append(format_text)
            if response:
                responses.append(response)
        return responses


def create_excel_file(values):
    df = pd.DataFrame(values, columns=['Cтатус', 'Вакансия', 'Компания', 'Дата отклика'])
    return df.to_csv(index=False, encoding='utf8')


async def main(headers, number_pages):
    tasks = [asyncio.create_task(get_responses(page, headers)) for page in range(number_pages)]
    pages = await asyncio.gather(*tasks)
    values = [response for page in pages for response in page]
    return create_excel_file(values)
