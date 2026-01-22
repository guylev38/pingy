<template>
    <q-dialog>
        <q-card-section>
            <q-card class="q-pa-md">
                <q-card-section v-if="group == 'single'">
                    <q-form @submit.prevent="submitSingle" ref="singleForm">
                        <q-input
                            v-model="ipAddress"
                            label="IP Address"
                        ></q-input>
                    </q-form>
                </q-card-section>
                <q-card-section v-if="group == 'range'">
                    <q-form @submit.prevent="submitRange" ref="rangeForm">
                        <q-input
                            v-model="startAddress"
                            label="Start Address"
                        ></q-input>
                        <q-input
                            v-model="endAddress"
                            label="End Address"
                        ></q-input>
                    </q-form>
                </q-card-section>
                <q-option-group
                    v-model="group"
                    :options="options"
                    color="primary"
                >
                </q-option-group>
                <q-card-section
                    style="display: flex; gap: 20px; justify-content: center"
                >
                    <q-btn
                        padding="10px"
                        dense
                        label="cancel"
                        color="negative"
                        v-close-popup
                    ></q-btn>
                    <q-btn
                        padding="10px"
                        dense
                        label="Add"
                        v-close-popup
                        @click="submit"
                        color="primary"
                    ></q-btn>
                </q-card-section>
            </q-card>
        </q-card-section>
    </q-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import type IDevice from '../../types/device';
import type IDeviceRange from '../../types/deviceRange';

const emits = defineEmits<{
    (e: 'single', data: IDevice): void;
    (e: 'range', data: IDeviceRange): void;
}>();

const group = ref<'single' | 'range'>('single');
const ipAddress = ref('');
const startAddress = ref('');
const endAddress = ref('');

const currentForm = ref(null);

const options = [
    {
        label: 'Single Device',
        value: 'single',
    },
    {
        label: 'Range of Devices',
        value: 'range',
    },
];

function submit() {
    if (group.value === 'single') {
        submitSingle();
    } else {
        submitRange();
    }
}

function submitSingle() {
    emits('single', { ip: ipAddress.value });
}

function submitRange() {
    emits('range', {
        startAddress: startAddress.value,
        endAddress: endAddress.value,
    });
}
</script>
