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
            <q-dialog v-model="confirmDeleteDevice">
                <q-card>
                    <q-card-section class="row items-center">
                        <q-avatar icon="delete" text-color="black"></q-avatar>
                        <br />
                        <div class="text-p">
                            Are you sure you want to delete this device?
                        </div>
                    </q-card-section>
                    <q-card-actions align="center">
                        <q-btn
                            label="Cancel"
                            color="primary"
                            v-close-popup
                        ></q-btn>
                        <q-btn
                            label="Confirm"
                            color="negative"
                            @click="deleteDevice"
                        ></q-btn>
                    </q-card-actions>
                </q-card>
            </q-dialog>
        </q-card-actions>
    </q-card>
</template>

<script setup lang="ts">
import type IDevice from '../types/device';
import { ref } from 'vue';
import { useQuasar } from 'quasar';

const $q = useQuasar();

const confirmDeleteDevice = ref(false);

const deviceProp = defineProps<{ device: IDevice }>();
delete deviceProp.device._id;

async function deleteDevice() {
    try {
        const res = await fetch('http://127.0.0.1:8000/api/delete_device', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(deviceProp.device),
        });

        if (!res.ok)
            throw new Error('Failed to delete device ' + deviceProp.device.ip);

        window.location.reload();
    } catch (err: any) {
        const error = err as Error;
        $q.notify({
            type: 'negative',
            message: error.message,
        });
    } finally {
        confirmDeleteDevice.value = false;
    }
}
</script>
