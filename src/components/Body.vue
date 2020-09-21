<template>
    <div class="wrapper">
        <Weekday />
        <Weekday />
        <Weekday v-bind:todos="todos" v-on:del-todo="deleteTodo" v-on:add-todo="addTodo"/>
        <Weekday />
        <Weekday />
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
      todos: [
        {
          title: "Work on fancy todo list",
          completed: false
        },
        {
          title: "Play DnD with the dudes",
          completed: true
        },
        {
          title: "call doctor about covid test",
          completed: false
        }
      ]
    }
  },
  methods : {
      deleteTodo(title) {
          this.todos = this.todos.filter(todo => todo.title !== title);
      },
      addTodo(newTodo) {
        this.todos = [...this.todos, newTodo]
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