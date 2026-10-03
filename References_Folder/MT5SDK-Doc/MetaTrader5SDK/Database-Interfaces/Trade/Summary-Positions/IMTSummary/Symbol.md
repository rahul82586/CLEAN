[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummary](../IMTSummary.md) / Symbol

[Previous](Clear.md) | [Next](Digits.md)

# IMTSummary::Symbol

Gets the symbol, for which summary positions are calculated.

C++
    
    
    LPCWSTR  IMTSummary::Symbol()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTSummary.Symbol()

### Return Value

If successful, it returns a pointer to a string with the name of the symbol. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTSummary](../IMTSummary.md) object.

To use the string after the object removal (call of the [IMTSummary::Release](Release.md) method of this object), a copy of it should be created.
