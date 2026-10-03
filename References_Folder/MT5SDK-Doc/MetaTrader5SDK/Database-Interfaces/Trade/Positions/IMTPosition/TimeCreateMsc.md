[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / TimeCreateMsc

[Previous](TimeUpdate.md) | [Next](TimeUpdateMsc.md)

# IMTPosition::TimeCreateMsc

Gets position creation time in milliseconds.

C++
    
    
    INT64  IMTPosition::TimeCreateMsc()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTPosition.TimeCreateMsc()

### Return Value

Date and time of position creation, in milliseconds that have elapsed since 01.01.1970.

# IMTPosition::TimeCreateMsc

Sets position creation time in milliseconds.

C++
    
    
    MTAPIRES  IMTPosition::TimeCreateMsc(
       const INT64  time      // Creation time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.TimeCreateMsc(
       long         time      // Creation time
       )

### Parameters

**time**  
[in] Date and time of position creation in milliseconds that have elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

If the value of this field is specified, the [IMTPosition::TimeCreate](TimeCreate.md) value will be filled in automatically.
