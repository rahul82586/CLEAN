[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / Print

[Previous](Clear.md) | [Next](Order.md)

# IMTOrder::Print

Get the string description of an order.

C++
    
    
    LPCWSTR  IMTOrder::Print(
       MTAPISTR&  string      // The order description string
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTOrder.Print()

Python
    
    
    MTOrder.Print()

### Parameters

**string**  
[out] The order description string.

### Return Value

A pointer to string that is passed as a parameter.

### Note

The description string does not include the login of the client, to whom the order belongs.
