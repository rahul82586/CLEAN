[🏠 Document Start](../../README.md) / [Web API](../README.md) / [Manager Interface (Rest API)](../Manager-Interface-(Rest-API).md) / Text Protocol (Raw API)

[Previous](Common-Requests/Get-Journal.md) | [Next](Text-Protocol-(Raw-API)/Format-of-Packages.md)

# Text Protocol (Raw API)

The main method of working with the trading platform via Web API is sending commands via GET and POST requests (Rest API). However, Web API also supports the purely text-based protocol (Raw API). In fact, it is a set of commands of a certain format that can be sent as text messages over TCP connection. A sending method remains at the discretion of a programmer.

This section contains the protocol description:

  * [Format of Packets](Text-Protocol-(Raw-API)/Format-of-Packages.md)
  * [Format of Commands](Text-Protocol-(Raw-API)/Format-of-Commands.md)
  * [Authentication](Text-Protocol-(Raw-API)/Authentication.md)
  * [Encryption](Text-Protocol-(Raw-API)/Encryption.md)



The text API supports the same commands as Rest API. The command descriptions are provided in the [Main Interface (Rest API)](../Manager-Interface-(Rest-API).md) section.
