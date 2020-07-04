import socket
import time

class ClientError(Exception):
    pass

class Client:
    def __init__(self, host, port, timeout = None):
        self.sock = socket.create_connection((host, port), timeout)
    def put(self, metric_name, metric_value, timestamp = None):
        timestamp = timestamp or int(time.time())
        put_request = "put {} {} {}\n".format(metric_name, metric_value, timestamp)
        self.sock.sendall(put_request.encode())
        data = b""
        while not data.endswith(b"\n\n"):
            data += self.sock.recv(1024)
        response = data.decode()
        split_response = response.split("\n")
        if split_response[0] == "error":
            raise ClientError(split_response[1])
    def get(self, metric_name):
        answer_dict = {}
        get_request = "get {}\n".format(metric_name)
        self.sock.sendall(get_request.encode())
        data = b""
        while not data.endswith(b"\n\n"):
            data += self.sock.recv(1024)
        response = data.decode()
        split_response = response.split("\n")
        if split_response[0] == "ok":
            for result in split_response[1:]:
                if not result:
                    break
                result_split = result.split(" ")
                if result_split[0] not in answer_dict:
                    answer_dict[result_split[0]] = []
                try:
                    answer_dict[result_split[0]].append((int(result_split[2]),float(result_split[1])))
                    answer_dict[result_split[0]].sort(key =lambda res: res[0])
                except ValueError as ve:
                    raise ClientError(ve)
                except TypeError as te:
                    raise ClientError(te)
                except IndexError as ie:
                    raise ClientError(ie)
        elif split_response[0] =="error":
            raise ClientError(split_response[1])
        else:
            raise ClientError("response error")
        return answer_dict



