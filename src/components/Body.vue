<template>
    <div class="wrapper">
        <div v-for="todos in todoLists" v-bind:key="todos"> 
          <Weekday v-bind:todos='todos' v-on:del-todo="deleteTodo" v-on:add-todo="addTodo"/>
        </div>
    </div>
</template>

<script>
import Weekday from './Weekday';

export default {
    name: "Body",
    components: {
        Weekday
    },
  data() {
    return {
      todoLists: [
       {
         day: "yesterday",
         todoList: [
           {
          title: "Work on fancy todo list",
          completed: false
        }
         ]
       },
       {
         day: "today",
         todoList: [
           {
          title: "Work on fancy todo list",
          completed: false
        },
        {
          title: "call doctor about covid test",
          completed: false
        }
         ]
       },
       {
         day: "tomorrow",
         todoList: [
           {
          title: "Have some fun",
          completed: false
        }
         ]
       },
       {
         day: "dayAfterTomorrow",
         todoList: [
           {
          title: "Work on cool project",
          completed: false
        }
         ]
       },
       {
         day: "twoDaysFromNow",
         todoList: [
           {
          title: "Work on cool stuff",
          completed: false
        }
         ]
       }
      ]
    }
  },
  methods : {
      deleteTodo(title, day) {
        for (var i = 0; i < this.todoLists.length; i ++ ) {
          //this is working to cycle through the days..
          if (this.todoLists[i].day == day) {
            //find the item with the right title, remove 1 of that item from the list
            for (var j = 0; j < this.todoLists[i].todoList.length; j++) {
              if (this.todoLists[i].todoList[j].title == title) {
                this.todoLists[i].todoList.splice(j, 1);
              }
            }
          }   
        }
      },
      addTodo(newTodo, day) {
        console.log(newTodo, day);
        for (var i = 0; i < this.todoLists.length; i ++ ) {
          //this is working to cycle through the days..
          if (this.todoLists[i].day == day) {
            //if the day is right add the item to the list
            console.log("hello")
            this.todoLists[i].todoList.push(newTodo)
          }   
        }
      }
  }
}
</script>

<style scoped>
.wrapper {
	display:grid;
	grid-template-columns: 4fr 4fr 4fr 4fr 4fr;
	grid-auto-rows: 500px;
	/*padding: 0px 10px 0px 10px;*/
}

.wrapper > div{
	border-left:	#CCC 1px solid;
	border-right:	#CCC 1px solid;
}
</style>