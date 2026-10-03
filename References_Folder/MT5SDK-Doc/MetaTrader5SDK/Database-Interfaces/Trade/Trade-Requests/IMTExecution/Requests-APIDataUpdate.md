[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests APIDataUpdate

[Previous](Requests-ApiDataGet.md) | [Next](Requests-APIDataNext.md)

# IMTExecution::APIDataUpdate

Add or update the custom parameter of type INT64 for a trade execution.

C++
    
    
    MTAPIRES  IMTExecution::APIDataUpdate(
       const UINT    pos,        // Parameter position
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       const INT64   value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.APIDataUpdate(
       uint          pos,        // Parameter position
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       long          value       // Parameter value
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

**app_id**  
[in] The ID of the application that sets the custom parameter.

**id**  
[in] Parameter ID.

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A trade execution can contain up to 8 custom parameters.

# IMTExecution::APIDataUpdate

Add or update the custom parameter of type UINT64 for a trade execution.

C++
    
    
    MTAPIRES  IMTExecution::APIDataUpdate(
       const UINT    pos,        // Parameter position
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       const UINT64  value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.APIDataUpdate(
       uint          pos,        // Parameter position
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       ulong         value       // Parameter value
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

**app_id**  
[in] The ID of the application that sets the custom parameter.

**id**  
[in] Parameter ID.

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A trade execution can contain up to 8 custom parameters.

# IMTExecution::APIDataUpdate

Add or update the custom parameter of the double type for a trade execution.
    
    
    MTAPIRES  IMTExecution::APIDataUpdate(
       const UINT    pos,        // Parameter position
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       const double  value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.APIDataUpdate(
       uint          pos,        // Parameter position
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       double        value       // Parameter value
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

**app_id**  
[in] The ID of the application that sets the custom parameter.

**id**  
[in] Parameter ID.

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A trade execution can contain up to 8 custom parameters.
