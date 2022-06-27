<script>
import axios from 'axios';
import { reactive } from 'vue';
import router from '../router';
import { useAuthStore } from '../stores/auth';

export default {
    name: 'LoginForm',
    setup(){
        const formData = reactive({
            email: '',
            password: ''
        })
        const auth = useAuthStore()
        function login(){
            axios.post('http://127.0.0.1:9000/api/token/', 
                formData
            ).then(function(response){
                auth.user_token = response.data.access
                localStorage.setItem('user_token', JSON.stringify(response.data.access))
                router.push('/')
            }).catch(function(){
                console.log(error)
            })
        }
        return {
            formData,
            login
        }
    }
}
</script>
<template>
    <div class="container">
        <div class="signup_div">
            <h2 class="text-center mb-5">Login Form</h2>
            <form @submit.prevent="login">
                <div>
                    <label for="email" class="signup-label">Email</label>
                    <input type="email" name="email" id="email" class="form-control" v-model="formData.email" required />
                </div>
                <div>
                    <label for="password" class="signup-label">Password</label>
                    <input type="password" name="password" id="password" class="form-control" v-model="formData.password" required />
                </div>
                <div>
                    <router-link class="btn btn-primary" to="/signup">Register</router-link>
                    <button type="submit" class="btn btn-primary" style="float:right;">Login</button>
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