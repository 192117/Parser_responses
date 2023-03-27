import asyncio

from flask import Flask, Response, render_template, request

from utils import main

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_xls', methods=['POST'])
def download():

    data = request.form

    headers = {
        'User-Agent': data['user-agent'],
        'Cookie': data['cookie']
    }

    csv_data = asyncio.run(main(headers=headers, number_pages=int(data['num-pages'])))

    return Response(
        csv_data,
        mimetype='text/csv',
        headers={
            'Content-Disposition': 'attachment;filename=hh.csv',
            'Cache-Control': 'no-cache'
        }
    )


if __name__ == '__main__':
    app.run(debug=False)
