import asyncio

class ServerError(Exception):
    pass

class Storage:

    def __init__(self):
        self.storage = {}

    def put(self, metric_name, timestamp, metric_value):
        if metric_name not in self.storage:
            self.storage[metric_name] = {}
            self.storage[metric_name][timestamp] =  metric_value
        else:
            self.storage[metric_name][timestamp] = metric_value

    def get(self, metric_name):
        if metric_name == "*":
            if not self.storage:
                result = []
            result = [(name, self.storage[name][timestamp], timestamp) for name in self.storage for timestamp in self.storage[name]]
        else:
            try:
                result_dict = self.storage[metric_name]
                result = [(metric_name, result_dict[timestamp], timestamp) for timestamp in result_dict]
            except KeyError:
                result = []
        return result


class ClientServerProtocol(asyncio.Protocol):
    storage = Storage()

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def _put(self, put_data):
        if len(put_data) > 3:
            raise ServerError("wrong command")
        try:
            metric_name = put_data[0]
            metric_value = float(put_data[1])
            timestamp = int(put_data[2])
        except ValueError:
            raise ServerError("wrong command")
        except IndexError:
            raise ServerError("wrong command")
        except TypeError:
            raise ServerError("wrong command")
        self.storage.put(metric_name, timestamp, metric_value)

    def _get(self, get_data):
        if len(get_data) > 1:
            raise ServerError("wrong command")
        try:
            metric_name = get_data[0]
        except IndexError:
            raise ServerError("wrong command")
        return self.storage.get(metric_name)

    def process_data(self, data):
        data_split = data.strip().split(" ")
        if data_split[0] == "put":
            try:
                self._put(data_split[1:])
                return "ok\n\n"
            except ServerError:
                return "error\nwrong command\n\n"
        elif data_split[0] == "get":
            result_list = []
            result_list.append("ok")
            try:
                res = self._get(data_split[1:])
            except ServerError:
                return "error\nwrong command\n\n"
            for name, value, timestamp in res:
                result_list.append(f"\n{name} {value} {timestamp}")
            result_list.append("\n\n")
            result = "".join(result_list)
            return result
        else:
            return "error\nwrong command\n\n"


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

if __name__ == "__main__":
    run_server("127.0.0.1", 8888)