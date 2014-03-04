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
