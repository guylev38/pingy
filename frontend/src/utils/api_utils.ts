/*

Utils for interaction with the pingy backend api.

:author: guylev38
:date: 09/01/2026

*/

/***** Imports ******/

import type IDevice from "../types/device"

/***** Consts ******/

const BASE_API_URL = "http://127.0.0.1:8000/api/"

export const POSTCommands = {
    ADD: "ADD",
    DELETE: "DELETE"
} as const

const POST_ENDPOINTS: Record<POSTCommands, string> = {
    ADD: "add_device",
    DELETE: "delete_device"
}

export const GETCommands = {
    DEVICES: "DEVICES",
    STATUS: "STATUS"
}

const GET_ENDPOINTS: Record<GETCommands, string> = {
    DEVICES: "devices",
    STATUS: "status"
}

/***** Types ******/

type ApiResponse = {
    message: string
    status: number
}

export type POSTCommands = typeof POSTCommands[keyof typeof POSTCommands]
export type GETCommands = typeof GETCommands[keyof typeof GETCommands]

/***** Functions ******/

export async function sendGETCommand(command: GETCommands): Promise<ApiResponse> {
    const endpoint = GET_ENDPOINTS[command];

    const res = await fetch(`${BASE_API_URL}${endpoint}`);

    if(!res.ok){
        throw new Error(`/api/status: ${res.status}`)
    }

    return res.json() as Promise<ApiResponse>
}

export async function sendPOSTCommand(device: IDevice, action: POSTCommands): Promise<ApiResponse> {

    const endpoint = POST_ENDPOINTS[action];
    const res = await fetch(`${BASE_API_URL}${endpoint}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(device)
    })

    if(!res.ok) throw new Error(await res.text())
    
    return res.json()
}