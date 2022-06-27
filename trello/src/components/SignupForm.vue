<script>
import {reactive, ref} from 'vue';
import axios from 'axios';
import router from '../router';
export default {
    name: 'SignupForm',
    setup() {
       const formData = reactive({
           name: '',
           email: '',
           password: ''
       })
       function Signup(){
           axios.post('http://127.0.0.1:9000/accounts/signup', {
               name: formData.name,
               email: formData.email,
               password: formData.password
           }).then(function(response){
               console.log("response", response)
               console.log(response.status)
               alert("Registration completed")
               router.push('/login')
           }).catch(function(error){
               console.log("error", error)
           })
       }
       return {
           formData,
           Signup
       }
       
    },
}
</script>

<template>
    <div class="container">
        <div class="signup_div">
            <h2 class="text-center mb-5">Registration Form</h2>
            <form @submit.prevent="Signup">
                <div>
                    <label for="name" class="signup-label">Name</label>
                    <input type="text" name="name" id="name" class="form-control" v-model="formData.name" required />
                </div>
                <div>
                    <label for="email" class="signup-label">Email</label>
                    <input type="email" name="email" id="email" class="form-control" v-model="formData.email" required />
                </div>
                <div>
                    <label for="password" class="signup-label">Password</label>
                    <input type="password" name="password" id="password" class="form-control" v-model="formData.password" required />
                </div>
                <div>
                    <router-link class="btn btn-primary" :to="{name: 'login'}">Login</router-link>
                    <button type="submit" class="btn btn-primary" style="float:right;">Signup</button>
                </div>
            </form>
        </div>
    </div>
</template>
<style>
.signup_div{
    width: 600px;
    height: auto;
    padding: 40px;
    box-shadow: 1px 1px 5px 6px lightgray;
    margin: auto;
    margin-top: 100px;
    border-radius: 20px;
}
.signup_div>form>div>label{
    color: black;
    font-weight: bold;
    font-size: 17px;
}
.signup_div>form>div>input{
    height: 45px;
    margin-bottom: 10px;
    border-radius: 10px;
    margin-top: 2px;
}
</style>