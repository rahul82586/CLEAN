[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Print

[Previous](Clear.md) | [Next](Deal.md)

# IMTDeal::Print

Get the string description of a deal.

C++
    
    
    LPCWSTR  IMTDeal::Print(
       MTAPISTR&  string      // The deal description string
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTDeal.Print()

### Parameters

**string**  
[out] The deal description string.

### Return Value

A pointer to string that is passed as a parameter.

### Note

The description string does not include the login of the client, to whom the deal belongs.
