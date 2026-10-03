[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Operations with Connection](../Operations-with-Connection.md) / NetworkRescan

[Previous](../Operations-with-Connection.md) | [Next](NetworkBytesSent.md)

# IMTManagerAPI::NetworkRescan

Forced launch of scanning for access points and receiving the scanning results. Scanning includes obtaining a complete map of the network with the data on the access servers' workload, as well as measuring ping to each access point. After obtaining the data, decision is made on whether the access point better than the current one is found.

C++
    
    
    MTAPIRES  IMTManagerAPI::NetworkRescan(
       const UINT     flags       // Flags (for future use)
       const UINT     timeout     // Timeout of waiting for scanning
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.NetworkRescan(
       uint           flags       // Flags (for future use)
       uint           timeout     // Timeout of waiting for scanning
       )

Python
    
    
    ManagerAPI.NetworkRescan(
       int            flags       # Flags (for future use)
       int            timeout     # Timeout of waiting for scanning
       )

### Parameters

**flags**  
[in] Flags. This parameter is not used at the moment.

**timeout**  
[in] Time to wait for the completion of scanning in milliseconds. If scanning is not finished within the specified time, the check for the best access point is performed nonetheless. If it is present, the method returns MT_RET_OK value. In order to check the availability of the best access point without waiting, this method can be called with timeout parameter equal to 0.

### Return Value

The method reports on scanning results using the following response codes:

  * [MT_RET_OK](../../../Return-Codes/Successful-completion.md) \- the best access point found. To connect to it, [IMTManagerAPI::Disconnect](../Connection-to-the-Server/Disconnect.md) method can be called. It is followed by [IMTManagerAPI::Connect](../Connection-to-the-Server/Connect.md) passing the name of the server, connection to which is to be performed. The server name can be received using [IMTManagerAPI::NetworkServer](NetworkServer.md) method.
  * [MT_RET_NOTFOUND](../../../Return-Codes/Common-errors.md) \- the best access point not found.
  * [MT_RET_FREQUENT](../../../Return-Codes/Common-errors.md) \- too frequent requests. Requests can be made no more frequently than once per half an hour.



### Note

In order to arrange selection of the best access point for connecting Manager API, the name of the server for connection instead of an IP address should be specified in [IMTManagerAPI::Connect](../Connection-to-the-Server/Connect.md) method. The server name can be received using [IMTManagerAPI::NetworkServer](NetworkServer.md) method.
