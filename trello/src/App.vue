<script>
import {useProfileStore} from './stores/profile.js'
import axios from 'axios';
export default{
  setup() {
      const client = axios.create({
            baseURL: import.meta.env.API_URL
        });
        console.log("env variable --- ", import.meta.env.API_URL)
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
       return {
           ProfileData,
           profile
       }
    },
    beforeMount() {
        this.ProfileData()
        console.log('before mount called')
        console.log(this.profile.name)
    }
}
</script>

<template>
  <router-view></router-view>
</template>

<style>
@import "@/assets/base.css";
</style>