[🏠 Document Start](../README.md) / [Structures](README.md) / MTLogRecord

[Previous](MTMailRange.md) | [Next](MTChartBar.md)

# MTLogRecord

This structure describes the [Server log](../Manager-API/Administrator-Interface/Common-Functions.md) entry. The structure is defined with the one-byte alignment.
    
    
    #pragma pack(push,1)
    struct MTLogRecord
      {
       UINT              flags;                                  // Flags EnMTLogFlags
       UINT              code;                                   // Message types EnMTLogCode
       INT               type;                                   // Types of events EnMTLogType
       INT64             datetime;                               // Date and time in seconds
       wchar_t           source[64];                             // Source
       wchar_t           message[512];                           // Message text
       INT64             datetime_msc;                           // Date and time in milliseconds
       int               reserved[2];                            // A reserved field
      };
    #pragma pack(pop)

This structure is used in the following methods:

  * [IMTAdminAPI::LoggerServerRequest](../Manager-API/Administrator-Interface/Common-Functions/LoggerServerRequest.md)
  * [IMTManagerAPI::LoggerServerRequest](../Manager-API/Manager-Interface/Common-Functions/LoggerServerRequest.md)
  * [IMTReportAPI::LoggerRequest](../Report-API/Main-Interface-of-Reports/Common-Functions/LoggerRequest.md)
  * [IMTServerAPI::LoggerRequest](../Server-API/Main-API-Interface/Common-Functions/LoggerRequest.md)



The structure contains the following parameters:

Field | Type | Description  
flags | UINT | Log [entry flags (#enmtlogflags)](../Journal-Constants/README.md#enmtlogflags).  
code | UINT | Log [message type (#enmtlogcode)](../Journal-Constants/README.md#enmtlogcode).  
type | INT | [Event type (#enmtlogtype)](../Journal-Constants/README.md#enmtlogtype).  
datetime | INT64 | Date and time of a message in seconds that have elapsed since 01.01.1970.  
source | wchar_t | Source of the message.  
message | wchar_t | Message text.  
datetime_msc | INT64 | Date and time of a message in milliseconds that have elapsed since 01.01.1970.  
reserved | int | A reserved parameter.
