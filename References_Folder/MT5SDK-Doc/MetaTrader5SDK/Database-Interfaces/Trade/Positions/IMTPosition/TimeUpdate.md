[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / TimeUpdate

[Previous](TimeCreate.md) | [Next](TimeCreateMsc.md)

# IMTPosition::TimeUpdate

Get the time of the last modification of a trade position.

C++
    
    
    INT64  IMTPosition::TimeUpdate()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTPosition.TimeUpdate()

### Return Value

Time of the last modification of a position, in seconds that have elapsed since 01.01.1970.

### Note

Position modification time is the time of its last volume modification. It is actually the time of the last deal of the financial instrument that corresponds to this position. This time does not change when Stop Loss or Take Profit is modified or when the position is edited via the Administrator terminal or API.

# IMTPosition::TimeUpdate

Set the time of the last modification of a trade position.

C++
    
    
    MTAPIRES  IMTPosition::TimeUpdate(
       const INT64  time      // Last modification time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.TimeUpdate(
       long         time      // Last modification time
       )

### Parameters

**time**  
[in] Time of the last modification of a position, in seconds that have elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

If the value of this field is specified, the [IMTPosition::TimeUpdateMsc](TimeUpdateMsc.md) value will be filled in automatically.
