from BaseClass import BaseClass
class JavaScriptClass(BaseClass):
    __instance__ = None
    def __init__(self):
        if JavaScriptClass.__instance__ is None:
            JavaScriptClass.__instance__ = self
            super().__init__()
        else:
            pass
    @staticmethod
    def getInstance():
        if not JavaScriptClass.__instance__:
            JavaScriptClass()
        return JavaScriptClass.__instance__
    def generateClass(self, className, options = {}):
        space = options['Space Indent']
        singleton = options['Singleton']
        newLine = options['New line bracket']
        if(singleton):
            return '''class {className} {n}{{
{t}constructor() {n}{u}{{
{t}{t}if ({className}._instance) {n}{u}{u}{{
{t}{t}{t}return {className}._instance
{t}{t}}}
{t}{t}{className}._instance = this;
{t}
{t}}}
}}'''.format(className = className, n=self.newLine(newLine), t=self.seperator(space), u = self.conditionalSpace(space, newLine))
        else:
            return '''class {className} {n}{{
{t}
{t}constructor() {n}{u}{{
{t}{t}
{t}}}
{t}
}}'''.format(className = className, n=self.newLine(newLine), t=self.seperator(space), u = self.conditionalSpace(space, newLine))
    
    def getFileTypeName(self):
        return 'JavaScript File'
    def getFileExtension(self):
        return '.js'
    def getOptions(self):
        return {'Singleton':{'type':'bool'},'New line bracket':{'type':'bool'}, 'Space Indent':{'type':'int', 'min':-1,'max':8}}
    def getTabTrigger(self):
        return -1