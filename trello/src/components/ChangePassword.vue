<script>
import axios from 'axios';
import { reactive, ref, toRefs } from 'vue';
import { useProfileStore } from '../stores/profile';

export default {
    name: 'ChangePassword',
    setup() {
        const message = ref('')
        const formData = reactive({
          old_password: '',
          new_password: ''
        })
        const displayMessage = ref('none')
        function ChangePass(){
          const token = JSON.parse(localStorage.getItem('user_token'))
          axios.post('http://127.0.0.1:9000/accounts/change-password', formData, {
            headers: {'Authorization': 'Bearer ' + token}
          }).then(function(response){
            //   profile.name = response.data.name
                message.value = response.data.message
                displayMessage.value = 'block'
                setTimeout(function() {
                message.value = ''
              }, 3000)
          }).catch(function(error){
            console.log(error)
            message.value = "Invalid password"
            displayMessage.value = 'block'
            setTimeout(function() {
                message.value = ''
              }, 3000)
          })
        }
        return {
          ChangePass,
          formData,
          message,
          displayMessage
        }
    },
}
</script>

<template>
<!-- Modal -->
<div class="modal fade" id="ChangePass" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="staticBackdropLabel">Update your profile</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <form @submit.prevent="ChangePass">
        <div class="modal-body popup_div">
            <div>
                <label for="old_password" class="signup-label">Old Password</label>
                <input type="password" class="form-control" name="old_password" id="old_password" v-model="formData.old_password" />
            </div>
            <div>
                <label for="new_password" class="signup-label">New Password</label>
                <input type="password" class="form-control" name="new_password" id="new_password" v-model="formData.new_password" />
            </div>
            <div>
                <span :style="{'display': displayMessage}">{{message}}</span>
            </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn btn-primary">Change</button>
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