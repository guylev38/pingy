<template>
    <q-layout view="hHh lpR fFf">
        <Header
            @toggle-left-drawer="toggleLeftDrawer"
            @toggle-ping-results="togglePingResults"
        />

        <LeftSidebar
            v-model="leftDrawerOpen"
            @add-device="toggleAddDeviceDialog"
        />
        <DeviceGrid :devices="devices" />
        <PingResults
            v-model="showPingResults"
            :offline-devices="offlineDevices"
        />

        <AddDeviceDialog v-model="showAddDeviceDialog" />
    </q-layout>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import Header from './components/Header.vue';
import LeftSidebar from './components/LeftSidebar.vue';
import DeviceGrid from './components/DeviceGrid.vue';
import PingResults from './components/PingResults.vue';
import AddDeviceDialog from './components/modals/AddDeviceDialog.vue';
import type IDevice from './device';

const leftDrawerOpen = ref(true);
const showPingResults = ref(false);
const devices = ref<IDevice[]>([]);
const offlineDevices = computed(() =>
    devices.value.filter((d) => d.status == false)
);
const showAddDeviceDialog = ref(false);
const newDevice = ref<IDevice>({ ip: '' });

function toggleLeftDrawer() {
    leftDrawerOpen.value = !leftDrawerOpen.value;
}

function togglePingResults() {
    showPingResults.value = !showPingResults.value;
}

function toggleAddDeviceDialog() {
    showAddDeviceDialog.value = !showAddDeviceDialog.value;
}

async function startPing() {}

async function addDevice() {}

async function addDeviceBulk() {}

async function removeDevice() {}

async function fetchDevices() {}

// Timer
</script>
