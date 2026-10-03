[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Connection to the Server](../Connection-to-the-Server.md) / Connect

[Previous](Pumping-Modes.md) | [Next](Disconnect.md)

# IMTAdminAPI::Connect

Connect to the trading platform.

C++
    
    
    virtual MTAPIRES  IMTAdminAPI::Connect(
       LPCWSTR  server,               // Server address
       UINT64   login,                // Login
       LPCWSTR  password,             // Password
       LPCWSTR  password_cert,        // Certificate password
       UINT64   pump_mode,            // Pumping mode
       UINT     timeout=INFINITE      // Timeout
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.Connect(
       sring                     server,         // Server address
       ulong                     login,          // Login
       string                    password,       // Password
       string                    password_cert,  // Certificate password
       CIMTAdminAPI.EnPumpModes  pump_mode,      // Pumping mode
       uint                      timeout         // Timeout
       )

Python
    
    
    AdminAPI.Connect(
       str                       server,         # Server address
       int                       login,          # Login
       str                       password,       # Password
       AdminAPI.EnPumpModes      pump_mode,      # Pumping mode
       int                       timeout         # Timeout
       )

### Parameters

**server**  
[in] Address and port of the Access server of the platform to which you are connecting. The values should be separated by a colon, for example: 192.168.0.1:443.

**login**  
[in] The login of the manager for connection.

**password**  
[in] The password of the manager for connection.

**password_cert**  
[in] Certificate password. It is only used in the advanced server authentication mode. In this case, the certificate for the administrator account should be copied to [Manager API data directory]\bases\\[server name]\certificates\\.

**pump_mode**  
[in] The pumping mode, in which connection will be established. To pass the pumping mode, theIMTAdminAPI::EnPumpModesenumeration is used.

**timeout=INFINITE**  
[in] Server connection timeout in milliseconds. If the application fails to connect to a server within this time, attempts will be terminated. By default there is no time limit.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code will be returned.

### Note

After establishing a connection to the server, Manager API will automatically keep it up. No additional actions are required to keep the connection up.
