[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Text Protocol (Raw API)](../Text-Protocol-(Raw-API).md) / Format of Packages

[Previous](../Text-Protocol-(Raw-API).md) | [Next](Format-of-Commands.md)

<a id="format-of-packets"></a>
# Format of Packets (#format-of-packets)

The MetaTrader 5 Web API is a packaged protocol. Data is transmitted in the form of packets having a header and a body.

<a id="header"></a>
## Title (#header)

In the beginning of the packet, a 9-byte header of the following format is passed:
    
    
    LLLLKKKKF

where:

Part of the command | Description | Range  
LLLL | A text ASCII number in the hex format, in which the length of the message body is passed. | The size can be specified as a number in the range 0000-FFFF. It defines the maximum packet size — 65 KB.  
KKKK | A text ASCII number in the hex format, in which the length of the serial number of the message is passed. Serial numbers are required for combining several packets into one. | The serial number must be within the range 0000-FFFF:

  * 0-3FFF (0-16383) — client commands.
  * 4000-7FFF (16384-32767) — messages from an access server.
  * 8000-FFFF (32768-65535) — messages from a trade server.

  
F | A text ASCII number in the hex format, in which flags are passed. | Flags can be specified as a number in the range 0-F.  
  
<a id="flags"></a>
### Flags (#flags)

To pass additional information about a packet, flags in the range 0 to F are used, which are transmitted in the last byte of the packet header. Currently the following flags are available:

  * 1 — the flag indicates that the command has an extension. If a command does not fit into one packet, it is split into several packets, in each of which except for the last one this flag is transmitted.



<a id="body"></a>
## Body (#body)

The header is followed by the packet body with the size LLLL specified in the header. The maximum size of body is 65 KB. If a command does not fit into one packet, it should be is split into several packets. Packets are combined based on the KKKK identifiers (serial number), which are specified in the header of each packet.

Splitting of data into packets should be taken into account when sending messages and when receiving them from the server. A received command should not be processed until the last packet with the same identifier and without flag 1 is received.

All the text commands of the Web API and their parameters are passed in the Unicode format (UTF-16, little endian).  
---  
  
Packet Example
    
    
    000800010TEST

where:

  * 0008 — body size. The TEST string in the Unicode format (4 characters = 8 byte);
  * 0001 — number of the message;
  * 0 — flags. In this case there are no flags.
  * TEST — body.


