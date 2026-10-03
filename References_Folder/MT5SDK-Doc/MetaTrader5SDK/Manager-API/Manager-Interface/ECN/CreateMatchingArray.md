[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [ECN](../ECN.md) / CreateMatchingArray

[Previous](CreateMatching.md) | [Next](CreateFilling.md)

# IMTManagerAPI::ECNCreateMatchingArray

Create an array of matching order objects.

C++
    
    
    IMTECNMatchingArray*  IMTManagerAPI::ECNCreateMatchingArray()

.NET
    
    
    CIMTECNMatchingArray  CIMTManagerAPI.ECNCreateMatchingArray()

### Return Value

The function returns a pointer to the created object that implements the [IMTECNMatchingArray](../../../Database-Interfaces/ECN/IMTMatchingArray.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTECNMatchingArray::Release](../../../Database-Interfaces/ECN/IMTECNMatchingArray/IMTMatchingArray-Release.md) method of this object.
