[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTStr](../CMTStr.md) / ToLower

[Previous](Format.md) | [Next](ToUpper.md)

# CMTStr::ToLower

Convert all characters in a string object to lower case.
    
    
    void  CMTStr::ToLower()

# CMTStr::ToLower

Convert all characters in the specified string to lower case.
    
    
    static void  CMTStr::ToLower(
       LPWSTR  str,      // String
       UINT    size      // Buffer size
       )

### Parameters

**str**  
[in][out] A pointer to the Unicode string.

**size**  
[in] Buffer size (in characters), in which the Unicode string is located.

# CMTStr::ToLower

Convert all characters in the specified string to lower case.
    
    
    static void  CMTStr::ToLower(
       wchar_t  (&str)[size]      // String
       )

### Parameters

**( &str)[size]**  
[in][out] The string, in which you want to convert all characters to lower case (a pointer to the str buffer of the size size).

### Note

To use this method, the compiler must know the size of the string buffer.
