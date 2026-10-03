[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / Compare

[Previous](Step.md) | [Next](Clear.md)

# CMTArrayBase::Compare

Comparison of the current object with the specified array.
    
    
    bool  CMTArrayBase::Compare(
       const CMTArrayBase&  array      // An array to compare
       )

### Parameters

**array**  
[in] A reference to theCMTArrayBasearray object, with which you need to compare the current array object.

### Return Value

Arrays are considered equal if their sizes ([CMTArrayBase::Width](Width.md)), the number of elements ([CMTArrayBase::Total](Total.md)) and contents are equal. In this case, it returns true. If the arrays are not equal, it returns false.
