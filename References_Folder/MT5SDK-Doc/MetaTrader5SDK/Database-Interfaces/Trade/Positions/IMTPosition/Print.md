[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / Print

[Previous](Clear.md) | [Next](Login.md)

# IMTPosition::Print

Get the string description of a position.

C++
    
    
    LPCWSTR  IMTPosition::Print(
       MTAPISTR&  string      // Position description string
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTPosition.Print()

### Parameters

**string**  
[out] The trade position description string.

### Return Value

A pointer to string that is passed as a parameter.

### Note

The description string does not include the login of the client, to whom the position belongs.
