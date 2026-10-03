[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Assets](../../Assets.md) / [IMTExposureArray](../IMTExposureArray.md) / Clear

[Previous](Assign.md) | [Next](Add.md)

# IMTExposureArray::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTExposureArray::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExposureArray.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
