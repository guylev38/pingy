<template>
    <q-page-container class="q-pa-md">
       <div class="row q-col-gutter-md">
            <div 
                v-for="device in devices"
                class="col-xs-12 col-sm-6 col-md-4 col-lg-3">
                <Device :device="device"/>
            </div> 
        </div>

        <div v-if="loading" class="text-center q-mt-lg">
            <q-spinner color="primary" size="2em"></q-spinner>
            <div class="q-mt-sm">Loading Devices...</div>
        </div>

        <div v-else-if="!devices.length && !loading" class="text-center q-mt-lg">
            <q-icon name="devices_other" size="3em" color="grey"></q-icon>
            <div class="text-grey q-mt-sm">No Devices Found</div>
        </div>
    
        <PingResults v-model="isPingResultsOpen" :offlineDevices="offlineDevices" @toggle-ping-results="closePingResults"/>
    </q-page-container>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from "vue"
import type IDevice from "../device"
import Device from "./Device.vue"
import PingResults from "./PingResults.vue"
import { useQuasar } from 'quasar'

const $q = useQuasar()
const devices = ref<IDevice[]>([])
const loading = ref(true)
const isPingResultsOpen = ref(false)

const offlineDevices = computed(() => devices.value.filter(d => d.status == false))

function closePingResults(){
    isPingResultsOpen.value = false
}

async function fetchDevices() {
    try{
        const res = await fetch('http://127.0.0.1:8000/api/devices')
        if (!res.ok) throw new Error('Failed to fetch devices')
        const data = await res.json()
        devices.value = data.devices || data 

        if(offlineDevices.value.length > 0) isPingResultsOpen.value = true
    } catch (err: any){
        console.error(err)
        $q.notify({
            type: 'negative',
            message: 'Failed to load devices',
            position: 'top-right'
        })
    } finally {
        loading.value = false
    }
}

onMounted(fetchDevices)

</script>