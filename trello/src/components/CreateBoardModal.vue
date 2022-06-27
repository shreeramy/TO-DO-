<script>
import axios from 'axios';
import { inject, reactive, ref } from 'vue';
import { useProfileStore } from '../stores/profile';

export default {
    name: 'CreateBoardModal',
    setup() {
        const message = ref('')
        const displayMessage = ref('none')
        const formData = reactive({
          name: '',
          description: ''
        })

        const loadBoard  = inject('loadBoard')
        function CreateBoard(){
          const token = JSON.parse(localStorage.getItem('user_token'))
          axios.post('http://127.0.0.1:9000/board/', formData, {
            headers: {'Authorization': 'Bearer ' + token}
          }).then(function(response){
              message.value = response.data.message
              displayMessage.value = 'block'
              loadBoard()
              setTimeout(function() {
                message.value = ''
              }, 3000)
          }).catch(function(error){
            console.log(error)
          })
        }
        return {
          CreateBoard,
          loadBoard,
          message,
          displayMessage,
          formData,
        }
    },
}
</script>

<template>
<!-- Modal -->
<div class="modal fade" id="createBoard" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="staticBackdropLabel">Create new board</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <form @submit.prevent="CreateBoard">
        <div class="modal-body popup_div">
            <div>
                <label for="name" class="signup-label">Name</label>
                <input type="text" class="form-control" name="name" id="name" v-model="formData.name"
                 />
            </div>
            <div>
                <label for="description" class="signup-label">Description</label>
                <textarea class="form-control" name="description" id="description" v-model="formData.description"
                 ></textarea>
            </div>
            <div>
                <span :style="{'display': displayMessage}">{{message}}</span>
            </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn btn-primary">Save</button>
        </div>
      </form>
    </div>
  </div>
</div>
</template>

<style>
.popup_div>form>div>label{
    color: black;
    font-weight: bold;
    font-size: 17px;
}
.popup_div>form>div>input{
    height: 45px;
    margin-bottom: 10px;
    border-radius: 10px;
    margin-top: 2px;
}
</style>