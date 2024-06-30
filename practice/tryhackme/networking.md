# Networking

### Introductory Networking

_Summary: intro to OSI and TCP/IP model_&#x20;

Room: [https://tryhackme.com/r/room/introtonetworking](https://tryhackme.com/r/room/introtonetworking)

* OSI is a good start, but real world implementation is based on TCP/IP model
* OSI layers:
  * \[7] application -> end-user (HTTP, FTP, SMTP)
  * \[6] presentation -> encryption, compression
  * \[7] session -> establish session, allows opening 2 tabs in a browser
  * \[6] transport -> port, TCP/UDP
  * \[7] network -> ip address, routing
  * \[6] data link -> mac address, transmission preparation
  * \[7] physical -> bits to signal
* encapsulation -> adds trailer at the end of layer 2 for integrity
* TCP/IP layers: 5,6,7 is merged
