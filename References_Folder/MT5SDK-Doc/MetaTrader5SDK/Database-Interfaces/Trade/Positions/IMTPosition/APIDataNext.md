[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / APIDataNext

[Previous](Dealer.md) | [Next](ModificationFlags.md)

# IMTPosition::APIDataNext

Gets a custom parameter of a trade position of the INT64 type by the parameter position.

C++
    
    
    MTAPIRES  IMTPosition::APIDataNext(
       const UINT     pos,        // Position of the parameter
       const USHORT&  app_id,     // Application ID
       const UCHAR&   id,         // Parameter ID
       INT64&         value       // A reference to the value
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.APIDataNext(
       uint           pos,        // Position of the parameter
       out ushort     app_id,     // Application ID
       out byte       id,         // Parameter ID
       out long       value       // Value
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

**app_id**  
[out] A pointer to the ID of the application that gas set the custom parameter.

**id**  
[out] A pointer to the parameter ID.

**value**  
[out] A pointer to a value of the custom parameter.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

# IMTPosition::APIDataNext

Gets a custom parameter of a trade position of the UINT64 type by the parameter position.

C++
    
    
    MTAPIRES  IMTPosition::APIDataNext(
       const UINT     pos,        // Position of the parameter
       const USHORT&  app_id,     // Application ID
       const UCHAR&   id,         // Parameter ID
       UINT64&        value       // A pointer to the value
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.APIDataNext(
       uint           pos,        // Position of the parameter
       out ushort     app_id,     // Application ID
       out byte       id,         // Parameter ID
       out ulong      value       // Value
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

**id**  
[out] A pointer to the parameter ID.

**value**  
[out] A pointer to a value of the custom parameter.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

# IMTPosition::APIDataNext

Gets a custom parameter of a trade position of the double type by the parameter position.

C++
    
    
    MTAPIRES  IMTPosition::APIDataNext(
       const UINT     pos,        // Position of the parameter
       const USHORT&  app_id,     // Application ID
       const UCHAR&   id,         // Parameter ID
       double&        value       // A pointer to the value
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.APIDataNext(
       uint           pos,        // Position of the parameter
       out ushort     app_id,     // Application ID
       out byte       id,         // Parameter ID
       out double     value       // Value
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

**app_id**  
[out] A pointer to the ID of the application that gas set the custom parameter.

**id**  
[out] A pointer to the parameter ID.

**value**  
[out] A pointer to a value of the custom parameter.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
