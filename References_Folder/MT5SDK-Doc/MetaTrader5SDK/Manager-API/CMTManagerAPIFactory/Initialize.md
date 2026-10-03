[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [CMTManagerAPIFactory](../CMTManagerAPIFactory.md) / Initialize

[Previous](../CMTManagerAPIFactory.md) | [Next](Shutdown.md)

# CMTManagerAPIFactory::Initialize

Initialize the Manager API.

C++
    
    
    MTAPIRES  CMTManagerAPIFactory::Initialize(
       LPCWSTR  dll_path=NULL  // Path to DLL library of the API
       )

.NET
    
    
    MTRetCode  SMTManagerAPIFactory.Initialize(
       string  dll_path=NULL  // Path to DLL library of the API
       )

### Parameters

**dll_path**  
[in] Full path to DLL library of the Manager API. An optional parameter. If the path is not specified, the method will try to find a library in the following order:

  * In the directory where the application executable is located.
  * In the parent directory, then in the next upper-level directory and so on, up to five levels up from the executable files directory.
  * Using the path from the system PATH variable.



### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code will be returned.

### Note

The method loads the DLL of the Manager API and gets addresses of [exported functions](../Exported-Functions.md). Depending on the application architecture, the 32-bit or 64-bit version of DLL is loaded.
