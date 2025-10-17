<template>
    <q-drawer v-model="showSidebar" show-if-above bordered class="shadow-10">
        <q-list>
            <q-item-label header>Controls</q-item-label>
            
            <q-item clickable v-ripple @click='$emit("start-ping")'>
                <q-item-section avatar>
                    <q-icon name="play_circle"></q-icon>
                </q-item-section>
                <q-item-section>Start Ping</q-item-section>
            </q-item>
            <q-item clickable v-ripple @click='$emit("add-device")'>
                <q-item-section avatar>
                    <q-icon name="add"></q-icon>
                </q-item-section>
                <q-item-section>Add Device</q-item-section>
            </q-item>
        </q-list>
    </q-drawer>
</template>

<script setup lang="ts">
const showSidebar = defineModel<boolean>({ required: true })
const emit = defineEmits(['start-ping', 'add-device'])
</script>