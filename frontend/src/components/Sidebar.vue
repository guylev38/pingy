<script setup lang="ts">
import { NFlex, NButton } from 'naive-ui';
</script>

<template>
    <n-flex vertical class="sidebar" align="center">
        <h1>Pingy</h1>
        <n-button type="success">Start Ping</n-button>
        <n-button type="info">Get Device</n-button>
        <n-button secondary>Add Device</n-button>
        <n-button type="default" round>Settings</n-button>
    </n-flex>
</template>

<style scoped>
    .sidebar{
        padding: 20px;
        height: 100%;
        width: 10%;
        border: 3px solid black;
    }
</style>