[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / RegistrationSet

[Previous](Registration.md) | [Next](LastAccess.md)

# IMTUser::RegistrationSet

Set the client record creation date.

C++
    
    
    MTAPIRES  IMTUser::RegistrationSet(
       const INT64  date  // Creation date
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.RegistrationSet(
       long         date  // Creation date
       )

### Parameters

**date**  
[in] Client record creation date in seconds that have elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Please be careful when changing the registration date manually: data should fit the account trading history, and thus there should not be any trading operations before the registration date. Otherwise, such operations can be ignored when generating reports.
