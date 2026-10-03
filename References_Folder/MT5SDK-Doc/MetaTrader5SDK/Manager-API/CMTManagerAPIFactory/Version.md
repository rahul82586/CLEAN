[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [CMTManagerAPIFactory](../CMTManagerAPIFactory.md) / Version

[Previous](CreateAdmin.md) | [Next](LicenseCheckAdmin.md)

# CMTManagerAPIFactory::Version

Get the version of the Manager Manager API.

C++
    
    
    MTAPIRES  CMTManagerAPIFactory::Version(
       UINT&    version    // Version
       )

.NET
    
    
    MTRetCode  SMTManagerAPIFactory.GetVersion(
       out uint version    // Version
       )

### Parameters

**& version**  
[out] The version of the Manager API library.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
