[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Connect/Disconnect](../ConnectDisconnect.md) / Connect

[Previous](../ConnectDisconnect.md) | [Next](Disconnect.md)

# MT5WebAPI.Connect

Connect a Web client to a trade server.
    
    
    MTRetCode  MT5WebAPI.Connect(
       string        server,       // IP address
       int           port,         // Port
       ulong         login,        // Login
       string        password,     // Password
       EnPumpModes   pumpModes,    // Pumping mode
       EnCryptModes  crypt,        // Encryption mode
       int           timeout       // Timeout
       )

### Parameters

**server**  
[in] The IP address of the server to connect to.

**port**  
[in] The port of the server to connect to.

**login**  
[in] The login of the manager account, using which you want to connect.

**password**  
[in] The password of the manager account, using which you want to connect.

**pumpModes**  
[in] The pumping mode, in which connection will be established. To pass the pumping mode, theMT5WebAPI::EnPumpModesenumeration is used.

**crypt**  
[in] Mode of encryption of data transmitted between the Web client and the trade server. To pass the encryption mode, theMT5WebAPI::EnCryptModesenumeration is used.

**timeout**  
[in] The period of waiting for server response in milliseconds.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

# MT5WebAPI.Connect

Connect a Web client to a trade server.
    
    
    MTRetCode  MT5WebAPI.Connect(
       string        server,       // IP address
       int           port,         // Port
       ulong         login,        // Login
       string        password,     // Password
       EnPumpModes   pumpModes     // Pumping mode
       )

### Parameters

**server**  
[in] The IP address of the server to connect to.

**port**  
[in] The port of the server to connect to.

**login**  
[in] The login of the manager account, using which you want to connect.

**password**  
[in] The password of the manager account, using which you want to connect.

**pumpModes**  
[in] The pumping mode, in which connection will be established. To pass the pumping mode, theMT5WebAPI::EnPumpModesenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

During connection, [AES encryption](../../../Text-Protocol-(Raw-API)/Encryption.md) of transmitted data and server response timeout of 5 seconds are used by default.
