<script>
import HeaderVue from './Header.vue'
import Card from './Card.vue'
import CreateCard from './CreateCard.vue'
import { onBeforeMount, provide, ref } from 'vue'
import axios from 'axios'
import { useRoute } from 'vue-router'
import EditTask from './EditTask.vue'
import { VueDraggableNext } from 'vue-draggable-next'
// import draggable from "@/vuedraggable";

export default {
    name: 'MyBoard',
    components: {
        HeaderVue,
        Card,
        CreateCard,
        EditTask,
        draggable: VueDraggableNext,
    },
    setup() {
        const items = ref([])
        const done = ref([])
        const Inprogress = ref([])
        const task_id = ref('')
        const name = ref('')
        const description = ref('')
        const route = useRoute()
        const board_name = ref('')
        function loadTask(){
            const token = JSON.parse(localStorage.getItem('user_token'))
            axios.get('http://127.0.0.1:9000/board/tasks/'+route.params.id, {
                headers: {'Authorization': 'Bearer ' + token}
            }).then(function(response){
                items.value = response.data.todo
                console.log("data", response.data)
                done.value = response.data.done
                Inprogress.value = response.data.inprogress
                board_name.value = response.data.board.name
            }).catch(function(error){
                console.log(error)
            })
        }
        provide('loadTask', loadTask)
        function deleteTask(id){
            const token = JSON.parse(localStorage.getItem('user_token'))
            axios.delete('http://127.0.0.1:9000/board/task/'+id,
                {'headers': {'Authorization': 'Bearer '+ token}}
            ).then(function(response){
                console.log(response)
                loadTask()
            }).catch(function(error){
                console.log(error)
            })
        }
        function changeStatus(event){
            console.log("event is fire", event.item._underlying_vm_.pk)
            console.log(event.to.id)
            const token = JSON.parse(localStorage.getItem('user_token'))
            axios.put('http://127.0.0.1:9000/board/task-status/'+event.item._underlying_vm_.pk, {
                status: event.to.id
            }, {
                headers: {'Authorization': 'Bearer ' + token}
            }).then(function(response){
                console.log('status changed')
            }).catch(function(error){
                console.log(error)
            })
        }
        function getTask(id1, name1, description1){
            console.log("get task called", id1)
            task_id.value = id1
            name.value = name1
            description.value = description1
            console.log(task_id.value)
        }
        onBeforeMount( () => {
            loadTask()
        })
        return {
            items,
            Inprogress,
            done,
            loadTask,
            deleteTask,
            name,
            description,
            getTask,
            task_id,
            board_name,
            changeStatus
        }
    },
}
</script>

<template>
   <header-vue></header-vue>
   <create-card></create-card>
   <edit-task :name="name" :description="description" :task_id="task_id"></edit-task>
   <div class="container mt-5">
       <h3 class="mb-3">
           {{board_name}}
       </h3>
       <div class="row">
           <card title="Todo">
               <draggable :list="items" group="tasks" v-model="items" @end="changeStatus($event)" id="TODO">
                    <div v-for="data in items" :key="data.id" class="task">
                        <h6>{{data.name}}
                            <span style="float:right">
                                <a @click="deleteTask(data.pk)" style="font-size:12px; color:red;">
                                    <font-awesome-icon icon="fas fa-trash" />
                                </a> |
                                <a @click="getTask(data.pk, data.name, data.description)"
                                style="font-size:12px; color:blue;" data-bs-toggle="modal" data-bs-target="#TaskEdit">
                                    <font-awesome-icon icon="fas fa-edit" />
                                </a>
                            </span>
                        </h6>
                        <p>{{data.description}}</p>
                    </div>
               </draggable>
           </card>
           <card title="Inprogress">
               <draggable v-model="Inprogress" group="tasks" @end="changeStatus($event)" id="INPROGRESS">
                    <div v-for="data in Inprogress" :key="data.id" class="task" @drop="changeStatus(data.pk)">
                        <h6>{{data.name}}
                            <span style="float:right">
                                <a @click="deleteTask(data.pk)" style="font-size:12px; color:red;">
                                    <font-awesome-icon icon="fas fa-trash" />
                                </a> |
                                <a @click="getTask(data.pk, data.name, data.description)" 
                                style="font-size:12px; color:blue;" data-bs-toggle="modal" data-bs-target="#TaskEdit">
                                    <font-awesome-icon icon="fas fa-edit" />
                                </a>
                            </span>
                        </h6>
                        <p>{{data.description}}</p>
                    </div>
               </draggable>
           </card>
           <card title="Done">
               <draggable v-model="done" group="tasks" @end="changeStatus($event)" id="DONE">
                    <div v-for="data in done" :key="data.id" class="task">
                        <h6>{{data.name}}
                            <span style="float:right">
                                <a @click="deleteTask(data.pk)" style="font-size:12px; color:red;">
                                    <font-awesome-icon icon="fas fa-trash" />
                                </a> |
                                <a @click="getTask(data.pk, data.name, data.description)" 
                                style="font-size:12px; color:blue;" data-bs-toggle="modal" data-bs-target="#TaskEdit">
                                    <font-awesome-icon icon="fas fa-edit" />
                                </a>
                            </span>
                        </h6>
                        <p>{{data.description}}</p>
                    </div>
               </draggable>
           </card>
       </div>
   </div>
</template>

<style>
.task{
    min-height: 80px;
    background-color: rgb(240, 222, 222);
    border-radius: 10px;
    padding: 10px;
    margin-top: 10px;
}
.task>h6{
    font-size: 15px;
}
.task>p{
    font-size: 12px;
}
a:hover{
    cursor: pointer;
}
</style>