<script>
import axios from 'axios';
import { computed, onBeforeMount, provide, ref } from 'vue';
import { useAuthStore } from '../stores/auth';
import moment from 'moment';
import CreateBoardModal from './CreateBoardModal.vue'
import UpdateBoardModalVue from './UpdateBoardModal.vue';
export default {
    name: 'Board',
    components: {
        CreateBoardModal,
        UpdateBoardModalVue
    },
    setup() {
        const board_data = ref([])
        const name = ref('')
        const description = ref('')
        const id = ref('')
        function created_date(value){
            return moment(value).format("DD-MM-YYYY HH:mm A");
        }
        function loadBoard(){
            const token = JSON.parse(localStorage.getItem('user_token'))
            console.log("board")
            axios.get('http://127.0.0.1:9000/board/', {
                'headers': {'Authorization': 'Bearer ' + token}
            }).then(function(response){
                board_data.value = response.data
            }).catch(function(error){
                console.log(error)
            })
        }
        provide('loadBoard', loadBoard)
        function deleteBoard(id){
            const token = JSON.parse(localStorage.getItem('user_token'))
            axios.delete('http://127.0.0.1:9000/board/'+id,
                {'headers': {'Authorization': 'Bearer '+ token}}
            ).then(function(response){
                console.log(response)
                loadBoard()
            }).catch(function(error){
                console.log(error)
            })
        }
        function getBoard(id1, name1, description1){
            id.value = id1
            name.value = name1,
            description.value = description1
        }
        return {
            loadBoard,
            board_data,
            created_date,
            deleteBoard,
            name,
            description,
            getBoard,
            id
        }
    },
    beforeCreate(){
        this.loadBoard()
    }
}
</script>

<template>
    <div class="container">
        <h3 class="mt-3 mb-3">
            My Boards
        </h3>
        <create-board-modal></create-board-modal>
        <update-board-modal-vue :id="id" :name="name" :description="description"></update-board-modal-vue>
        <div class="row">
            <div class="col-4 mt-3" v-for="data in board_data" :key="data.id">
                
                <div class="board-div">
                    <h3>
                    <router-link :to="{name: 'board', params: {id: data.id}}" class="info-btn">
                        <font-awesome-icon icon="fa fa-info-circle" />
                    </router-link>
                    {{data.name}}
                    <span style="float:right">{{created_date(data.created_at)}}</span>
                    </h3>
                    <p>{{data.desscription}}</p>
                    <div style="text-align:right">
                        
                        <a @click="getBoard(data.id, data.name, data.desscription)" 
                        data-bs-toggle="modal" data-bs-target="#updateBoard" class="edit-btn">
                            <font-awesome-icon icon="fas fa-edit" />
                        </a>
                        <a @click="deleteBoard(data.id)" class="delete-btn">
                            <font-awesome-icon icon="fas fa-trash" />
                        </a>
                    </div>
                </div>
            </div>
            <div class="col-4 mt-3" data-bs-toggle="modal" data-bs-target="#createBoard">
                <div class="create-link">
                    <p>Create new board...</p>
                </div>
                
            </div>
        </div>
    </div>
</template>

<style>
.board-div{
    width: 100%;
    padding: 15px;
    padding-top: 20px;
    padding-bottom: 20px;
    background-color: rgb(0, 174, 255);
    color: white;
    border-radius: 15px;
    text-decoration: none;
    min-height: 150px;

}
.board-div>h3>span{
    font-size: 12px;
    font-style: italic;
    text-decoration: none;
}
.board-div>h3{
    font-size: 16px;
    text-decoration: none;
}
.board-div>div>button{
    font-size: 15px;
}
.board-div>p{
    font-size: 13px;
}
.create-link{
    color: white;
    text-decoration: none;
    background-color: rgb(0, 174, 255);
    font-size: 17px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 15px;
    min-height: 150px;
}
a {
    text-decoration: none;
}
.delete-btn{
    padding-left: 10px;
    color: red;
    font-size: 20px;
}
.info-btn{
    padding-right: 5px;
    color: rgb(134, 238, 134);
}
.edit-btn{
    padding-left: 10px;
    color: blue;
    font-size: 20px;
}
</style>