import bitcoinaddress as ba
import json
import zmq
import argparse


def load_addresses(f):
    """
    Reads from the addresses table/database/json file.
    """
    return json.loads(open(f, 'r').read())


def start_server(host, port, addresses):
    """
    Starts the bitcoinaddress server.
    """
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    address = 'tcp://%s:%s' % (host, port)
    socket.bind(address)
    print 'runs on %s' % address

    while True:
        data = socket.recv()
        data = json.loads(data)
        socket.send(ba.dumps({
            'address': addresses.get(data.get('name'), None)
        }))


def main(args):
    addresses = load_addresses('addresses.json')
    start_server(args.host, args.port, addresses)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Bitcoin Address Server')
    parser.add_argument('--host', dest='host', default='127.0.0.1',
                        help="Host the server binds to.")
    parser.add_argument('--port', dest='port', default='4179',
                        help="Port the server binds to.")
    args = parser.parse_args()
    main(args)
