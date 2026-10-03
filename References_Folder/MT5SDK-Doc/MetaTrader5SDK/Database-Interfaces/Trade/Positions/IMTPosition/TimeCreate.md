[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / TimeCreate

[Previous](ExternalID.md) | [Next](TimeUpdate.md)

# IMTPosition::TimeCreate

Get position creation time.

C++
    
    
    INT64  IMTPosition::TimeCreate()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTPosition.TimeCreate()

### Return Value

Date and time of position creation, in seconds that have elapsed since 01.01.1970.

# IMTPosition::TimeCreate

Position creation time.

C++
    
    
    MTAPIRES  IMTPosition::TimeCreate(
       const INT64  time      // Creation time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.TimeCreate(
       long         time      // Creation time
       )

### Parameters

**time**  
[in] Date and time of position creation, in seconds that have elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

If the value of this field is specified, the [IMTPosition::TimeCreateMsc](TimeCreateMsc.md) value will be filled in automatically.
