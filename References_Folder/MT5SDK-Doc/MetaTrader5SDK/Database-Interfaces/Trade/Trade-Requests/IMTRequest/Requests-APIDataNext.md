[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests APIDataNext

[Previous](Requests-APIDataUpdate.md) | [Next](Requests-APIDataRaw.md)

# IMTRequest::APIDataNext

Get the INT64 type custom parameter of a trade request by a position.

C++
    
    
    MTAPIRES  IMTRequest::APIDataNext(
       const UINT     pos,        // Parameter position
       const USHORT&  app_id,     // Application ID
       const UCHAR&   id,         // Parameter ID
       INT64&         value       // A pointer to the value
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.APIDataNext(
       uint           pos,        // Parameter position
       out ushort     app_id,     // Application ID
       out byte       id,         // Parameter ID
       out long       value       // A pointer to the value
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

**app_id**  
[out] A pointer to the ID of the application which has set the custom parameter.

**id**  
[out] A pointer to the parameter identifier.

**value**  
[out] A pointer to the custom parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

# IMTRequest::APIDataNext

Get the UINT64 type custom parameter of a trade request by a position.

C++
    
    
    MTAPIRES  IMTRequest::APIDataNext(
       const UINT     pos,        // Parameter position
       const USHORT&  app_id,     // Application ID
       const UCHAR&   id,         // Parameter ID
       UINT64&        value       // A pointer to the value
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.APIDataNext(
       uint           pos,        // Parameter position
       out ushort     app_id,     // Application ID
       out byte       id,         // Parameter ID
       out ulong      value       // A pointer to the value
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

**app_id**  
[out] A pointer to the ID of the application which has set the custom parameter.

**id**  
[out] A pointer to the parameter identifier.

**value**  
[out] A pointer to the custom parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

# IMTRequest::APIDataNext

Get the 'double' type custom parameter of a trade request by a position.

C++
    
    
    MTAPIRES  IMTRequest::APIDataNext(
       const UINT     pos,        // Parameter position
       const USHORT&  app_id,     // Application ID
       const UCHAR&   id,         // Parameter ID
       double&        value       // A pointer to the value
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.APIDataNext(
       uint           pos,        // Parameter position
       out ushort     app_id,     // Application ID
       out byte       id,         // Parameter ID
       out double     value       // A pointer to the value
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

**app_id**  
[out] A pointer to the ID of the application which has set the custom parameter.

**id**  
[out] A pointer to the parameter identifier.

**value**  
[out] A pointer to the custom parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
