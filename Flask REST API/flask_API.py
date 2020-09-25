from flask import Flask, jsonify, request, json
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
        res_data = request.get_json(silent=True)

        #parse that data 
        day = res_data['day']
        data = res_data['newTodo']

        ## add post data to the todo_list
        addToToDo(data, day)
        ## return posted data 
        return res_data['newTodo']

    else:
        return "hlelo"
        

def addToToDo(newTodo, day):
    global todo_lists
    
    for d in todo_lists:
        if d['day'] == day:
            d['todoList'].append('newTodo')
    print(todo_lists)


if __name__ == '__main__':
    app.run(debug=True)
