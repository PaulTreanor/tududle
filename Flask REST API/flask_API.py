from flask import Flask, jsonify, request 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

@app.route('/todo_lists', methods =["GET", "POST"])
def todoData():
    global todo_lists
    if request.method == "GET":
        return jsonify(todo_lists)

    if request.method == "POST":
        
        ## take in post data
        newTodo = request.get_json(silent=True)
        print(newTodo)                  #print response so that can see what you're dealing with
        ## add post data to the todo_list

        ## return posted data 
        return newTodo

    else:
        return "hlelo"
        
if __name__ == '__main__':
    app.run(debug=True)