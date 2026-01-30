<template>
    <q-card>
        <q-card-section>
            <div class="text-h6">{{ device.ip }}</div>
            <q-badge v-if="device.status == true" color="positive"
                >Online</q-badge
            >
            <q-badge v-if="device.status == null" color="info">Unkown</q-badge>
            <q-badge v-if="device.status == false" color="negative"
                >Offline</q-badge
            >
        </q-card-section>
        <q-card-actions align="right">
            <q-btn
                round
                dense
                color="negative"
                @click="confirmDeleteDevice = true"
            >
                <q-avatar icon="delete" size="2em"></q-avatar>
            </q-btn>
            <ConfirmDeleteDevice
                @confirm="emitDeleteDevice"
            ></ConfirmDeleteDevice>
        </q-card-actions>
    </q-card>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import type IDevice from '../types/device';
import ConfirmDeleteDevice from './modals/ConfirmDeleteDevice.vue';

const confirmDeleteDevice = ref(false);

const deviceProp = defineProps<{ device: IDevice }>();
const deviceEmits = defineEmits<{
    (e: 'delete', data: IDevice): void;
}>();

function emitDeleteDevice() {
    deviceEmits('delete', deviceProp.device);
}
</script>
