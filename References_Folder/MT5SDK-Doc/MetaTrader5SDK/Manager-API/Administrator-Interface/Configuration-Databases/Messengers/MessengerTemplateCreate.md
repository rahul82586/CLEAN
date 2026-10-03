[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / MessengerTemplateCreate

[Previous](MessengerGroupCreate.md) | [Next](MessengerSubscribe.md)

# IMTAdminAPI::MessengerTemplateCreate

Создание объекта шаблона сообщений, которой будет использоваться в мессенджере.

C++
    
    
    IMTConMessengerTemplate*  IMTAdminAPI::MessengerTemplateCreate()

.NET
    
    
    CIMTConMessengerTemplate  CIMTAdminAPI.MessengerTemplateCreate()

### Возвращаемое значение

Возвращает указатель на созданный объект, реализующий интерфейс [IMTConMessengerTemplate](../../../../Configuration-Interfaces/Messengers/IMTConMessengerTemplate.md). В случае неудачи возвращается NULL.

### Примечание

Созданный объект должен быть уничтожен вызовом метода [IMTConMessengerTemplate::Release](../../../../Configuration-Interfaces/Messengers/IMTConMessengerTemplate/Release.md) этого объекта.
