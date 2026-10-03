[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / ActivationTime

[Previous](ActivationMode.md) | [Next](ActivationPrice.md)

# IMTOrder::ActivationTime

Get the order activation time.

C++
    
    
    INT64  IMTOrder::ActivationTime()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTOrder.ActivationTime()

Python
    
    
    MTOrder.ActivationTime()

### Return Value

Date and time of the activation of an order, in seconds that have elapsed since 01.01.1970.
