import json

from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_devices():
    t = ''' [{
            "id": 1,
            "latitude": 39.915,
            "longitude": 116.404,
            "date": '2016-05-03',
            "name": '王小虎',
            "address": '上海市普陀区金沙江路 1518 弄',
            "remark": ''
        }, {
            "id": 1,
            "latitude": 39.915,
            "longitude": 116.404,
            "date": '2016-05-03',
            "name": '王小虎',
            "address": '上海市普陀区金沙江路 1518 弄',
            "remark": ''
        },{
            "id": '1',
            "latitude": 39.915,
            "longitude": 116.404,
            "date": '2016-05-03',
            "name": '王小虎',
            "address": '上海市普陀区金沙江路 1518 弄',
            "remark": ''
        },{
            "id": 1,
            "latitude": 39.915,
            "longitude": 116.404,
            "date": '2016-05-03',
            "name": '王小虎',
            "address": '上海市普陀区金沙江路 1518 弄',
            "remark": ''
        }]'''

    return t


@app.route('/user/login')
def user_login():
    return "success"


if __name__ == '__main__':
    # app.debug = True
    app.run(port=8080)
