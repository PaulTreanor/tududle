<template>
    <div>
        <h2 class="day">Friday</h2>
        <p class="date">September 18th, 2020</p>
        <form action="" method="get">
            <input type="text" name="todoItem" placeholder="Add todo item"/>
            <input type="submit" style="display:none"/>
        </form>
        <!----where the item components will be added --->
        <div v-for="todo in todos " v-bind:key="todo.title"> 
          <TodoItem v-bind:todo='todo' v-on:del-todo="$emit('del-todo', todo.title)"/>
        </div>
    </div>

</template>

<script>
import TodoItem from './TodoItem';

export default {
    name: 'Weekday',
    props: ["todos"],
    components: {
        TodoItem
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

form {
	padding-top: 10px;
	padding-bottom: 20px;
	padding-left: 10px;
}

input[type=text] {
  width: 95%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}

</style>