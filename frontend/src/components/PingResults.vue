<template>
    <q-drawer v-model="togglePingResultValue" side="right" bordered overlay>
        <div
            class="text-h5"
            v-if="offlineDevices.length == 0"
            style="text-align: center; padding: 15px"
            color="neutral"
        >
            No Offline Devices
        </div>
        <div
            v-if="offlineDevices.length > 0"
            style="text-align: center; padding: 20px"
            class="text-h5"
        >
            Ping Results
            <q-badge
                style="text-align: center; padding: 10px"
                color="neutral"
                >{{ offlineDevices[0]?.last_checked }}</q-badge
            >
        </div>
        <q-list v-if="offlineDevices.length > 0">
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
import type Device from '../types/device.ts';

defineProps<{
    offlineDevices: Device[];
}>();

const togglePingResultsEvent = defineEmits(['toggle-ping-results']);
const togglePingResultValue = defineModel<boolean>({ required: true });
</script>
