[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [CMTGatewayAPIFactory](../CMTGatewayAPIFactory.md) / Initialize

[Previous](../CMTGatewayAPIFactory.md) | [Next](Shutdown.md)

# CMTGatewayAPIFactory::Initialize

Loading of Gateway API library and all [functions exported by it](../Exported-Functions.md).

C++
    
    
    MTAPIRES  CMTGatewayAPIFactory::Initialize()

.NET
    
    
    MTRetCode  SMTGatewayAPIFactory.Initialize()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method determines the application bitness (32 or 64-bit) and loads an appropriate library.

  * In the directory where the application executable is located.
  * In the parent directory, then in the next upper-level directory and so on, up to five levels up from the executable files directory.
  * Using the path from the system PATH variable.


