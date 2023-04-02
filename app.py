import asyncio

from flask import Flask, Response, render_template, request

from utils_hh import main_hh
from utils_habr import main_habr

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_csv_hh', methods=['POST'])
def download_hh():

    data = request.form

    headers = {
        'User-Agent': data['user-agent'],
        'Cookie': data['cookie']
    }

    csv_data = asyncio.run(main_hh(headers=headers, number_pages=int(data['num-pages'])))

    return Response(
        csv_data,
        mimetype='text/csv',
        headers={
            'Content-Disposition': 'attachment;filename=hh.csv',
            'Cache-Control': 'no-cache'
        }
    )

@app.route('/generate_csv_habr', methods=['POST'])
def download_habr():

    data = request.form

    headers = {
        'User-Agent': data['user-agent'],
        'Cookie': data['cookie']
    }

    csv_data = asyncio.run(main_habr(headers=headers, number_pages=int(data['num-pages'])))

    return Response(
        csv_data,
        mimetype='text/csv',
        headers={
            'Content-Disposition': 'attachment;filename=habr.csv',
            'Cache-Control': 'no-cache'
        }
    )


if __name__ == '__main__':
    app.run(debug=False)
