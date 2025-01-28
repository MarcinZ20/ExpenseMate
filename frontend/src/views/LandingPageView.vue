<script setup lang="ts">

import NavbarComponent from '@/components/NavbarComponent.vue'
import HeroSection from '@/components/HeroSection.vue'
import FeaturesSection from '@/components/FeaturesSection.vue'
import TeamSection from '@/components/TeamSection.vue'
import CtaSection from '@/components/CtaSection.vue'
import FooterSection from '@/components/FooterSection.vue'
</script>

<template>
  <div class="bg-cwhite">
    <NavbarComponent/>
    <HeroSection/>
    <hr class="h-px mx-auto max-w-lg my-8 bg-purple-200 border-2 dark:bg-gray-700">
    <FeaturesSection/>
    <hr class="h-px mx-auto max-w-lg my-8 bg-gray-200 border-2 dark:bg-gray-700">
    <TeamSection/>
    <hr class="h-px mx-auto max-w-lg my-8 bg-gray-200 border-2 dark:bg-gray-700">
    <CtaSection/>
    <FooterSection/>
  </div>
</template>
