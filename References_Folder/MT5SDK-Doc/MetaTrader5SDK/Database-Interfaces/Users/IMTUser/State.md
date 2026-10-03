[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / State

[Previous](City.md) | [Next](ZipCode.md)

# IMTUser::State

Get a client's state (region) of residence.

C++
    
    
    LPCWSTR  IMTUser::State()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTUser.State()

### Return Value

If successful, it returns a pointer to the string with the state of residence. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTUser](../IMTUser.md) object.

# IMTUser::State

Set a client's state (region) of residence.

C++
    
    
    MTAPIRES  IMTUser::State(
       LPCWSTR  state      // State
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.State(
       string   state      // State
       )

### Parameters

**state**  
[in] The client's state (region) of residence.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The state name length is limited to 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
