<template>
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
                <q-btn label="Cancel" color="primary" v-close-popup></q-btn>
                <q-btn
                    label="Confirm"
                    color="negative"
                    @click="emitConfirm"
                ></q-btn>
            </q-card-actions>
        </q-card>
    </q-dialog>
</template>

<script lang="ts" setup>
import { ref } from 'vue';

const confirmDeleteDevice = ref(false);
const emits = defineEmits<{
    (e: 'confirm'): void;
}>();

function emitConfirm() {
    emits('confirm');
}
</script>
