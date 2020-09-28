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

@app.route('/todo_lists/<int:day>/<string:title>', methods =["DELETE", "PATCH"])
def deleteTodo(day, title):
    if request.method == "DELETE":
        deleteFromTodo(day, title)
        return "hello"
    if request.method =="PATCH":
        markComplete(day, title)
        return "hello"
    else:
        return "hlelo"

@app.route('/todo_lists', methods =["GET", "POST", "DELETE"])
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

    
        

def addToToDo(data, day):   #ads post data to global todo_list
    global todo_lists

    for d in todo_lists:
        if d['day'] == day:
            d['todoList'].append(data   )
            print(d)

def deleteFromTodo(day, title):
    global todo_lists

    for d in todo_lists:
        if d['day'] == day:
            print(d)
            for item in d['todoList']:
                if item["title"] == title:
                    d['todoList'].remove(item)
            print(d)
            break

def markComplete(day, title):
    global todo_lists

    for d in todo_lists:
        if d['day'] == day:
            for item in d['todoList']:
                if item["title"] == title:
                    if item["completed"] == True:
                        item["completed"] = False
                    else:
                        item["completed"] = True
            print(d)
            break

if __name__ == '__main__':
    app.run(debug=True)
