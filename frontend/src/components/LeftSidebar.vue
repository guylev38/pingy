<template>
    <q-drawer v-model="showSidebar" show-if-above bordered class="shadow-10">
        <q-list>
            <q-item-label header>Controls</q-item-label>
            
            <q-item clickable v-ripple @click="startPing">
                <q-item-section avatar>
                    <q-icon name="play_circle"></q-icon>
                </q-item-section>
                <q-item-section>Start Ping</q-item-section>
            </q-item>
            <q-item clickable v-ripple @click="showAddDeviceDialog = true">
                <q-item-section avatar>
                    <q-icon name="add"></q-icon>
                </q-item-section>
                <q-item-section>Add Device</q-item-section>
            </q-item>
            <q-item clickable v-ripple @click="showAddDeviceRangeDialog = true">
                <q-item-section avatar>
                    <q-icon name="create_new_folder"></q-icon>
                </q-item-section>
                <q-item-section>Add Devices by Range</q-item-section>
            </q-item>
        </q-list>
        
        <q-dialog persistent v-model="isPingInProgress">
            <q-card class="q-pa-md" style="min-width: 400px;">
                <div class="text-p" style="align-items: center; display:flex; gap:15px; justify-content: center;">
                    <q-spinner-radio color="primary" size="1.5em"/>
                    Pinging in Progress...
                </div>
            </q-card>
        </q-dialog>
    
        <q-dialog persistent v-model="isAddingDevices">
            <q-card class="q-pa-md" style="min-width: 400px">
                <q-spinner-orbit color="primary" size="1.5em">Adding Devices...</q-spinner-orbit>
            </q-card>
        </q-dialog>

        <q-dialog v-model="showAddDeviceDialog">
            <q-card class="q-pa-md" style="min-width: 400px">
                <q-card-section>
                    <div class="text-h6">add new device</div>
                </q-card-section>

                <q-card-section>
                    <q-form @submit.prevent="addDeviceButton" class="q-gutter-md">
                        <q-input v-model="newDevice.ip" label="device ip" filled required></q-input>
                        <q-card-actions align="right">
                            <q-btn dense label="cancel" color="negative" v-close-popup></q-btn>
                            <q-btn dense label="add" color="primary" v-close-popup type="submit"></q-btn>
                        </q-card-actions>
                    </q-form>
                </q-card-section>
            </q-card> 
        </q-dialog>
        <q-dialog v-model="showAddDeviceRangeDialog">
            <q-card class="q-pa-md" style="min-width: 400px">
                <q-card-section>
                    <div class="text-h6">Add Devices by Range</div>
                </q-card-section>

                <q-card-section>
                    <q-form @submit.prevent="addDeviceBulk" class="q-gutter-md">
                        <q-input v-model="startIp" label="Start IP" filled required></q-input>
                        <q-input v-model="endIp" label="End IP" filled required></q-input>
                        <q-card-actions align="right">
                            <q-btn dense label="cancel" color="negative" v-close-popup></q-btn>
                            <q-btn dense label="add" color="primary" v-close-popup type="submit"></q-btn>
                        </q-card-actions>
                    </q-form>
                </q-card-section>
            </q-card> 
        </q-dialog>
    </q-drawer>
</template>

<script setup lang="ts">
import { useQuasar } from 'quasar';
import { ref, } from 'vue';
import type IDevice from '../device';

const $q = useQuasar()

const showSidebar = defineModel<boolean>({ required: true })
const isPingInProgress = ref(false)
const isAddingDevices = ref(false)
const showAddDeviceDialog = ref(false)
const showAddDeviceRangeDialog = ref(false)

const newDevice = ref<IDevice>({
    ip: ""
})

const startIp = ref<string>('')
const endIp = ref<string>('')

async function startPing(){
    isPingInProgress.value = true
    try{
        const res = await fetch("http://127.0.0.1:8000/api/status")
        if (!res.ok) throw new Error("Ping Failed")
        window.location.reload()
    } catch (err){
       console.error(err) 
    } finally {
        isPingInProgress.value = false
    }
}

async function addDevice(device: IDevice){
    const res = await fetch('http://127.0.0.1:8000/api/add_device', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(device)
    })

    if (!res.ok) throw new Error('Failed to add device! API response: ' + res.json)
}

async function addDeviceButton(){
    try {
        await addDevice(newDevice.value)

        showAddDeviceDialog.value = false;
        window.location.reload() 
    } catch(err) {
        $q.notify({
            type: "negative",
            message: "Failed to add device"
        })
    }

}

async function addDeviceBulk(){
    let start_octet = Number(startIp.value.split('.').pop())
    let end_octet = Number(endIp.value.split('.').pop())
    var address: string =  startIp.value.split('.').slice(0, 3).join('.')

    isAddingDevices.value = true    

    for(let i = start_octet; i<=end_octet; i++){ 
        var current_ip: string = [address, String(i)].join('.')
        try{
            await addDevice({ ip: current_ip })        
        } catch (err) {
            $q.notify({
                type: "negative",
                message: `Failed to add device ${current_ip}, Stopping...`
            })

            return
        }
    }

    isAddingDevices.value = false
}
 
</script>