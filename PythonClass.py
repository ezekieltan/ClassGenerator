from BaseClass import BaseClass
class PythonClass(BaseClass):
    __instance__ = None
    def __init__(self):
        if PythonClass.__instance__ is None:
            PythonClass.__instance__ = self
            super().__init__()
        else:
            pass
    @staticmethod
    def getInstance():
        if not PythonClass.__instance__:
            PythonClass()
        return PythonClass.__instance__
    
    def generateClass(self, className, options = {}):
        space = options['Space Indent']
        singleton = options['Singleton']
        if(singleton):
            return '''class {className}:
{t}__instance__ = None
{t}def __init__(self):
{t}{t}if {className}.__instance__ is None:
{t}{t}{t}{className}.__instance__ = self
{t}{t}else:
{t}{t}{t}pass
{t}@staticmethod
{t}def getInstance():
{t}{t}if not {className}.__instance__:
{t}{t}{t}{className}()
{t}{t}return {className}.__instance__
{t}'''.format(className = className, t=self.seperator(space))   
        else:
            return '''class {className}:
{t}def __init__(self):
{t}{t}pass
{t}'''.format(className = className, t=self.seperator(space))
    
    def getFileTypeName(self):
        return 'Python File'
    def getFileExtension(self):
        return '.py'
    def getOptions(self):
        return {'Singleton':{'type':'bool'}, 'Space Indent':{'type':'int', 'min':0,'max':8}}
    def getTabTrigger(self):
        return 0