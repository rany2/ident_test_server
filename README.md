# ident_test_server

Basic server to test if IDENT is functioning properly.

# Example usage

## Server side

```
python3 ident_test_server.py :: 6000
```

## Client side

```
$ telnet 2001:666::1 6000
Trying 2001:666::1...
Connected to 2001:666::1.
Escape character is '^]'.
40332,6000:USERID:UNIX:ranyz
Connection closed by foreign host.
```

So we can see that the user that initiated the connection is `ranyz` and that the IDENT server is configured properly.
