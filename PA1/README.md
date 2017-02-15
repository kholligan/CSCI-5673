# Distributed Systems Programming Assignment 1

## Build and run

This program runs on Python 2.7. Run your server on any machine using
`$python server_udp.py`
Find the ip address of the machine your server is running on by calling `ifconfig` or `curl ipinfo.io/ip` depending on whether you need your local or public IP address.
For home networks, you may have to enable port forwarding to route the packets to your server.
Replace the line
```python
server_address = ("ENTER IP ADDRESS HERE", 8000)
```
with the IP address you obtained then run the client program by using
`$python client_udp.py`