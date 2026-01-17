/*
This interface represents a device.

Author: guylev38
Date: 24/10/2025
*/

export default interface IDevice{
    ip: string,
    status?: boolean,
    last_checked?: string,
    response_time?: string,
    _id?: string
}