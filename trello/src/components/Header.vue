<script>
import { useProfileStore } from '../stores/profile'

export default {
    name: 'Header',
    setup() {
        const profile = useProfileStore()
        
       return {
           profile
       }
    }
}
</script>
<template>
<nav class="navbar navbar-expand-lg navbar-light" style="background-color: #e3f2fd;">
  <a class="navbar-brand" href="#"><img src="@/assets/logo.png" style="height:40px; width: 40px;" /></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <router-link class="nav-link" :to="{name: 'home'}">Home</router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link" :to="{name: 'home'}">Boards</router-link>
      </li>
      
    </ul>
    <ul class="navbar-nav">
        <li class="nav-item dropdown ml-auto profile_dropdown float-right">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            {{profile.email}}
        </a>
        
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          
          <!-- <router-link></router-link> -->
          <a type="button" class="dropdown-item link-item" data-bs-toggle="modal" data-bs-target="#staticBackdrop">Profile</a>
          <a type="button" class="dropdown-item link-item" data-bs-toggle="modal" data-bs-target="#ChangePass">Change Password</a>
          <router-link class="dropdown-item link-item" :to="{name: 'logout'}">Logout</router-link>
        </div>
      </li>
    </ul>
  </div>
</nav>
</template>
<style>
.profile_dropdown>div{
    box-shadow: 2px 2px 2px 2px lightgrey;
    border: none;
    border-radius: 10px;
}
.link-item{
    color: black;
    font-size: 15px;

}
/* .second_nav{
    display: flex;
    flex-direction: row-reverse;
    width: 100%;
    float: right;
} */
</style>