[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / Constructor

[Previous](../CMTArrayBase.md) | [Next](Templates.md)

# Constructor

The size of elements in the array and the array change step for memory reallocation are specified in the CMTArrayBase class constructor.
    
    
    CMTArrayBase::CMTArrayBase(
       const UINT  width,     // Element size
       const UINT  step       // Size change step
       )

### Parameters

**width**  
[in] The size of one array element in bytes.

**step**  
[in] The array size change step for reallocation of memory for the array. The step is specified as a number of elements.
