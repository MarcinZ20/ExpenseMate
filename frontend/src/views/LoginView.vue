<script setup lang="ts">
import { useAuthStore } from '@/stores/auth.ts'
import { useForm } from 'vee-validate'
import * as yup from 'yup'
import axios from 'axios'

const schema = yup.object({
  email: yup.string().required().email('Email is required'),
  password: yup.string().min(6).required(),
})

const {handleSubmit, defineField } = useForm({
  validationSchema: schema
})

const [email, emailAttrs] = defineField('email', {
  validateOnModelUpdate: false,
  }
)
const [password, passwordAttrs] = defineField('password', {
  validateOnModelUpdate: false,
})

const onSubmit = handleSubmit(values => {
  const auth = useAuthStore()
  auth.login(values.email, values.password)
})
</script>

<template>
  <div class="bg-gray-50 dark:bg-gray-800 min-h-screen content-center align-top ">
    <div class="max-w-sm mx-auto">
      <h1 class="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white">Log in</h1>
    </div>
    <hr class="max-w-sm mx-auto h-px my-8 bg-gray-200 border-0 dark:bg-gray-700">
    <form @submit.prevent="onSubmit" class="max-w-sm mx-auto">
      <div class="mb-5">
        <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your email</label>
        <input type="email" id="email" v-model="email" v-bind="emailAttrs" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@flowbite.com" required />
      </div>
      <div class="mb-5">
        <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your password</label>
        <input type="password" id="password" v-model="password" v-bind="passwordAttrs" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required />
      </div>
      <button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button>
    </form>
  </div>
</template>

<style scoped>

</style>
