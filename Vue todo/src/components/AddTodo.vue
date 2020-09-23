<template>
    <form @submit="addTodo">
        <input type="text" name="title" placeholder="Add todo..." v-model="title"/>
        <input type="submit" value="submit" style="display:none" />
    </form>
</template>

<script>
export default {
    name: 'AddTodo',
    props: ['day'],
    data() {
      return {
        title: ''
      }
    },
    methods: {
      addTodo(e) {
        e.preventDefault();
        const newTodo = {
          title: this.title,
          completed: false
        }
        //send to parent componenet 
        this.$emit('add-todo', newTodo, this.day);
      }
    }
}
</script>

<style scoped>

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