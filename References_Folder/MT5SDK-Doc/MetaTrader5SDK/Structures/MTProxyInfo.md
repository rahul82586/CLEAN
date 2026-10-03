[🏠 Document Start](../README.md) / [Structures](README.md) / MTProxyInfo

[Previous](README.md) | [Next](MTLicenseCheck.md)

# MTProxyInfo

The MTProxyInfo structure is used for passing parameters of a proxy server. The structure is defined with the one-byte alignment.
    
    
    #pragma pack(push,1)
    struct MTProxyInfo
      {
       //--- Types of proxy servers
       enum
         {
          PROXY_SOCKS4   =0,                                     // SOCKS4
          PROXY_SOCKS5   =1,                                     // SOCKS5
          PROXY_HTTP     =2,                                     // HTTP (including NTLM)
          PROXY_FIRST    =PROXY_SOCKS4,                          // First type
          PROXY_LAST     =PROXY_HTTP                             // Last type
         };
       //--- Description of a proxy server
       int               enable;                                 // Flag of proxy server using
       int               type;                                   // Type of a proxy server
       wchar_t           address[64];                            // IP-address:Port of a proxy server
       wchar_t           auth[64];                               // Login:Password
      };
    #pragma pack(pop)

This structure is used in the following methods:

  * [IMTAdminAPI::ProxySet](../Manager-API/Administrator-Interface/Connection-to-the-Server/ProxySet.md)
  * [IMTManagerAPI:ProxySet](../Manager-API/Manager-Interface/Connection-to-the-Server/ProxySet.md)



This structure contains an enumeration, in which types of proxy servers passed in the type parameter are described:

ID | Value | Description  
PROXY_SOCKS4 | 0 | Type SOCKS4.  
PROXY_SOCKS5 | 1 | Type SOCKS5.  
PROXY_HTTP | 2 | Type HTTP, including NTLM authentication.  
PROXY_FIRST |  | Beginning of enumeration. Corresponds to PROXY_SOCKS4.  
PROXY_LAST |  | End of enumeration. Corresponds to PROXY_HTTP.  
  
The structure contains the following parameters:

Field | Type | Description  
enable | int | A flag of connection through a proxy server. 0 — proxy server is not used, 1 — connection through a proxy server.  
type | int | Proxy server type passed using the enumeration described above.  
address | wchart_t | The IP address of the proxy server and the port number separated by a colon. For example, 192.168.0.1:3180.  
auth | wchart_t | The login and password for connecting to the proxy server, separated by a colon.
