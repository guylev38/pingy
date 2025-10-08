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
            <q-item clickable v-ripple @click="addDevice">
                <q-item-section avatar>
                    <q-icon name="add"></q-icon>
                </q-item-section>
                <q-item-section>Add Device</q-item-section>
            </q-item>
            <q-item clickable v-ripple @click="promptAddTag">
                <q-item-section avatar>
                    <q-icon name="label"></q-icon>
                </q-item-section>
                <q-item-section>Add Tag</q-item-section>
            </q-item>

            <q-item-label header>Tags</q-item-label>
        
            <q-dialog v-model="showAddDeviceDialog">
                <q-form @submit.prevent="submitForm" class="q-gutter-md">
                    <q-input v-model="device.ip" label="Device IP" filled required></q-input>
                </q-form>
            </q-dialog>

        </q-list>
    </q-drawer>
</template>

<script setup lang="ts">
import { useQuasar } from 'quasar';
import { reactive } from 'vue';
import Device from './Device.vue';

const $q = useQuasar()

const showSidebar= defineModel<boolean>({ required: true })
const device = reactive({

})

/* TODO: Add API Calls*/

function startPing(){
    $q.notify({ message: 'Ping Started!', color: 'primary'})
}

function addDevice(){
    $q.notify({ message: 'Adding Device', color: 'primary'})
}

function promptAddTag(){
    $q.dialog({
        title: 'Add Tag',
        prompt: {
            model: '',
            type: 'text'
        },
        cancel: true,
        persistent: true
    }).onOk((tagName: string) => {
        if(tagName.trim()){
            $q.notify({message: `${tagName.trim()} Added!`})
        }
    })
}
</script>