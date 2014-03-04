import json
import socket


def get_host_ip(domain):
    """
    Gets the equivalent ip of a domain.
    """
    return socket.gethostbyname(domain)


def parse_address(raw_address):
    """
    Parses a raw address into a dictionary.

    eg.

    john@smith.com
    -> {'name': 'john', 'domain': 'smith.com'}
    """
    name, domain = raw_address.split('@')
    return {
        'name': name,
        'domain': domain,
    }


def loads(data):
    """
    Reads raw data and converts it into a python
    dictionary.
    """
    return json.loads(data)


def dumps(data):
    """
    Converts a dictionary into raw data to be sent to the
    server.
    """
    return json.dumps(data)


__all__ = ('loads', 'dumps', 'parse_address', 'get_host_ip', )
