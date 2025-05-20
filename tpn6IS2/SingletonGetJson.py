from SingletonMeta import SingletonMeta
import json

class SingletonGetJson(metaclass=SingletonMeta):

    jsonFile = ".\sitedata.json"
    data = None
    obj = None

    def getJasonToken(self):
        if self.obj is None:
            try:
                with open(self.jsonFile, 'r') as (myfile):
                    self.data = myfile.read()
            except:
                print ("Ups, hubo un error al intentar abrir el archivo sitedata.json")

            try:
                self.obj = json.loads(self.data)
            except:
                print ("Error, no se pudieron cargar los datos " + self.jsonFile + "\sitedata.json")

        return self.obj

    def getToken(self, tk):
        
        return self.getJasonToken()[tk]