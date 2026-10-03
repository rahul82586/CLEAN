[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / APIDataUpdate

[Previous](APIDataNext.md) | [Next](ApiDataGet.md)

# IMTDeal::APIDataUpdate

Changes the custom parameter of type INT64 for a deal.

C++
    
    
    MTAPIRES  IMTDeal::APIDataUpdate(
       const UINT    pos,        // Parameter position
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       const INT64   value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.APIDataUpdate(
       uint          pos,        // Parameter position
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       long          value       // A reference to the value
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

A deal can contain up to 8 custom parameters.

# IMTDeal::APIDataUpdate

Changes the custom parameter of type UINT64 for a deal.

C++
    
    
    MTAPIRES  IMTDeal::APIDataUpdate(
       const UINT    pos,        // Parameter position
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       const UINT64  value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.APIDataUpdate(
       uint          pos,        // Parameter position
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       ulong         value       // A reference to the value
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

A deal can contain up to 8 custom parameters.

# IMTDeal::APIDataUpdate

Changes the custom parameter of type double for a deal.

C++
    
    
    MTAPIRES  IMTDeal::APIDataUpdate(
       const UINT    pos,        // Parameter position
       const USHORT  app_id,     // Application ID
       const UCHAR   id,         // Parameter ID
       const double  value       // Parameter value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.APIDataUpdate(
       uint          pos,        // Parameter position
       ushort        app_id,     // Application ID
       byte          id,         // Parameter ID
       double        value       // A reference to the value
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

A deal can contain up to 8 custom parameters.
