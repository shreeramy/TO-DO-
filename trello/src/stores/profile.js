import {defineStore} from 'pinia';

export const useProfileStore = defineStore({
    id: 'profile',
    state: () => {
        return {
            name: '',
            email: ''
        }
    }
})