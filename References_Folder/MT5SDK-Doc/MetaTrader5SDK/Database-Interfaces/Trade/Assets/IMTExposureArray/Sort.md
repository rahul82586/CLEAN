[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Assets](../../Assets.md) / [IMTExposureArray](../IMTExposureArray.md) / Sort

[Previous](Next.md) | [Next](Search.md)

# IMTExposureArray::Sort

Sort an array using the sort function passed.
    
    
    MTAPIRES  IMTExposureArray::Sort(
       MTSortFunctionPtr  sort_function      // Sort function
       )

### Parameters

**sort_function**  
[in] A pointer to thesort function.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Positioning of elements after sorting is determined by the sort function sort_function.

### Example
    
    
    //+------------------------------------------------------------------+
    //| Function of comparing exposure for sorting                       |
    //+------------------------------------------------------------------+
    int SortExposure(const void* left,const void* right)
      {
       IMTExposure* lft=*(IMTExposure**)left;
       IMTExposure* rgh=*(IMTExposure**)right;
    //--- Compare by client volume
       return CMTStr::Compare(lft->VolumeClients(), rgh->VolumeClients());
      }
    //+------------------------------------------------------------------+
    //| Function of comparing exposure for searching                     |
    //+------------------------------------------------------------------+
    int SearchExposure(const void* left,const void* right)
      {
       double       lft=(double)left;
       IMTExposure* rgh=*(IMTExposure**)right;
    //--- Compare by client volume
       retrun CMTStr::Compare(lft, rgh->VolumeClients());
      }
    //+------------------------------------------------------------------+
    //| Example of sorting and searching                                |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTExposureArray* array;
       double            VolumeClients;
       int               index;
       ...
    //--- Initializing and filling the array of exposures
       ...
    //--- Sorting
       array->Sort(SortExposure);
    //--- Search
       index=array->Search(345,SearchExposure);
    //---
       return(0);
      }
