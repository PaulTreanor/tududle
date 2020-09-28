<template>
    <div>
        <Day v-bind:day="day"/>
        
        <AddTodo v-on:add-todo="addTodo" v-bind:day="day"/>   <!------v-bind:day needs to be send so it can be emitted back up--->

        <!----where the item components will be added --->
        <div v-for="todo in todoList " v-bind:key="todo.title"> 
          <TodoItem v-bind:todo='todo' v-bind:day ='day' v-on:del-todo="$emit('del-todo', todo.title, todos.day)" v-on:mark-completed="$emit('mark-completed', todo.title, todos.day)"/>
        </div>
    </div>

</template>

<script>
import TodoItem from './TodoItem';
import AddTodo from './AddTodo';
import Day from './dates/Day';

export default {
    name: 'Weekday',
    props: ["todos"],  //todos is an item with a day and a list of todos
    components: {
        TodoItem, 
        AddTodo,
        Day
    },
    data() {
      return {
        todoList: this.todos.todoList,
        day: this.todos.day
      }
      
    },
    methods: {
      addTodo(newTodo, day) {
        this.$emit('add-todo', newTodo, day);

      }
    }
}
</script>

<style scoped>

/*---------submit button styling -----------*/
.btn {
  display: inline-block;
  border: none;
  background: #555;
  padding: 7px 20px;
  cursor: pointer;
}

.btn:hover {
  background: #666;
}
</style>