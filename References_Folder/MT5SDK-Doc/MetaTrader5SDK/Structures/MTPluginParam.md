[🏠 Document Start](../README.md) / [Structures](README.md) / MTPluginParam

[Previous](MTPluginInfo.md) | [Next](MTServerInfo.md)

# MTPluginParam

This structure is used for describing default parameters of a plugin. Default parameters are passed through the default parameter of the [MTPluginInfo](MTPluginInfo.md) structure. The MTPluginParam structure is defined with the one-byte alignment.
    
    
    #pragma pack(push,1)
    struct MTPluginParam
      {
       //--- parameter types
       enum EnParamType
         {
          TYPE_STRING    =0,                                     // String
          TYPE_INT       =1,                                     // Integer
          TYPE_FLOAT     =2,                                     // Floating-point number
          TYPE_TIME      =3,                                     // Time
          TYPE_DATE      =4,                                     // Date
          TYPE_DATETIME  =5,                                     // Date and time
          TYPE_GROUPS    =6,                                     // List of groups
          TYPE_SYMBOLS   =7,                                     // List of symbols
          TYPE_BOOL      =8,                                     // Boolean
          //---
          TYPE_FIRST     =TYPE_STRING,
          TYPE_LAST      =TYPE_BOOL
         };
       //---
       UINT              type;                                   // Parameter type (EnParamType)
       wchar_t           name[64];                               // Parameter name
       wchar_t           value[256];                             // Parameter value
       UINT              reserved[16];                           // Reserved field
      };
    #pragma pack(pop)

The MTPluginParam structure contains the EnParamType enumeration that contains description of possible types of parameters:

ID | Value | Description  
TYPE_STRING | 0 | A string parameter.  
TYPE_INT | 1 | An integer parameter.  
TYPE_FLOAT | 2 | A floating-point number.  
TYPE_TIME | 3 | A parameter, in which time is specified (HH:MM:SS).  
TYPE_DATE | 4  | A parameter, in which date is specified (YYYY.MM.DD).  
TYPE_DATETIME | 5 | A parameter, in which date and time are specified (YYYY.MM.DD HH:MM:SS).  
TYPE_GROUPS | 6 | List of groups.  
TYPE_SYMBOLS | 7 | List of symbols.  
TYPE_BOOL | 8 | A boolean parameter.  
TYPE_FIRST |  | Beginning of enumeration. It corresponds to TYPE_STRING.  
TYPE_LAST |  | End of enumeration. It corresponds to TYPE_BOOL.  
  
The structure contains the following parameters:

Field | Type | Description  
type | UINT | Parameter type. To pass the type, the EnParamType enumeration is used.  
name | wchar_t | The name of the parameter.  
value | wchar_t | The value of the parameter.  
reserved | UINT | A reserved field for future use.
