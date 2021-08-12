import paramiko


class Client(object):
    def __init__(self, ip, port, user, password):
        self._client = paramiko.SSHClient()
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._client.connect(ip, port, user, password)

    def close(self):
        self._client.close()

    def send_command(self, command):
        # todo add expection handling!
        stdin, stdout, stderr = self._client.exec_command(command)
        return stdout.readlines()


class SSHBotnet(object):

    def __init__(self):
        self._clients = dict()

    def add_client(self, ip, user, password, port=22):
        if ip in self._clients:
            print(f'Client {user} with IP {ip} already added!')
        else:
            self._clients[ip] = Client(ip, port, user, password)

    def remove_client(self, client):
        if client._ip in self._clients:
            self._clients[client._ip].close()
            del(self._clients[client._ip])
        else:
            print(f"Client {client._user} with IP {client._ip} is not part of the botnet!")

    def send_command(self, command):
        # todo add expection handling!
        responses = []
        for ip in self._clients:
            resp = self._clients[ip].send_command(command)
            responses.append((ip, resp))
        return responses

if __name__ == "__main__":

    botnet = SSHBotnet()
    botnet.add_client('192.168.1.1', 'demouser', 'demopass')

    responses = botnet.send_command("ls -al")

    for ip, resp in responses:
        print(f"Output for IP {ip}")
        for line in resp:
            print(line)