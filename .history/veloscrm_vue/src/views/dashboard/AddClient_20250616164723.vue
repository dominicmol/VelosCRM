<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add client</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Name</label>
                        <div class="control">
                            <input
                                type="text"
                                class="input"
                                v-model="name"
                                placeholder="Enter client name"
                                required
                            />
                        </div>
                    </div>

                    <div class="field">
                        <label>Contact person</label>
                        <div class="control">
                            <input
                                type="text"
                                class="input"
                                v-model="contact_person"
                                placeholder="Enter contact person"
                                required
                            />
                        </div>
                    </div>

                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input
                                type="email"
                                class="input"
                                v-model="email"
                                placeholder="example@client.com"
                            />
                        </div>
                    </div>

                    <div class="field">
                        <label>Phone</label>
                        <div class="control">
                            <input
                                type="text"
                                class="input"
                                v-model="phone"
                                placeholder="Enter phone number"
                            />
                        </div>
                    </div>

                    <div class="field">
                        <label>Website</label>
                        <div class="control">
                            <input
                                type="text"
                                class="input"
                                v-model="website"
                                placeholder="https://"
                            />
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button type="submit" class="button velos-button">
                                Submit
                            </button>
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
    name: 'AddClient',
    data() {
        return {
            name: '',
            contact_person: '',
            email: '',
            phone: '',
            website: ''
        }
    },
    methods: {
        async submitForm() {
            this.$store.commit('setIsLoading', true)

            const client = {
                name: this.name,
                contact_person: this.contact_person,
                email: this.email,
                phone: this.phone,
                website: this.website
            }

            try {
                await axios.post('/clients/', client)
                toast({
                    message: 'The client was added',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: 'bottom-right',
                })
                this.$router.push('/dashboard/clients')
            } catch (error) {
                console.error('Error adding client:', error)
                toast({
                    message: 'Failed to add client',
                    type: 'is-danger',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 3000,
                    position: 'bottom-right',
                })
            } finally {
                this.$store.commit('setIsLoading', false)
            }
        }
    }
}
</script>

<style scoped>
.button.velos-button {
    background-color: #a41917;
    color: #fff;
    font-weight: bold;
    border-radius: 6px;
    border: none;
    transition: background-color 0.3s ease;
}

.button.velos-button:hover {
    background-color: #841614;
}
</style>
