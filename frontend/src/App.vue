<script setup lang="ts">
/*
  App.vue for Pingy.

  Author: guylev38
  Date: 24/09/2025
*/

import { ref } from "vue";
import type { GlobalTheme } from "naive-ui";
import { NFlex, NConfigProvider } from "naive-ui";
import Devices from "./components/Devices.vue"
import Sidebar from "./components/Sidebar.vue"

const theme = ref<GlobalTheme | null>(null)

</script>

<template>
  <n-config-provider :theme="theme" style="height: 100%; width: 100%">
    <n-flex class="app-root" style="height: 100%; width: 100%;">
      <Sidebar></Sidebar>
      <Devices></Devices>
    </n-flex>
  </n-config-provider>
</template>

