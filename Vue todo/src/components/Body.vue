<template>
    <div class="wrapper">
        <div v-for="todos in todoLists" v-bind:key="todos"> 
          <Weekday v-bind:todos='todos' v-on:del-todo="deleteTodo" v-on:add-todo="addTodo
          "/>
        </div>
    </div>
</template>

<script>
import Weekday from './Weekday';
import axios from 'axios';


export default {
    name: "Body",
    components: {
        Weekday
    },
  data() {
    return {
      todoLists: [
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
        const { title, completed } = newTodo;
        for (var i = 0; i < this.todoLists.length; i ++ ) {
          //this is working to cycle through the days..
          if (this.todoLists[i].day == day) {
            //if the day is right add the item to the list
            axios.post('http://127.0.0.1:5000/todo_lists', {   //we're gonna need to add day in here too so flask knows where to add it
              title,
              completed
            })
              .then(res => this.todoLists[i].todoList.push(res.data))
              .catch(err => console.log(err)).bind(this)  
            
            
          }   
        }
      }
  },
  created() {   //runs immediately on start of program
    axios.get('http://127.0.0.1:5000/todo_lists')
      .then(res => this.todoLists = res.data)
      .catch(err => console.log(err))
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