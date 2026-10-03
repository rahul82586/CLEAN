[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / ActivationPrice

[Previous](ActivationTime.md) | [Next](ActivationFlags.md)

# IMTPosition::ActivationPrice

Get position activation price.

C++
    
    
    double  IMTPosition::ActivationPrice()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTPosition.ActivationPrice()

### Return Value

Position activation price.

### Note

Position activation price is the first price that has broken through the activation level (Margin Call or Stop Out).

# IMTPosition::ActivationPrice

Sets position activation price.

C++
    
    
    MTAPIRES  IMTPosition::ActivationPrice(
       const double  price      // Activation price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.ActivationPrice(
       double        price      // Activation price
       )

### Parameters

**price**  
[in] Position activation price.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
