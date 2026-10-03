[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / LastAccess

[Previous](RegistrationSet.md) | [Next](LastIP.md)

# IMTUser::LastAccess

Get the date of the last connection using the account.

C++
    
    
    INT64  IMTUser::LastAccess()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTUser.LastAccess()

### Return Value

Date of teh last connection in seconds that have elapsed since 01.01.1970.
