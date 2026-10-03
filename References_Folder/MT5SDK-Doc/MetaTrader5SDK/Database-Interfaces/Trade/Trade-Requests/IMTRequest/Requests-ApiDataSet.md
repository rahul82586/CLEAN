[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests ApiDataSet

[Previous](Requests-Reason.md) | [Next](Requests-ApiDataGet.md)

# IMTRequest::ApiDataSet

Set the custom parameter of type INT64 for a trade request.

C++
    
    
    MTAPIRES  IMTRequest::ApiDataSet(
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter identifier
       const INT64   value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.ApiDataSet(
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       long          value       // Parameter value
       )

### Parameters

**app_id**  
[in] The ID of the application which sets the custom parameter. Values from 1 to 4095 inclusive are valid.

**id**  
[in] Parameter ID. Values from 0 to 15 inclusive are valid.

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



# IMTRequest::ApiDataSet

Set the custom parameter of type UINT64 for a trade request.

C++
    
    
    MTAPIRES  IMTRequest::ApiDataSet(
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter identifier
       const UINT64  value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.ApiDataSet(
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       ulong         value       // Parameter value
       )

### Parameters

**app_id**  
[in] The ID of the application which sets the custom parameter. Values from 1 to 4095 inclusive are valid.

**id**  
[in] Parameter ID. Values from 0 to 15 inclusive are valid.

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



# IMTRequest::ApiDataSet

Set the 'double' type custom parameter ofor a trade request.

C++
    
    
    MTAPIRES  IMTRequest::ApiDataSet(
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter identifier
       const double  value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.ApiDataSet(
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       double        value       // Parameter value
       )

### Parameters

**app_id**  
[in] The ID of the application which sets the custom parameter. Values from 1 to 4095 inclusive are valid.

**id**  
[in] Parameter ID. Values from 0 to 15 inclusive are valid.

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


