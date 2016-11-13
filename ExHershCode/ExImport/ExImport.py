# import SampleImportModule
from SampleImportModule import ExImportedModule


# by using "from" for import, can call imported module without needing prefix
myModule = ExImportedModule()     # If we didn't use "from" for import, would need: myModule = SampleImportModule.ExImportedModule()
myModule.add(2)
print(myModule.get_current())