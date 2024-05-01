import asyncpg

from os import environ


class SSHMicroServiceRepository:
    @staticmethod
    async def get_connections():
        pg_conn = await asyncpg.connect(
            user=environ['POSTGRES_USER'],
            password=environ['POSTGRES_PASSWORD'],
            database=environ['POSTGRES_DB'],
            host=environ['POSTGRES_HOST'],
        )

        query = 'SELECT host, port, username, password FROM ssh_connections_app_sshconnection'
        result = await pg_conn.fetch(query)

        return result