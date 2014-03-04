import argparse
import bitcoinaddress as ba
import zmq


def main(args):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    data = ba.parse_address(args.address)
    socket.connect('tcp://%s:%s' % (ba.get_host_ip(data.get('domain')),
                                    args.port))
    socket.send(ba.dumps(data))
    response = socket.recv()
    print response


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Bitcoin Address Client')
    parser.add_argument('address',
                        help="Bitcoin address ala email: john@smith.com")
    parser.add_argument('--port', dest='port', default='4179',
                        help="Port the server runs.")
    args = parser.parse_args()
    main(args)
