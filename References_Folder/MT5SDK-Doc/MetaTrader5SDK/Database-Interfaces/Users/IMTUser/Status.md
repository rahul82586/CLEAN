[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / Status

[Previous](VisitorID.md) | [Next](Comment.md)

# IMTUser::Status

Get a client's status.

C++
    
    
    LPCWSTR  IMTUser::Status()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTUser.Status()

### Return Value

If successful, it returns a pointer to a string with the status of a client. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTUser](../IMTUser.md) object.

# IMTUser::Status

Set a client's status.

C++
    
    
    MTAPIRES  IMTUser::Status(
       LPCWSTR  id      // Status
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.Status(
       string   id      // Status
       )

### Parameters

**id**  
[in] The status of a client.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The length of the status is limited to 16 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
