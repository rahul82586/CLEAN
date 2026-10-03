[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTStr](../CMTStr.md) / FormatStr

[Previous](Delete.md) | [Next](Terminate.md)

# CMTStr::FormatStr

Fill in the specified string in accordance with the format string.
    
    
    static int  CMTStr::FormatStr(
       wchar_t  (&str)[strsize],     // Resulting string
       LPCWSTR  fmt,                 // Format string
                ...                  // Additional parameters
       )

### Parameters

**( &str)[strsize]**  
[out] A pointer to the wchar_t array of the strsize size, in which the resulting string is formed. The strsize size must be known to the compiler.

**fmt**  
[in] Format string (pattern). For example, to get the string 100 / 300, specify: Format("%d / % d",100,300);

**...**  
[in] The number of additional parameters is not limited and depends on the format string.

### Return Value

The length of the formed string in characters.

# CMTStr::FormatStr

Fill in the specified string in accordance with the format string.
    
    
    static int  CMTStr::FormatStr(
       LPWSTR   str,      // Resulting string
       UINT     size,     // The size of the resulting string
       LPCWSTR  fmt,      // Format string
                ...       // Additional parameters
       )

### Parameters

**str**  
[out] A pointer to a Unicode string, in which the resulting string is placed.

**size**  
[in] The size of the buffer for the resulting string in characters.

**fmt**  
[in] Format string (pattern). For example, to get the string 100 / 300, specify: Format("%d / % d",100,300);

**...**  
[in] The number of additional parameters is not limited and depends on the format string.

### Return Value

The length of the formed string in characters.
