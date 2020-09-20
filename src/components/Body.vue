<template>
    <div class="wrapper">
        <div > hello</div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
    </div>
</template>

<script>
export default {
    name: "Body"
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