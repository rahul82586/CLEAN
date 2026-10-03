[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTConfirm](../Requests-IMTConfirm.md) / Requests Retcode

[Previous](Requests-ID.md) | [Next](Requests-Volume.md)

# IMTConfirm::Retcode

Get the confirmation return code.

C++
    
    
    MTAPIRES  IMTConfirm::Retcode()  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConfirm.Retcode()

### Return Value

A value of the [EnMTAPIRetcode](../../../../Return-Codes/README.md) enumeration.

# IMTConfirm::Retcode

Set the return code in the confirmation.

C++
    
    
    MTAPIRES  IMTConfirm::Retcode(
       const MTAPIRES  retcode      // Return code
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConfirm.Retcode(
       MTRetCode       retcode      // Return code
       )

### Parameters

**retcode**  
[in] Return code. To pass the code, theEnMTAPIRetcodeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
