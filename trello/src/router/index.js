import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import LoginViewVue from "../views/LoginView.vue";
import ProfileViewVue from "../views/ProfileView.vue";
import SignupView from "../views/SignupView.vue";
import MyBoardViewVue from "../views/MyBoardView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/signup",
      name: "signup",
      component: SignupView,
    },
    {
      path: "/login",
      name: "login",
      component: LoginViewVue,
    },
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/logout',
      name: 'logout'
    },
    {
      path: '/board/:id',
      name: 'board',
      component: MyBoardViewVue
    }
  ],
});

router.beforeEach(async (to, from) => {
  const isAuthenticated = JSON.parse(localStorage.getItem('user_token'))
  if(!isAuthenticated && to.name != 'login' && to.name != 'signup'){
    return {name: 'login'}
  }
  if (isAuthenticated && to.name == 'login'){
    return {name: 'home'}
  }
  if(isAuthenticated && to.name == 'logout'){
    localStorage.clear()
    return {name: 'login'}
  }
})

export default router;
