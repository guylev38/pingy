<template>
    <q-dialog>
        <q-card-section>
            <q-card class="q-pa-md">
                <q-card-section v-if="group == 'single'">
                    <q-form @submit.prevent="submitSingle">
                        <q-input
                            v-model="ipAddress"
                            label="IP Address"
                        ></q-input>
                    </q-form>
                </q-card-section>
                <q-card-section v-if="group == 'range'">
                    <q-form @submit.prevent="submitRange">
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
                <q-card-section align="center" style="display: flex; gap: 20px">
                    <q-btn
                        dense
                        label="cancel"
                        color="negative"
                        v-close-popup
                    ></q-btn>
                    <q-btn
                        dense
                        label="Add"
                        v-close-popup
                        type="submit"
                        color="primary"
                    ></q-btn>
                </q-card-section>
            </q-card>
        </q-card-section>
    </q-dialog>
</template>

<script setup lang="ts">
import { ref, defineEmits } from 'vue';

const group = ref('single');
const ipAddress = ref('');
const startAddress = ref('');
const endAddress = ref('');

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

function submitSingle() {}

function submitRange() {}
</script>
