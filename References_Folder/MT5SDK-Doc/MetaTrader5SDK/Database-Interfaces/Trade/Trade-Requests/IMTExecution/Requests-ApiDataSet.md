[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests ApiDataSet

[Previous](Requests-EOSRolloverValue.md) | [Next](Requests-ApiDataGet.md)

# IMTExecution::ApiDataSet

Set the custom parameter of type INT64 for a trade execution.

C++
    
    
    MTAPIRES  IMTExecution::ApiDataSet(
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       const INT64   value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.ApiDataSet(
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       long          value       // Parameter value
       )

### Parameters

**app_id**  
[in] The ID of the application which sets the custom parameter. Values from 1 to 4095 inclusive.

**id**  
[in] Parameter ID. Values from 0 to 15 inclusive.

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A trade execution can contain up to 8 custom parameters.

# IMTExecution::ApiDataSet

Set the custom parameter of type UINT64 for a trade execution.

C++
    
    
    MTAPIRES  IMTExecution::ApiDataSet(
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       const UINT64  value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.ApiDataSet(
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       ulong         value       // Parameter value
       )

### Parameters

**app_id**  
[in] The ID of the application which sets the custom parameter. Values from 1 to 4095 inclusive.

**id**  
[in] Parameter ID. Values from 0 to 15 inclusive.

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A trade execution can contain up to 8 custom parameters.

# IMTExecution::ApiDataSet

Set the custom parameter of type double for a trade execution.

C++
    
    
    MTAPIRES  IMTExecution::ApiDataSet(
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       const double  value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.ApiDataSet(
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       double        value       // Parameter value
       )

### Parameters

**app_id**  
[in] The ID of the application which sets the custom parameter. Values from 1 to 4095 inclusive.

**id**  
[in] Parameter ID. Values from 0 to 15 inclusive.

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A trade execution can contain up to 8 custom parameters.
