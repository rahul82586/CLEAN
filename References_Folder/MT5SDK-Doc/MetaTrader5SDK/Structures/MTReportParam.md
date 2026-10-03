[🏠 Document Start](../README.md) / [Structures](README.md) / MTReportParam

[Previous](MTReportInfo.md) | [Next](MTReportServerInfo.md)

<a id="mtreportparam"></a>
# MTReportParam (#mtreportparam)

This structure is used for describing a reports module parameters. It describes both reports request parameters from a manager terminal and module parameters that are set during the configuration in MetaTrader 5 Administrator. Requests parameters are passed through the params field and external parameters are passed through the config field of the [MTReportInfo](MTReportInfo.md) structure. The MTReportParam structure is defined with the one-byte alignment.
    
    
    #pragma pack(push,1)
    struct MTReportParam
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

<a id="enparamtype"></a>
## Enumerations (#enparamtype)

The MTReportParam structure contains the EnParamType enumeration that contains description of possible types of parameters:

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
  
<a id="parameters"></a>
## Parameters (#parameters)

The structure contains the following parameters:

Field | Type | Description  
type | UINT | Parameter type. To pass the type, the EnParamType enumeration is used.  
name | wchar_t | The name of the parameter. The following macroses are used to pass the reports request parameters name from the MetaTrader 5 Manager terminal:

  * MTAPI_PARAM_GROUPS — "Groups" field;
  * MTAPI_PARAM_SYMBOLS — "Symbols" field;
  * MTAPI_PARAM_FROM — "From" parameter in the "Period" field;
  * MTAPI_PARAM_TO — "To" parameter in the "Period" field.

In case another name is specified for a parameter, it will be displayed in the additional parameters block of a manager terminal.  
value | wchar_t | The value of the parameter.  
reserved | UINT | A reserved field for future use.
