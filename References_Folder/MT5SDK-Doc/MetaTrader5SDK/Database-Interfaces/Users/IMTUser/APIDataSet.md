[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / APIDataSet

[Previous](LimitPositionsValue.md) | [Next](APIDataGet.md)

# IMTUser::ApiDataSet

Set the custom parameter of type INT64 for a client record.

C++
    
    
    MTAPIRES  IMTUser::ApiDataSet(
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       const INT64   value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.ApiDataSet(
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       long          value       // Parameter value
       )

### Parameters

**app_id**  
[in] The ID of the application that sets the custom parameter. Values ​​from 1 to 4095 inclusive are allowed.

**id**  
[in] Parameter ID. Values ​​from 0 to 15 inclusive are allowed.

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A client record can contain up to 16 custom parameters.

# IMTUser::ApiDataSet

Set the custom parameter of type UINT64 for a client record.

C++
    
    
    MTAPIRES  IMTUser::ApiDataSet(
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       const UINT64  value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.ApiDataSet(
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       ulong         value       // Parameter value
       )

### Parameters

**app_id**  
[in] The ID of the application that sets the custom parameter. Values ​​from 1 to 4095 inclusive are allowed.

**id**  
[in] Parameter ID. Values ​​from 0 to 15 inclusive are allowed.

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A client record can contain up to 16 custom parameters.

# IMTUser::ApiDataSet

Set the custom parameter of the double type for a client record.

C++
    
    
    MTAPIRES  IMTUser::ApiDataSet(
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       const double  value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.ApiDataSet(
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       double        value       // Parameter value
       )

### Parameters

**app_id**  
[in] The ID of the application that sets the custom parameter. Values ​​from 1 to 4095 inclusive are allowed.

**id**  
[in] Parameter ID. Values ​​from 0 to 15 inclusive are allowed.

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A client record can contain up to 16 custom parameters.
