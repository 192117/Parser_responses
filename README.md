# Сервис по получению списка откликов на вакансии c hh и career.habr (со стороны кандидата)


## Стек:
1. Flask
2. Asyncio
3. Aiohttp
4. BS4
5. Pandas
6. Docker

## _HH_
Сервис проходит по вкладке [Все отклики](https://hh.ru/applicant/negotiations?filter=all&page=0)

![Страница с откликами](https://github.com/192117/ParserHH/blob/master/page.png)

Для того, чтобы получить файл, необходимо передать в форму на [сайте](http://5.104.108.168:8006/) свои User-Agent, 
Cookie и количество страниц на вкладке все отклики

Для получени User-Agent и Cookie перейдите на сайт hh, перейдите во Панель разработчика(F12 или посмотреть код) и 
найдите там index.html и посмотрите заголовки запроса. Скопируйте полностью cookie и user-agent.

![Заголовки запроса](https://github.com/192117/ParserHH/blob/master/headers.png)

Вставьте все необходимые данные и нажмите "Получить свои отклики c hh в CSV-формате", через время начнется загрузка файла.
Можете просмотреть свои отклики

![Отклики](https://github.com/192117/ParserHH/blob/master/response.png)


## _CAREER.HABR_
Сервис проходит по вкладке [Основные](https://career.habr.com/responses?page=1)

![Страница с откликами](https://github.com/192117/ParserHH/blob/master/page_habr.png)

Для того, чтобы получить файл, необходимо передать в форму на [сайте](http://5.104.108.168:8006/) свои User-Agent, 
Cookie и количество страниц на вкладке все отклики

Для получени User-Agent и Cookie перейдите на сайт hh, перейдите во Панель разработчика(F12 или посмотреть код) и 
найдите там index.html и посмотрите заголовки запроса. Скопируйте полностью cookie и user-agent.

![Заголовки запроса](https://github.com/192117/ParserHH/blob/master/headers_habr.png)

Вставьте все необходимые данные и нажмите "Получить свои отклики c career.habr в CSV-формате", через время начнется загрузка файла.
Можете просмотреть свои отклики

![Отклики](https://github.com/192117/ParserHH/blob/master/response.png)
