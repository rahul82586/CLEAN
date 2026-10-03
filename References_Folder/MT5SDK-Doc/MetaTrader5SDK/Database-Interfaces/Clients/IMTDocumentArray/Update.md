[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocumentArray](../IMTDocumentArray.md) / Update

[Previous](Detach.md) | [Next](UpdateCopy.md)

# IMTDocumentArray::Update

Change a document at the specified position of an array.

C++
    
    
    MTAPIRES  IMTDocumentArray::Update(
       const UINT    pos,      // Position
       IMTDocument*  document  // Document object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocumentArray.Update(
       uint          pos,      // Position
       CIMTDocument  document  // Document object
       )

### Parameters

**pos**  
[in] Position of a document in an array starting with 0.

**document**  
[in]Document object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The IMTDocumentArray::Update method deletes the previous element ([IMTDocument::Release](../IMTDocument/Release.md) call) and replaces it with a new one. After that, the lifetime of a new element is controlled by an array object. Thus, when deleting an array object (by IMTDocumentArray::Release call), an earlier inserted object is automatically removed.

### Example
    
    
    //--- example
       IMTDocumentArray *array    =api->DocumentCreateArray();   
       IMTDocument      *document1=api->DocumentCreate();
       IMTDocument      *document2=api->DocumentCreate();
    //---
       array->Add(document1);
       array->Update(0,document2); // the first element (object document1) is replaced by document2
       //--- after that the document1 element will be released via Release, and the document2 lifetime will be controlled by the array
