[🏠 Document Start](../README.md) / [Structures](README.md) / MTPluginInfo

[Previous](MTReportServerInfo.md) | [Next](MTPluginParam.md)

# MTPluginInfo

The MTPluginInfo structure is used for transmitting the primary data of a plugin to a server. The structure is defined with the one-byte alignment.
    
    
    #pragma pack(push,1)
    struct MTPluginInfo
      {
       UINT              version;                               // Plugin Version
       UINT              version_api;                           // Server API version
       wchar_t           name[64];                              // Name of the plugin
       wchar_t           copyright[128];                        // Copyright
       wchar_t           description[256];                      // Description
       MTPluginParam     defaults[128];                         // Default parameters
       UINT              defaults_total;                        // Number of default parameters
       UINT              reserved[128];                         // A reserved field
      };
    #pragma pack(pop)

The structure is passed to the server via the entry point [MTServerAbout](../Server-API/Entry-Points/MTServerAbout.md). It contains the following parameters:

Field | Type | Description  
version | UINT | In this parameter, information about the plugin version is passed to the server.  
version_API | UINT | This field is used to pass the version of the Server API, in which the plugin has been compiled.  
name | wchar_t | This parameter is used to pass the name of the plugin.  
copyright | wchar_t | This parameter is used to pass the copyright.  
description | wchar_t | This parameter is used to pass the plugin description.  
defaults | MTPluginParam | An array of default parameters described by the [MTPluginParam](MTPluginParam.md) structure.  
defaults_total | UINT | The total number of passed default parameters.  
reserved | UINT | A reserved field for future use.
