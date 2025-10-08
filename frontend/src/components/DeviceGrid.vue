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

    </q-page-container>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue"
import Device from "./Device.vue"
import { useQuasar } from 'quasar'

interface device {
    ip: string,
    status: boolean,
    tags?: Array<string>
} 

const $q = useQuasar()
const devices = ref<device[]>([])
const loading = ref(true)


const fetchDevices = async () => {
    try{
        const res = await fetch('http://127.0.0.1:8000/api/devices')
        if (!res.ok) throw new Error('Failed to fetch devices')
        const data = await res.json()
        devices.value = data.devices || data 
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