[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / ApiDataSet

[Previous](ActivationFlags.md) | [Next](ApiDataGet.md)

# IMTOrder::ApiDataSet

Set the custom parameter of type INT64 for a trade order.

C++
    
    
    MTAPIRES  IMTOrder::ApiDataSet(
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       const INT64   value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.ApiDataSet(
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       long          value       // A reference to the value
       )

### Parameters

**app_id**  
[in] The ID of the application that sets the custom parameter. Values ​​from 1 to 4095 inclusive are allowed.

**id**  
[in] Parameter ID. Values ​​from 0 to 15 inclusive are allowed.

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

A trade order can contain up to 8 custom parameters.

# IMTOrder::ApiDataSet

Set the custom parameter of type UINT64 for a trade order.

C++
    
    
    MTAPIRES  IMTOrder::ApiDataSet(
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       const UINT64  value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.ApiDataSet(
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       ulong         value       // A reference to the value
       )

### Parameters

**app_id**  
[in] The ID of the application that sets the custom parameter. Values ​​from 1 to 4095 inclusive are allowed.

**id**  
[in] Parameter ID. Values ​​from 0 to 15 inclusive are allowed.

**value**  
[in] Parameter value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

A trade order can contain up to 8 custom parameters.

# IMTOrder::ApiDataSet

Set the custom parameter of the double type for a trade order.

C++
    
    
    MTAPIRES  IMTOrder::ApiDataSet(
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       const double  value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.ApiDataSet(
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

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

A trade order can contain up to 8 custom parameters.
