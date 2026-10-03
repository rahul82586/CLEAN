[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTStr](../CMTStr.md) / Append

[Previous](Terminate.md) | [Next](Insert.md)

# CMTStr::Append

Add the specified string at the end of the string object.
    
    
    void  CMTStr::Append(
       LPCWSTR  appstring      // The string to add
       )

### Parameters

**appstring**  
[in] The string to add.

# CMTStr::Append

Add the specified string object at the end of the current string object.
    
    
    void  CMTStr::Append(
       const CMTStr  &appstring      // String object to add
       )

### Parameters

**& appstring**  
[in] TheCMTStrstring object that you want to add.

# CMTStr::Append

Add the specified character at the end of the string object.
    
    
    void  CMTStr::Append(
       wchar_t  appchar      // The character to add
       )

### Parameters

**appchar**  
[in] The character that you want to add.

# CMTStr::Append

Add the specified string at the end of another string.
    
    
    static void  CMTStr::Append(
       wchar_t  (&dst)[dstsize],     // String
       LPCWSTR  src                  // The string to add
       )

### Parameters

**( &dst)[dstsize]**  
[in][out] The wchar_t array of the dstsize size, at the end of which a string should be added. The dstsize size must be known to the compiler.

**src**  
The string to add.

# CMTStr::Append

Add the specified string at the end of another string with an explicitly indicated size.
    
    
    static void  CMTStr::Append(
       LPWSTR   dst,         // String
       UINT     dstsize,     // String buffer size
       LPCWSTR  src          // String to add
       )

### Parameters

**dst**  
[in][out] The string, into which the specified string will be added.

**dstsize**  
[in] The size of the string buffer (in characters), in which a string is added.

**src**  
[in] The string to add.
