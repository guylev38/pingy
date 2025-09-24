<script setup lang="ts">

import { NFlex } from "naive-ui";
import DeviceCard from "./DeviceCard.vue"

</script> 


<template>
    <n-flex vertical justify="center">
        <DeviceCard ip="192.168.0.2" status="online" lastChecked="yesterday" :ms="10"></DeviceCard>
        <DeviceCard ip="192.168.0.8" status="online" lastChecked="yesterday" :ms="10"></DeviceCard>
        <DeviceCard ip="192.168.0.11" status="online" lastChecked="yesterday" :ms="10"></DeviceCard>
    </n-flex>
</template>