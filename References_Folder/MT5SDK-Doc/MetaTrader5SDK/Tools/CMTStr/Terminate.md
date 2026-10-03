[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTStr](../CMTStr.md) / Terminate

[Previous](FormatStr.md) | [Next](Append.md)

# CMTStr::Terminate

Null the last element (insert end of line character) of the specified string.
    
    
    static void  CMTStr::Terminate(
       wchar_t  (&str)[strsize]      // String
       )

### Parameters

**( &str)[strsize]**  
[in][out] The string (array of strings), in which you want to null the last character.
