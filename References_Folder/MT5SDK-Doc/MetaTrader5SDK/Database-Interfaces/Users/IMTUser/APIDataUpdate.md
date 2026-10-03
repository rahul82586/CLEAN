[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / APIDataUpdate

[Previous](APIDataNext.md) | [Next](APIDataClear.md)

# IMTUser::APIDataUpdate

Updates a custom parameter of type INT64 for a client record.

C++
    
    
    MTAPIRES  IMTUser::APIDataUpdate(
       const UINT    pos,        // Parameter position
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       const INT64   value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTAPIRES  IMTUser::APIDataUpdate(
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

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A client record can contain up to 16 custom parameters.

# IMTUser::APIDataUpdate

Updates a custom parameter of type UINT64 for a client record.

C++
    
    
    MTAPIRES  IMTUser::APIDataUpdate(
       const UINT    pos,        // Parameter position
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       const UINT64  value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTAPIRES  IMTUser::APIDataUpdate(
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

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A client record can contain up to 16 custom parameters.

# IMTUser::APIDataUpdate

Updates a custom parameter of double type for a client record.

C++
    
    
    MTAPIRES  IMTUser::APIDataUpdate(
       const UINT    pos,        // Parameter position
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       const double  value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTAPIRES  IMTUser::APIDataUpdate(
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

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A client record can contain up to 16 custom parameters.
