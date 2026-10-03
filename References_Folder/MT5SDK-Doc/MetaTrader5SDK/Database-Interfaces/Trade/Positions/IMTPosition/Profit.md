[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / Profit

[Previous](VolumeExt.md) | [Next](Storage.md)

# IMTPosition::Profit

Get the current profit/loss of a trade position.

C++
    
    
    double  IMTPosition::Profit()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTPosition.Profit()

### Return Value

The current profit/loss of a trade position in the deposit currency of the account.

# IMTPosition::Profit

Set the current profit/loss of a trade position.

C++
    
    
    MTAPIRES  IMTPosition::Profit(
       const double  profit      // Current profit
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.Profit(
       double        profit      // Current profit
       )

### Parameters

**profit**  
[in] The current profit/loss of a trade position in the deposit currency of the account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
