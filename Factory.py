from PythonClass import PythonClass
from PHPClass import PHPClass
from JavaClass import JavaClass
from JavaScriptClass import JavaScriptClass
from ReactClass import ReactClass
from DashClass import DashClass
class Factory:
    __instance__ = None
    def __init__(self):
        if Factory.__instance__ is None:
            Factory.__instance__ = self
        else:
            pass
    @staticmethod
    def getInstance():
        if not Factory.__instance__:
            Factory()
        return Factory.__instance__
    def getLanguageList(self):
        return ['Python', 'PHP', 'Java', 'JavaScript', 'React', 'Dash']
    def getClassInstance(self, language):
        if (language=='Python'):
            return PythonClass.getInstance()
        elif (language=='PHP'):
            return PHPClass.getInstance()
        elif (language=='Java'):
            return JavaClass.getInstance()
        elif (language=='JavaScript'):
            return JavaScriptClass.getInstance()
        elif (language=='React'):
            return ReactClass.getInstance()
        elif (language=='Dash'):
            return DashClass.getInstance()