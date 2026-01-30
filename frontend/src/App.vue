<template>
    <q-layout view="hHh lpR fFf">
        <Header
            @toggle-left-drawer="toggleLeftDrawer"
            @toggle-ping-results="togglePingResults"
        />

        <LeftSidebar
            v-model="leftDrawerOpen"
            @add-device="toggleAddDeviceDialog"
            @start-ping="
                updateDevices(async () => {
                    await startPing();
                })
            "
        />
        <DeviceGrid :devices="devices" />
        <PingResults
            v-model="showPingResults"
            :offline-devices="offlineDevices"
        />

        <AddDeviceDialog
            v-model="showAddDeviceDialog"
            @single="
                updateDevices(async (device) => {
                    await addSingleDevice(device);
                }, $event)
            "
            @multiple="
                updateDevices(async (range) => {
                    await addMultipleDevices(range);
                }, $event)
            "
        />
    </q-layout>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import Header from './components/Header.vue';
import LeftSidebar from './components/LeftSidebar.vue';
import DeviceGrid from './components/DeviceGrid.vue';
import PingResults from './components/PingResults.vue';
import AddDeviceDialog from './components/modals/AddDeviceDialog.vue';
import { sendPOSTCommand, sendGETCommand } from './utils/api_utils';
import { GETCommands, POSTCommands } from './utils/api_utils';
import type { ApiResponse } from './utils/api_utils';
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

async function startPing() {
    await sendGETCommand(GETCommands.STATUS);
}

async function addSingleDevice(newDevice: IDevice | undefined) {
    await sendPOSTCommand(newDevice, POSTCommands.ADD);
}

async function addMultipleDevices(range: IDeviceRange | undefined) {
    if (range === undefined) {
        throw new Error('Undefined Range!');
    }

    let start = getLastOctet(range.startAddress);
    let end = getLastOctet(range.endAddress);

    const promises: Promise<ApiResponse>[] = [];

    for (let i = start; i <= end; i++) {
        const curr_ip = replaceLastOctet(range.startAddress, String(i));
        promises.push(sendPOSTCommand({ ip: curr_ip }, POSTCommands.ADD));
    }

    await Promise.all(promises);
}

async function removeDevice(device: IDevice) {
    await sendPOSTCommand(device, POSTCommands.DELETE);
}

async function fetchDevices() {
    devices.value = await sendGETCommand(GETCommands.DEVICES);
}

async function updateDevices<T extends any[]>(
    action: (...payload: T) => Promise<void>,
    ...data: T
): Promise<void> {
    try {
        await action(...data);
    } catch (error) {
        console.error('Mutation Failed: ', error);
    } finally {
        await fetchDevices();
    }
}

// Utils
function getLastOctet(ip: string): number {
    return Number(ip.split('.')[3]);
}

function replaceLastOctet(ip: string, newOctet: string): string {
    const parts = ip.split('.');
    parts[3] = newOctet;
    return parts.join('.');
}

onMounted(fetchDevices);
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap');

* {
    font-family: 'Roboto', sans-serif;
}
</style>
