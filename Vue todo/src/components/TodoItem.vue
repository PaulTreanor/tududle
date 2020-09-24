<template>
    <div class="todo-item" v-bind:class="{'is_complete':todo.completed,'greyedout':day==-1, 'redout':day==0}">
        <p v-on:click="markComplete">{{todo.title}}</p>

        <button @click="$emit('del-todo', todo.title)" class="del"><i class='bx bx-trash'></i></button>
    </div>
</template>

<script>
export default {
    name: 'TodoItem',
    props: ['todo', 'day'],
    methods: {
        markComplete() {
            this.todo.completed = !this.todo.completed;
            //emit flag to call a method to update flask
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
.greyedout {
    color: #888 !important;
}

.redout {
    color: red;
}
.is_complete {
    text-decoration: line-through;
    color: #999;
}
</style>