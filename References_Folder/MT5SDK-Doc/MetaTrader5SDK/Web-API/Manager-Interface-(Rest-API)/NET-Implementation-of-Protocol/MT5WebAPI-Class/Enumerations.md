[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../MT5WebAPI-Class.md) / Enumerations

[Previous](Constructor.md) | [Next](ConnectDisconnect.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The MT5WebAPI class contains the following enumerations:

  * [EnCryptModes (#encryptmodes)](Enumerations.md#encryptmodes)
  * [EnPumpModes (#enpumpmodes)](Enumerations.md#enpumpmodes)



<a id="encryptmodes"></a>
## MT5WebAPI.EnCryptModes (#encryptmodes)

Possible modes of [encryption](../../Text-Protocol-(Raw-API)/Encryption.md) of the data stream exchanged between the Web client and the trade server are enumerate in MT5WebAPI::EnCryptModes.

ID | Value | Description  
CRYPT_MODE_NONE | 0 | Encryption is disabled.  
CRYPT_MODE_AES | 1 | AES encryption using the 256-bit key in the OFB (Output Feedback) mode. For more information, see ["Encryption"](../../Text-Protocol-(Raw-API)/Encryption.md).  
  
This enumeration is used in the [MT5WebAPI.Connect](Connect-Disconnect/Connect.md) method.

<a id="enpumpmodes"></a>
## MT5WebAPI.EnPumpModes (#enpumpmodes)

Enabling a pumping mode means that the Web client will synchronize the appropriate database of the server with a locally created database. Thus, to obtain information the application can access the local database.

> Currently pumping is not available. This feature will be implemented later.

Possible pumping modes are enumerate in MT5WebAPI::EnPumpModes.

ID | Value | Description  
PUMP_MODE_NONE | 0x00000000 | No data pumping.  
  
The pumping mode, in which you want to connect, is passed in the parameter of the pumpModes method [MT5WebAPI.Connect](Connect-Disconnect/Connect.md).
