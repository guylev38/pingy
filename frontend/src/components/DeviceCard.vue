<script setup lang="ts">
import { NCard, NTag } from "naive-ui"

type deviceCardProps = {
    ip: string
    status: "online" | "offline"
    lastChecked: string
    ms: number;
}

defineProps<deviceCardProps>()
</script>

<template>
    <n-card :title="ip" size="small" bordered>
        <n-tag type="success" v-if="status === 'online'">Online</n-tag>
        <n-tag type="error" v-else>Offline</n-tag>
    </n-card>
</template>