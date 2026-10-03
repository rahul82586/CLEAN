[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRouteDealer](../IMTConRouteDealer.md) / Name

[Previous](Login.md) | [Next](../IMTConRouteSink.md)

# IMTConRouteDealer::Name

Get the name of a dealer to whom requests under this rule will be sent.

C++
    
    
    LPCWSTR  IMTConRouteDealer::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConRouteDealer.Name()

Python (Manager API)
    
    
    MTConRouteDealer.Name

### Return Value

If successful, it returns a pointer to a string with the name of a dealer. Otherwise, it returns NULL.

### Note

The name of the dealer is defined by the user account ([IMTUser::Name](../../../Database-Interfaces/Users/IMTUser/Name.md)), based on which the manager record is create.
