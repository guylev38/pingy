<script setup lang="ts">
defineProps<{ device: any }>();
</script>

<template>
   <q-card>
        <q-card-section>
            <div class="text-h6">{{ device.ip }}</div>
            <div>Status: {{ device.status ? 'Online' : 'Offline' }}</div>
        </q-card-section> 
   </q-card> 
</template>