[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / Name

[Previous](LastIP.md) | [Next](FirstName.md)

# IMTUser::Name

Get the name of a client.

C++
    
    
    LPCWSTR  IMTUser::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTUser.Name()

### Return Value

If successful, it returns a pointer to a string with the name of a client. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTUser](../IMTUser.md) object.

# IMTUser::Name

Set the name of a client.

C++
    
    
    MTAPIRES  IMTUser::Name(
       LPCWSTR  name      // Name of a client
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.Name(
       string   name      // Name of a client
       )

### Parameters

**name**  
[in] The name of a client.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The maximum length of a client's symbol name is 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.

# How the method is used in the trading platform version 2265 and higher

The method is considered obsolete starting with the [platform version 2265](https://support.metaquotes.net/en/news/3110). The field was previously used for specifying the full name of the client. Now, three separate fields are used for specifying the name, the middle name and the last name: [IMTUser::FirstName](FirstName.md), [IMTUser::MiddleName](MiddleName.md) and [IMTUser::LastName](LastName.md).

In version 2265 and above, data can be received via the IMTUser::Name get-method as follows:

  * If the broker uses the previously adopted procedure and only the IMTUser::Name field is filled in a record, its value will be passed as a result.
  * If the broker has switched to the new system and the new fields LastName and MiddleName are filled in a record, the combined string "[IMTUser::Name] [IMTUser::MiddleName] [IMTUser::LastName]" will be returned as a result.



Thus the method always returns a correct value, no matter what system is used by the broker.

When using a set-method, the passed value is written to the IMTUser::Name property. In this case, the IMTUser::MiddleName and IMTUser::LastName values are forcibly deleted. Let us consider the reasons for this:

  * You set the full name using the old IMTUser::Name method.
  * If any values were left in the IMTUser::MiddleName and IMTUser::LastName field, then upon a call of the IMTUser::Name get-method you would receive the combined string "[IMTUser::Name] [IMTUser::MiddleName] [IMTUser::LastName]".
  * Since new fields are cleared upon the set-method call, the get-method will only return the previously set name value.



This ensures a correct operation with the platform data using old and new data.
