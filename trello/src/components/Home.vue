<script>
import Header from './Header.vue'
import {useProfileStore} from '../stores/profile.js'
import ProfileEditModal from './ProfileEditModal.vue'
import ChangePassword from './ChangePassword.vue'
import axios from 'axios';
import { onBeforeUpdate, onBeforeMount } from 'vue';
import Board from './Board.vue';
export default {
    name: 'Home',
    components: {
        Header,
        ProfileEditModal,
        ChangePassword,
        Board
    },
    setup() {
        const profile = useProfileStore()
        function ProfileData(){
            const token = JSON.parse(localStorage.getItem('user_token'))
            axios.get('http://127.0.0.1:9000/accounts/profile', {
                'headers': {'Authorization': 'Bearer ' + token}
            }).then(function(response){
              
                profile.name = response.data.name
                profile.email = response.data.email
                  console.log("--------",profile.name)
            }).catch(function(error){
                console.log(error)
            })
       }
       onBeforeMount( () => {
            ProfileData()
            console.log('before mount called')
            console.log(profile.name)
        })
        // onBeforeUpdate( () => {
        //     ProfileData()
        //     console.log('before update called')
        //     console.log(profile.name)
        // })
       return {
           ProfileData,
           profile
       }
    }
    
}
</script>

<template>
   <Header />
   <profile-edit-modal></profile-edit-modal>
   <change-password></change-password>
   <Board></Board>
</template>