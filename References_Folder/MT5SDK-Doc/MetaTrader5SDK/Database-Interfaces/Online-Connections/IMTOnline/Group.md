[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Online Connections](../../Online-Connections.md) / [IMTOnline](../IMTOnline.md) / Group

[Previous](Login.md) | [Next](Address.md)

# IMTOnline::Group

Get the group to which the user is included.

C++
    
    
    LPCWSTR  IMTOnline::Group()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTOnline.Group()

### Return Value

If successful, it returns a pointer to a string with the group of a user. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTUser](../../Users/IMTUser.md) object.

# 
