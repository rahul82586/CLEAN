[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / LastPassChange

[Previous](PhonePassword.md) | [Next](PasswordHash.md)

# IMTUser::LastPassChange

Gets the date of the last change of the user's password.

C++
    
    
    INT64  IMTUser::LastPassChange()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTUser.LastPassChange()

### Return Value

The date of the last password change in seconds that have elapsed since January 01, 1970.
