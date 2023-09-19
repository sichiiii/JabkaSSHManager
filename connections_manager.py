import asyncio
import asyncssh


async def ssh_client(hostname, port, username, password):
    try:
        async with asyncssh.connect(
                host=hostname,
                port=port,
                username=username,
                password=password,
                known_hosts=None
        ) as ssh:
            while True:
                command = await asyncio.to_thread(input, f"{username}$ ")
                if command.lower() == "exit":
                    break

                _, stdout, _ = await ssh.open_session(command)
                result = await stdout.read()
                print(result)
    except Exception as e:
        print("Ошибка: ", str(e))


if __name__ == "__main__":
    hostname = input("Введите имя хоста: ")
    port = int(input("Введите порт (по умолчанию 22): ") or 22)
    username = input("Введите имя пользователя: " or "root")
    password = input("Введите пароль: ")

    asyncio.run(ssh_client(hostname, port, username, password))
