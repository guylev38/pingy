<script setup lang="ts">

import { NGrid, NGridItem } from "naive-ui";
import DeviceCard from "./DeviceCard.vue"

</script> 


<template>
    <n-grid class="devices" responsive="screen" :x-gap="2" :y-gap="2" :cols="3">
        <n-grid-item>
            <DeviceCard ip="192.168.0.2" status="online" lastChecked="yesterday" :ms="10"></DeviceCard>
        </n-grid-item>
        <n-grid-item>
            <DeviceCard ip="192.168.0.8" status="online" lastChecked="yesterday" :ms="10"></DeviceCard>
        </n-grid-item>
        <n-grid-item>
            <DeviceCard ip="192.168.0.11" status="online" lastChecked="yesterday" :ms="10"></DeviceCard>
        </n-grid-item>
        <n-grid-item>
            <DeviceCard ip="192.168.0.11" status="online" lastChecked="yesterday" :ms="10"></DeviceCard>
        </n-grid-item>
        <n-grid-item>
            <DeviceCard ip="192.168.0.11" status="online" lastChecked="yesterday" :ms="10"></DeviceCard>
        </n-grid-item>
    </n-grid>
</template>

<style scoped>
    .devices {
        align-items: center;
        width: 50%;
    }
</style>