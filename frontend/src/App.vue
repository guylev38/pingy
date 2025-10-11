<template>
  <q-layout view="hHh lpR fFf">
    <Header @toggle-left-drawer="toggleLeftDrawer" />

    <LeftSidebar v-model="leftDrawerOpen" />
    <DeviceGrid />


  </q-layout>
</template>

<script setup lang="ts">

import { ref } from "vue"
import Header from "./components/Header.vue"
import LeftSidebar from "./components/LeftSidebar.vue"
import DeviceGrid from "./components/DeviceGrid.vue"

const leftDrawerOpen = ref(true)

function toggleLeftDrawer(){
  leftDrawerOpen.value = !leftDrawerOpen.value
}


</script>

<style>
</style>