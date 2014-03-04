Bitcoin Address
===============

A simple protocol that allows you to mask your bitcoin
address like an email (something like john@smith.com).

Insipiration
------------

Copy and pasting long bitcoin addresses is haaaaard.

Protocol
--------

Just like how email works, the client parses the addresses
separating the name and the domain.

```
john | @ | smith.com
name | x | domain
```

Now, the client sends a request (similar to how http works)
to the domain sending the name as the body. Right now, it's
in json.

```
{
  "name": "john",
  "address": "smith.com"
}
```

Once the request is acknowledged, the server responds with
the bitcoin hash the domain maps to. Again, it's in json.

```
{
  "address": "mybitcoinhashthatshardtoremember"
}
```

Should a name not map to something, the address value will
hold the value `null`.

Examples
--------

Wrote a server and a client under the directory `examples`.

###Server

The server does the conversion of addresses into hashes.

```
$ python server.py -h
usage: server.py [-h] [--host HOST] [--port PORT]

Bitcoin Address Server

optional arguments:
  -h, --help   show this help message and exit
  --host HOST  Host the server binds to.
  --port PORT  Port the server binds to.
```

Running it...

```
$ python server.py --host 0.0.0.0 --port 41791
```

###Client

The client is a simple python binary that works like
`$ whois`.

```
$ python client.py -h
usage: client.py [-h] [--port PORT] address

Bitcoin Address Client

positional arguments:
  address      Bitcoin address ala email: john@smith.com

optional arguments:
  -h, --help   show this help message and exit
  --port PORT  Port the server runs.
```

An example usage:

```
$ python client.py jesse@bit.jpanganiban.com
{"address": "mybitcoinhash"}
```
