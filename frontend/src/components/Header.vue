<template>
    <q-header elevated>
        <q-toolbar class="glossy">
            <q-btn
                flat
                round
                dense
                icon="menu"
                @click="$emit('toggle-left-drawer')"
            />
            <q-toolbar-title>Controller Dashboard</q-toolbar-title>
            <q-btn
                flat
                round
                dense
                icon="menu"
                @click="$emit('toggle-ping-results')"
            ></q-btn>
        </q-toolbar>
    </q-header>
</template>

<script setup></script>
