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

        <AddDeviceDialog
            v-model="showAddDeviceDialog"
            @single="addDeviceToGrid"
            @range="addDeviceBulkToGrid"
        />
    </q-layout>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import Header from './components/Header.vue';
import LeftSidebar from './components/LeftSidebar.vue';
import DeviceGrid from './components/DeviceGrid.vue';
import PingResults from './components/PingResults.vue';
import AddDeviceDialog from './components/modals/AddDeviceDialog.vue';
import { sendPOSTCommand, sendGETCommand } from './utils/api_utils';
import { GETCommands, POSTCommands } from './utils/api_utils';
import type IDevice from './types/device';
import type IDeviceRange from './types/deviceRange';

const leftDrawerOpen = ref(true);
const showPingResults = ref(false);
const showAddDeviceDialog = ref(false);

const devices = ref<IDevice[]>([]);
const offlineDevices = computed(() =>
    devices.value.filter((d) => d.status == false),
);

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

async function addDeviceToGrid(newDevice: IDevice) {
    console.log('Adding new device');
    await sendPOSTCommand(newDevice, POSTCommands.ADD);
}

async function addDeviceBulkToGrid(range: IDeviceRange) {
    let start = getLastOctet(range.startAddress);
    let end = getLastOctet(range.endAddress);

    for (let i = start; i <= end; i++) {}
}

async function removeDevice() {}

async function fetchDevices() {
    await sendGETCommand(GETCommands.DEVICES);
}
// Timer

// Utils
function getLastOctet(ip: string): number {
    return Number(ip.split('.')[3]);
}

function replaceLastOctet(ip: string, newOctet: string): string {
    const parts = ip.split('.');
    parts[3] = newOctet;
    return parts.join('.');
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap');

* {
    font-family: 'Roboto', sans-serif;
}
</style>
