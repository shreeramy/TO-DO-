<script>
import axios from 'axios';
import { reactive, ref } from 'vue';
import { useProfileStore } from '../stores/profile';

export default {
    name: 'ProfileEditModal',
    // data() {
    //   return {
    //       name: ""
    //   }
      
    // },
    setup() {
        const message = ref('')
        const displayMessage = ref('none')
        const profile = useProfileStore()
        const formData = reactive({
          name: profile.name
        })

        
        function EditProfile(){
          const token = JSON.parse(localStorage.getItem('user_token'))
          axios.put('http://127.0.0.1:9000/accounts/profile', formData, {
            headers: {'Authorization': 'Bearer ' + token}
          }).then(function(response){
              profile.name = response.data.name
              message.value = response.data.message
              displayMessage.value = 'block'
              setTimeout(function() {
                message.value = ''
              }, 3000)
          }).catch(function(error){
            console.log(error)
          })
        }
        return {
          EditProfile,
          profile,
          message,
          displayMessage,
          formData,
        }
    },
    beforeMount(){
      const profile = useProfileStore()
      // this.formData.name = profile.name
    }
}
</script>

<template>
<!-- Modal -->
<div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="staticBackdropLabel">Update your profile</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <form @submit.prevent="EditProfile">
        <div class="modal-body popup_div">
            <div>
                <label for="name" class="signup-label">Name</label>
                <input type="text" class="form-control" name="name" id="name" v-model="formData.name"
                 />
            </div>
            <div>
                <span :style="{'display': displayMessage}">{{message}}</span>
            </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
          <button type="submit" class="btn btn-primary">Update</button>
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