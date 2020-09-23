from flask import Flask, jsonify, request 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/todo_lists')
def todoData():
    todo_lists = [
        {
            "day" :-1,
            "todoList" : [{
                "title": "Work on fancy todo list",
                "completed": False
                },
                {
                "title": "Do something cool",
                "completed": True
                },
                ]
        },
        {
            "day" :0,
            "todoList" : [{
                "title": "Work on fancy todo list",
                "completed": False
                }]
        },
        {
            "day" :1,
            "todoList" : [{
                "title": "Work on fancy todo list",
                "completed": False
                }]
        },
        {
            "day" :2,
            "todoList" : [{
                "title": "Work on fancy todo list",
                "completed": False
                },
                {
                "title": "Do something cool",
                "completed": True
                },
                ]
        },
        {
            "day" :3,
            "todoList" : [{
                "title": "Work on fancy todo list",
                "completed": True
                }]
        },

    ]
    return jsonify(todo_lists)

if __name__ == '__main__':
    app.run(debug=True)