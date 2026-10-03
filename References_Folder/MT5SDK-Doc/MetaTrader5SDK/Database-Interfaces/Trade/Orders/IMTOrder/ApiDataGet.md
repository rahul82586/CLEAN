[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / ApiDataGet

[Previous](ApiDataSet.md) | [Next](ApiDataClear.md)

# IMTOrder::ApiDataGet

Get the INT64 type value of a custom parameter of a trade order.

C++
    
    
    MTAPIRES  IMTOrder::ApiDataGet(
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       INT64&        value       // A reference to the value
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.ApiDataGet(
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       out long      value       // A reference to the value
       )

### Parameters

**app_id**  
[in] The ID of the application that has set the custom parameter.

**id**  
[in] Parameter ID.

**value**  
[out] A reference to the value of the custom parameter.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

# IMTOrder::ApiDataGet

Get the UINT64 type value of a custom parameter of a trade order.

C++
    
    
    MTAPIRES  IMTOrder::ApiDataGet(
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       UINT64&       value       // A reference to the value
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.ApiDataGet(
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       out ulong     value       // A reference to the value
       )

### Parameters

**app_id**  
[in] The ID of the application that has set the custom parameter.

**id**  
[in] Parameter ID.

**value**  
[out] A reference to the value of the custom parameter.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

# IMTOrder::ApiDataGet

Get the double type value of a custom parameter of a trade order.

C++
    
    
    MTAPIRES  IMTOrder::ApiDataGet(
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       double&       value       // A reference to the value
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.ApiDataGet(
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       out double    value       // A reference to the value
       )

### Parameters

**app_id**  
[in] The ID of the application that has set the custom parameter.

**id**  
[in] Parameter ID.

**value**  
[out] A reference to the value of the custom parameter.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
