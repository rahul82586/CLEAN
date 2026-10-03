[🏠 Document Start](../README.md) / [Structures](README.md) / MTGatewayInfo

[Previous](MTBookMTBookDiff.md) | [Next](MTNews.md)

<a id="mtgatewayinfo"></a>
# MTGatewayInfo (#mtgatewayinfo)

MTGatewayInfo structure is used for setting a gateway/data feed module parameters. The structure is defined with the one-byte alignment.
    
    
    #pragma pack(push,1)
    struct MTGatewayInfo
      {
       //--- Gateway/data feed module operation modes
       enum EnModes
         {
          GATEWAY_MODE_QUOTES     =1,                            // Receiving quotes
          GATEWAY_MODE_NEWS       =2,                            // Receiving news
          GATEWAY_MODE_POSITIONS  =4,                            // Ability to get the state of positions
          GATEWAY_MODE_NONE       =0,
          GATEWAY_MODE_ALL        =GATEWAY_MODE_QUOTES|GATEWAY_MODE_NEWS|GATEWAY_MODE_POSITIONS
         };
       //--- Flags of the fields available for setting
       enum EnFields
         {
          GATEWAY_FIELD_SERVER    =1,                            // The Server field
          GATEWAY_FIELD_LOGIN     =2,                            // The Login field
          GATEWAY_FIELD_PASSWORD  =4,                            // The Password field
          GATEWAY_FIELD_PARAMS    =8,                            // The Parameters field
          GATEWAY_FIELD_NONE      =0,
          GATEWAY_FIELD_ALL       =GATEWAY_FIELD_SERVER|GATEWAY_FIELD_LOGIN|GATEWAY_FIELD_PASSWORD|GATEWAY_FIELD_PARAMS
         };
       //--- Gateway/data feed module description
       UINT              version;                                // Gateway/data feed version
       UINT              version_api;                            // Gateway API version
       wchar_t           name_default[128];                      // Default name
       wchar_t           copyright[128];                         // Copyright
       wchar_t           server_default[128];                    // Default server address
       wchar_t           login_default[64];                      // Default login
       wchar_t           password_default[64];                   // Default password
       wchar_t           parameters_default[512];                // Default additional parameters
       UINT              mode;                                   // Operation mode
       UINT              fields;                                 // Mandatory fields
       wchar_t           description[512];                       // Description
       wchar_t           module_id[16];                          // Gateway module identifier
       wchar_t           build_date[16];                         // Build date of the gateway/data feed
       wchar_t           build_api_date[16];                     // Build date of Gateway API
       UINT              reserved[32];                           // Reserved field
      };
    #pragma pack(pop)

<a id="enumerations"></a>
## Enumerations (#enumerations)

This structure contains the following enumerations:

  * EnModes
  * EnFields



<a id="enmodes"></a>
### EnModes (#enmodes)

Gateway operation modes are described in EnModes:

ID | Value | Description  
GATEWAY_MODE_QUOTES | 1 | Gateway/data feed can transmit the quotes.  
GATEWAY_MODE_NEWS | 2 | Gateway/data feed can transmit the news.  
GATEWAY_MODE_POSITIONS | 4  | The gateway supports [requesting the state of external trading system positions](../Gateway-API/Main-Interface/Controlling-Positions-in-External-System.md). The request can be made from "Positions" tab of the gateway in MetaTrader 5 Administrator.  
GATEWAY_MODE_NONE | 0 | Beginning of enumeration. It corresponds to the absence of any operation modes.  
GATEWAY_MODE_ALL |  | End of enumeration. It corresponds to the support of all operation modes.  
  
<a id="enfields"></a>
### EnFields (#enfields)

EnFields contains descriptions of the flags of the fields that will be available for a gateway/data feed setting through MetaTrader 5 Administrator:

ID | Value | Description  
GATEWAY_FIELD_SERVER | 1 | The field of the address of an external server for connection.  
GATEWAY_FIELD_LOGIN | 2 | Login field.  
GATEWAY_FIELD_PASSWORD | 4  | Password field.  
GATEWAY_FIELD_PARAMS | 8 | Additional external parameters.  
GATEWAY_FIELD_NONE | 0 | Beginning of enumeration. It corresponds to the absence of required fields.  
GATEWAY_FIELD_ALL |  | End of enumeration. Corresponds to enabling of all fields.  
  
<a id="parameters"></a>
## Parameters (#parameters)

MTGatewayInfo structure contains the following parameters:

Field | Type | Description  
version | UINT | In this parameter information about the gateway/data feed module version is passed to the server. Information about the build number and date of the application and of the used Gateway API will be displayed on the Staus page of gateways and data feeds in MetaTrader 5 Administrator.  
version_API | UINT | This field is used to pass the version of Gateway API, in which the gateway/data feed has been compiled. Filled with a value of MTGatewayAPIVersion specified MT5APIGateway.h by default. Required parameter.  
name | wchar_t | This parameter serves for passing the name that is placed in the configuration by default during the selection of a gateway/data feed module in the "File" field of MetaTrader 5 Administrator.  
copyright | wchar_t | This parameter is used to pass the copyright. Copyright is shown on the ["Information"](../Gateway-API/Main-Interface/External-Connection-State.md) tab of the gateway/data feed in MetaTrader 5 Administrator.  
server_default | wchar_t | This parameter serves for passing the server address (in address:port format) that is placed in the configuration by default during the selection of a gateway/data feed module in the "File" field.  
login_default | wchar_t | This parameter serves for passing the login that is placed in the configuration by default during the selection of a gateway/data feed module in the "File" field.  
password_default | wchar_t | This parameter serves for passing the password that is placed in the configuration by default during the selection of a gateway/data feed module in the "File" field.  
parameters_default | wchar_t | This parameter serves for passing the parameters that are placed in the configuration by default during the selection of a gateway/data feed module in the "File" field. The parameters are passed in the following format: Parameter1=Value1\\\nParameter2=Value2\\\n...\\\nParametrN=ValueN\\\n. For example: | TradingCalendarHolidays=\\\nFIXTargetCompId=\\\nFIXSenderCompId=\\\nFIXSenderSubId=\\\nFIXDeliverToCompID=\\\nLimitOrdersCoverage=Gateway  
\\\nStopOrdersCoverage=N\\\nLimitOrdersCoverageTimeout=5\\\nWeekTimeBegin=17:00\\\nWeekTimeEnd=17:00\\\nMinQtySet=N\nFIXQuotesLogEnabled=N\\\n  
---  
  
mode | UINT | Gateway/data feed operation modes are passed in this field. To pass the options, the EnModes enumeration is used.  
fields | UINT | Flags of the fields available for a gateway/data feed setting in MetaTrader 5 Administrator are passed in this field. To pass the options, the EnFields enumeration is used.  
description | wchar_t | This parameter is used to pass the gateway/data feed module description. Description is shown on the ["Information"](../Gateway-API/Main-Interface/External-Connection-State.md) Description is shown on the.  
module_id | wchar_t | Identifier of the gateway module. It used to bind deals to a specific gateway ([IMTDeal::Gateway](../Database-Interfaces/Trade/Deals/IMTDeal/Gateway.md)). For example, if several instances (configurations) of the same gateway are created within the trading platform, deals processed by that gateway instances can be grouped by this identifier in reports. The field is required.  
build_date | wchar_t | The build date of the gateway/data feed.  
build_api_date | wchar_t | The build date of the Gateway API, that was used to create the current version of the gateway/data feed. Filled with a value of MTGatewayAPIDate specified MT5APIGateway.h by default.  
reserved | UINT | A reserved field for future use.
