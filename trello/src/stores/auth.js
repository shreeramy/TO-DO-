import {defineStore} from 'pinia';

export const useAuthStore = defineStore({
    id: "auth",
    state: () => ({
        user_token: null
    })
})