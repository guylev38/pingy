<template>
    <q-drawer v-model="modelValue" side="right" bordered overlay>
        <q-btn icon="close" flat dense round @click="$emit('toggle-ping-results')" />
        <div style="text-align: center; padding: 20px;" class="text-h5"> 
            Ping Results
            <q-badge style="text-align: center; padding: 10px;" color="neutral">{{ offlineDevices[0]?.last_checked }}</q-badge>
        </div>
        <q-list>
            <q-item-label header>Offline Devices</q-item-label>

            <q-item v-for="device in offlineDevices" :key="device.ip">
                <q-item-section>
                    {{ device.ip }}
                </q-item-section>
                <q-item-section side>
                    <q-icon name="wifi_off" color="negative"></q-icon>
                </q-item-section>
            </q-item>
        </q-list>
    </q-drawer>
</template>

<script setup lang="ts">
import { defineProps, defineModel } from 'vue';
import type Device from "../device.ts"

defineProps<{
    offlineDevices: Device[]
}>()

const modelValue = defineModel<boolean>({ required: true })

</script>