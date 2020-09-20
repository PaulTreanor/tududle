<template>
    <div class="todo-item" v-bind:class="{'is_complete':todo.completed}">
        <p v-on:click="markComplete">{{todo.title}}</p>

        <button @click="$emit('del-todo', todo.title)" class="del"><i class='bx bx-trash'></i></button>
    </div>
</template>

<script>
export default {
    name: 'TodoItem',
    props: ['todo'],
    methods: {
        markComplete() {
            this.todo.completed = !this.todo.completed;
        }
    }
}
</script>

<style scoped>
.todo-item{
    background: ;
    padding: 10px;
    border-bottom: 1px #ccc dotted;
    display:grid;
	grid-template-columns: 4fr 1fr;
    cursor: pointer;
}
.is_complete {
    text-decoration: line-through;
    color: #999;
}
.del {
    background: #ff0000;
    color: #ffffff;
    border: none;
    padding: 4px;
    margin: 0;
    border-radius: 10%;
    cursor: pointer;
}

.del:hover {
	background-color: #000;
}

.del:active {
	background-color: #ccc;
	color: #000;
}


</style>