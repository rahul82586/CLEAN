[🏠 Document Start](../README.md) / [Structures](README.md) / MTServerInfo

[Previous](MTPluginParam.md) | [Next](../Configuration-Interfaces/README.md)

# MTServerInfo

Using the MTServerInfo structure, the server provides the plugin with the information about the trading platform and the server on which it is running. The structure is defined with the one-byte alignment.
    
    
    #pragma pack(push,1)
    struct MTServerInfo
      {
       wchar_t           platform_name[64];                     // Name of the platform
       wchar_t           platform_owner[128];                   // Owner of th eplatform
       UINT              server_version;                        // Server version
       UINT              server_build;                          // Server build
       UINT              server_type;                           // Server type
       UINT64            server_id;                             // Server ID
       UINT              reserverd[32];                         // A reserved field
      };
    #pragma pack(pop)

This structure is used in the [IMTServerAPI::About](../Server-API/Main-API-Interface/Common-Functions/About.md) method.

The structure contains the following parameters:

Field | Type | Description  
platform_name | wchar_t | Name of the platform.  
platform_owner | wchar_t | The name of the platform owner.  
server_version | UINT | Version of the server on which the plugin is running.  
server_build | UINT | Build of the server on which the plugin is running.  
server_type | UINT | Type of the server on which the plugin is running. To pass the server type, the [IMTConServer::EnServerTypes (#enservertypes)](../Configuration-Interfaces/Network/IMTConServer/Enumerations.md#enservertypes) enumeration is used.  
server_id | UINT64 | The ID of the server on which the plugin is running.  
reserved | UINT | A reserved field for future use.
