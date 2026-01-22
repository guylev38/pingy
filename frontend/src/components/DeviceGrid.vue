<template>
    <q-page-container class="q-pa-md">
        <div class="row q-col-gutter-md">
            <div
                v-for="device in devices"
                class="col-xs-12 col-sm-6 col-md-4 col-lg-3"
            >
                <Device :device="device" />
            </div>
        </div>

        <div v-if="loading" class="text-center q-mt-lg">
            <q-spinner color="primary" size="2em"></q-spinner>
            <div class="q-mt-sm">Loading Devices...</div>
        </div>

        <div
            v-else-if="!devices.length && !loading"
            class="text-center q-mt-lg"
        >
            <q-icon name="devices_other" size="5em" color="grey"></q-icon>
            <div class="text-grey q-mt-sm">No Devices Found</div>
        </div>
    </q-page-container>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import type IDevice from '../types/device';
import Device from './Device.vue';

const loading = ref(false);

const props = defineProps<{ devices: IDevice[] }>();
const devices = ref<IDevice[]>([]);

watch(
    () => props.devices,
    () => {
        devices.value = props.devices;
    }
);
</script>
