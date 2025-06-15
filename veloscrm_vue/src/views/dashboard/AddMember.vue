<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add member</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input
                                type="email"
                                name="email"
                                class="input"
                                v-model="username"
                                placeholder="example@velos.nl"
                            >
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input
                                type="password"
                                name="password1"
                                class="input"
                                v-model="password1"
                                placeholder="Enter password"
                            >
                        </div>
                    </div>

                    <div class="field">
                        <label>Repeat password</label>
                        <div class="control">
                            <input
                                type="password"
                                name="password2"
                                class="input"
                                v-model="password2"
                                placeholder="Repeat password"
                            >
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" :key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button type="submit" class="button velos-button">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'AddMember',
    data() {
        return {
            username: '',
            password1: '',
            password2: '',
            errors: []
        }
    },
    methods: {
        async submitForm() {
            this.errors = []

            if (this.username === '') {
                this.errors.push('The username is missing')
            }

            if (this.password1 === '') {
                this.errors.push('The password is too short')
            }

            if (this.password1 !== this.password2) {
                this.errors.push('The password are not matching')
            }

            if (!this.errors.length) {
                this.$store.commit('setIsLoading', true)

                const formData = {
                    username: this.username,
                    password: this.password1
                }

                await axios
                    .post('/api/v1/users/', formData)
                    .then(response => {
                        toast({
                            message: 'The member was added',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

                        const emailData = { email: this.username }

                        axios
                            .post('/api/v1/teams/add_member/', emailData)
                            .then(() => {
                                this.$router.push({ name: 'Team' })
                            })
                            .catch(error => {
                                if (error.response) {
                                    for (const property in error.response.data) {
                                        this.errors.push(`${property}: ${error.response.data[property]}`)
                                    }
                                } else if (error.message) {
                                    this.errors.push('Something went wrong. Please try again!')
                                }
                            })
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again!')
                        }
                    })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
}
</script>

<style scoped>
.button.velos-button {
    background-color: #a41917;
    color: white;
    font-weight: bold;
    border-radius: 6px;
    border: none;
    transition: background-color 0.3s ease;
}

.button.velos-button:hover {
    background-color: #841614;
}
</style>
