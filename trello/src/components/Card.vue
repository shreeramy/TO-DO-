<script>
export default {
    name: 'Card',
    props: ['title'],
    setup() {
        
    },
}
</script>

<template>
    <div class="col-4">
        <div class="card-div p-3 pb-5">
            <h5 class="text-center pt-3">{{title}}</h5>
            <!-- <hr /> -->
            <div>
                <slot></slot>
            </div>
            <template v-if="title == 'Todo'">
                <a class="create-task" data-bs-toggle="modal" data-bs-target="#createTask">Add Task...</a>
            </template>
            
        </div>
    </div>
</template>

<style>
.card-div{
    background-color: white;
    box-shadow: 2px 2px 5px 5px lightgrey;
    min-height: 450px;
    width: 100%;
    border-radius: 15px;
    position: relative;
}
.create-task{
    color: blue;
    text-decoration: none;
    bottom: 10px;
    position: absolute;
}
.create-task:hover{
    cursor: pointer;
}
</style>