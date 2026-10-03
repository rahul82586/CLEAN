[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTStr](../CMTStr.md) / TrimSpaces

[Previous](Trim.md) | [Next](Replace.md)

# CMTStr::TrimSpaces

Remove all space characters from the beginning and end of the string.
    
    
    void  CMTStr::TrimSpaces()

### Note

The method does not remove spaces in the middle of the string. For example, the string " AB C " is converted to "AB C".

# CMTStr::TrimSpaces

Remove all space characters from the beginning and end of the specified string.
    
    
    static void  CMTStr::TrimSpaces(
       LPWSTR  str      // String
       )

### Parameters

**str**  
[in] The string, from which you want to remove space characters.

### Note

The method does not remove spaces in the middle of the string. For example, the string " AB C " is converted to "AB C".
