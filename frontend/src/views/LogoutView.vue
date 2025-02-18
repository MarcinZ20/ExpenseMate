<script setup lang="ts">
import router from '@/router';

const onMainPageClick = () => {
    router.push('/')
}
</script>

<template>
    <div class="text-center margin-auto">
        <article class="prose lg-prose-xl m-2">
            <h1>You've been logged out.</h1>
        </article>
        <button @click='onMainPageClick' class="p-2 m-2 text-white bg-purple rounded">
            Back to main page
        </button>
    </div>
</template>

<style>
</style>