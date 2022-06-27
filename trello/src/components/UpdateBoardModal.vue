<script>
import axios from 'axios';
import { inject, reactive, ref } from 'vue';
import { useProfileStore } from '../stores/profile';

export default {
    name: 'UpdateBoardModal',
    props: ['id', 'name', 'description'],
    setup(props) {
        const message = ref('')
        const displayMessage = ref('none')
        const formData = reactive({
          name: '',
          description: ''
        })

        const loadBoard  = inject('loadBoard')

        function updateBoard(id){
          const token = JSON.parse(localStorage.getItem('user_token'))
          axios.put('http://127.0.0.1:9000/board/'+id, {
            name: props.name,
            desscription: props.description
          }, {
            headers: {'Authorization': 'Bearer ' + token}
          }).then(function(response){
              message.value = "Board data updated successfully!"
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
          updateBoard,
          loadBoard,
          message,
          displayMessage,
          formData
        }
    },
}
</script>

<template>
<!-- Modal -->
<div class="modal fade" id="updateBoard" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="staticBackdropLabel">Update board details</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <form @submit.prevent="updateBoard(id)">
        <div class="modal-body popup_div">
            <div>
                <label for="name" class="signup-label">Name</label>
                <input type="text" class="form-control" name="name" id="name" v-model="name"
                 />
            </div>
            <div>
                <label for="description" class="signup-label">Description</label>
                <textarea class="form-control" name="description" id="description" v-model="description"
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