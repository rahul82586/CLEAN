[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests APIDataUpdate

[Previous](Requests-ApiDataGet.md) | [Next](Requests-APIDataNext.md)

# IMTRequest::APIDataUpdate

Change the custom parameter of type INT64 for a trade request.

C++
    
    
    MTAPIRES  IMTRequest::APIDataUpdate(
       const UINT    pos,        // Parameter position
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter identifier
       const INT64   value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.APIDataUpdate(
       uint          pos,        // Parameter position
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       long          value       // Parameter value
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

**app_id**  
[in] The ID of the application which sets the custom parameter.

**id**  
[in] Parameter ID.

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

A trade request can contain up to 8 custom parameters.

  * TA_REQUEST
  * TA_INSTANT
  * TA_MARKET
  * TA_EXCHANGE
  * TA_PENDING
  * TA_CLOSE_BY
  * TA_DEALER_POS_EXECUTE
  * TA_DEALER_ORD_PENDING
  * TA_DEALER_CLOSE_BY



# IMTRequest::APIDataUpdate

Change the custom parameter of type UINT64 for a trade request.

C++
    
    
    MTAPIRES  IMTRequest::APIDataUpdate(
       const UINT    pos,        // Parameter position
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter identifier
       const UINT64  value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.APIDataUpdate(
       uint          pos,        // Parameter position
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       ulong         value       // Parameter value
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

**app_id**  
[in] The ID of the application which sets the custom parameter.

**id**  
[in] Parameter ID.

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

A trade request can contain up to 8 custom parameters.

  * TA_REQUEST
  * TA_INSTANT
  * TA_MARKET
  * TA_EXCHANGE
  * TA_PENDING
  * TA_CLOSE_BY
  * TA_DEALER_POS_EXECUTE
  * TA_DEALER_ORD_PENDING
  * TA_DEALER_CLOSE_BY



# IMTRequest::APIDataUpdate

Change the custom parameter of type UINT64 for a trade request.

C++
    
    
    MTAPIRES  IMTRequest::APIDataUpdate(
       const UINT    pos,        // Parameter position
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter identifier
       const double  value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.APIDataUpdate(
       uint          pos,        // Parameter position
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       double        value       // Parameter value
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

**app_id**  
[in] The ID of the application which sets the custom parameter.

**id**  
[in] Parameter ID.

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

A trade request can contain up to 8 custom parameters.

  * TA_REQUEST
  * TA_INSTANT
  * TA_MARKET
  * TA_EXCHANGE
  * TA_PENDING
  * TA_CLOSE_BY
  * TA_DEALER_POS_EXECUTE
  * TA_DEALER_ORD_PENDING
  * TA_DEALER_CLOSE_BY


