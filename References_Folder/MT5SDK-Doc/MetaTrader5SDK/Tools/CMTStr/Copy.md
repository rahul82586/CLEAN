[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTStr](../CMTStr.md) / Copy

[Previous](Insert.md) | [Next](CopyCodePage.md)

# CMTStr::Copy

Copy data from an object to a string of the specified size.
    
    
    void  CMTStr::Copy(
       LPWSTR  string,     // String
       UINT    maxlen      // String size
       )  const

### Parameters

**string**  
[out] The string, to which the data from the current string is copied.

**maxlen**  
[in] The size of the string buffer (in characters), in which data is copied.

# CMTStr::Copy

Copy data from an object to an ANSI string of the specified size.
    
    
    void  CMTStr::Copy(
       LPSTR  string,     // String
       UINT   maxlen      // String size
       )  const

### Parameters

**string**  
[out] The string, to which the data from the current string is copied.

**maxlen**  
[in] The size of the string buffer (in characters), in which data is copied.

### Note

When you copy data to a string, they are converted from the Unicode format to ANSI.

# CMTStr::Copy

Copy data from one string to another.
    
    
    static void  CMTStr::Copy(
       wchar_t  (&dst)[dstsize],     // Resulting string
       LPCWSTR  src                  // Source string
       )

### Parameters

**( &dst)[dstsize]**  
[in] The wchar_t array of the dstsize size, to which you copy data. The dstsize size must be known to the compiler.

**src**  
[out] The string, from which you copy data.

# CMTStr::Copy

Copy the specified amount of data from one string to another.
    
    
    static void  CMTStr::Copy(
       wchar_t  (&dst)[dstsize],     // Resulting string
       LPCWSTR  src,                 // Source string
       UINT     srccount             // Number of characters
       )

### Parameters

**( &dst)[dstsize]**  
[in] The wchar_t array of the dstsize size, to which you copy data. The dstsize size must be known to the compiler.

**src**  
[out] The string, from which you copy data.

**srccount**  
[in] Size of data (in characters) that you want to copy.

# CMTStr::Copy

Copy data from one string to another with an indication of its size.
    
    
    static void  CMTStr::Copy(
       LPWSTR   dst,         // Resulting string
       UINT     dstsize,     // String buffer size
       LPCWSTR  src          // Source string
       )

### Parameters

**dst**  
[out] The string, to which you copy data.

**dstsize**  
[in] The size of the string buffer (in characters), in which data is copied.

**src**  
[in] The string, from which you copy data.

# CMTStr::Copy

Copy the specified amount of data from one string to another.
    
    
    static void  CMTStr::Copy(
       LPWSTR   dst,          // Resulting string
       UINT     dstsize,      // The size of the resulting string
       LPCWSTR  src,          // Source string
       UINT     srccount      // Number of characters
       )

### Parameters

**dst**  
[out] The string, to which you copy data.

**dstsize**  
[in] The size of the string buffer (in characters), in which data is copied.

**src**  
[in] The string, from which you copy data.

**srccount**  
[in] Size of data (in characters) that you want to copy.

# CMTStr::Copy

Copy data from a Unicode string to an ANSI string.
    
    
    static void  CMTStr::Copy(
       char     (&dst)[dstsize],     // Resulting string
       LPCWSTR  src                  // Source string
       )

### Parameters

**( &dst)[dstsize]**  
[out] The char array of the dstsize size, to which you copy data. The dstsize size must be known to the compiler.

**src**  
[in] The string, from which you copy data.

# CMTStr::Copy

Copy data from a Unicode string to an ANSI string with the specified size.
    
    
    static void  CMTStr::Copy(
       LPSTR    dst,         // Resulting string
       UINT     dstsize,     // The size of the resulting string
       LPCWSTR  src          // Source string
       )

### Parameters

**dst**  
[out] The string, to which you copy data.

**dstsize**  
[in] The size of the string buffer (in characters), in which data is copied.

**src**  
[in] The string, from which you copy data.

# CMTStr::Copy

Copy data from an ANSI string to a Unicode string.
    
    
    static void  CMTStr::Copy(
       LPWSTR  dst,         // Resulting string
       UINT    dstsize,     // The size of the resulting string
       LPCSTR  src          // Source string
       )

### Parameters

**dst**  
[out] The string, to which you copy data.

**dstsize**  
[in] The size of the string buffer (in characters), in which data is copied.

**src**  
[in] The string, from which you copy data.
