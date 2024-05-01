from fastapi import FastAPI, WebSocket
import asyncio
import paramiko
from repository import SSHMicroServiceRepository

app = FastAPI()
connections = {}


async def establish_ssh_connection(host, port, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(host, port=port, username=username, password=password)

    channel = ssh_client.get_transport().open_session()
    channel.get_pty()
    channel.invoke_shell()

    return channel


async def run_ssh_command(channel, command):
    channel.send(command + '\n')

    result = b''

    while not channel.recv_ready():
        await asyncio.sleep(0.1)
    while channel.recv_ready():
        ch_recv = channel.recv(1024)

        result += ch_recv
        await asyncio.sleep(0.1)

    decoded_string = result.decode("utf-8")
    return decoded_string


async def get_or_establish_ssh_connection(websocket, host, port, username, password):
    if websocket not in connections:
        channel = await establish_ssh_connection(host, port, username, password)
        connections[websocket] = channel
    return connections[websocket]


@app.websocket("/ssh")
async def websocket_handler(websocket: WebSocket, host: str, port: int, username: str, password: str):
    await websocket.accept()

    conn = await get_or_establish_ssh_connection(websocket, host, port, username, password)

    while True:
        data = await websocket.receive_json()

        if not data:
            break

        ssh_results = await run_ssh_command(conn, data['command'])

        await websocket.send_text(ssh_results)