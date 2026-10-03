[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTStr](../CMTStr.md) / Format

[Previous](Assign.md) | [Next](ToLower.md)

# CMTStr::Format

Fill in the string object in accordance with the format string.
    
    
    int  CMTStr::Format(
       LPCWSTR  fmt,     // Format string
                ...      // Additional parameters
       )

### Parameters

**fmt**  
[in] Format string (pattern). For example, to get the string 100 / 300, specify: Format("%d / % d",100,300);

**...**  
[in] The number of additional parameters is not limited and depends on the format string.

### Return Value

The length of the formed string in characters.
