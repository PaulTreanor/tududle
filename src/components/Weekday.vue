<template>
    <div>
        <h2 class="day">Friday</h2>
        <p class="date">September 18th, 2020</p>
        <AddTodo v-on:add-todo="addTodo"/>

        <!----where the item components will be added --->
        <div v-for="todo in todos " v-bind:key="todo.title"> 
          <TodoItem v-bind:todo='todo' v-on:del-todo="$emit('del-todo', todo.title)"/>
        </div>
    </div>

</template>

<script>
import TodoItem from './TodoItem';
import AddTodo from './AddTodo';

export default {
    name: 'Weekday',
    props: ["todos"],
    components: {
        TodoItem,
        AddTodo
    },
    methods: {
      addTodo(newTodo) {
        this.$emit('add-todo', newTodo);
        console.log(124)
      }
    }
}
</script>

<style scoped>
.day {
	margin: auto;
	text-align: center;
	color: black;
	font-family: 'Oswald', "Helvetica Neue", Helvetica, Arial sans-serif;
	text-transform: uppercase;
	}

.date {
	margin:auto;
	text-align: center;
	padding-bottom: 20px;
	color: black;
}
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