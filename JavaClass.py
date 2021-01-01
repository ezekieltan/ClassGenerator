from BaseClass import BaseClass
class JavaClass(BaseClass):
    __instance__ = None
    def __init__(self):
        if JavaClass.__instance__ is None:
            JavaClass.__instance__ = self
            super().__init__()
        else:
            pass
    @staticmethod
    def getInstance():
        if not JavaClass.__instance__:
            JavaClass()
        return JavaClass.__instance__
    def generateClass(self, className, options = {}):
        space = options['Space Indent']
        singleton = options['Singleton']
        newLine = options['New line bracket']
        if(singleton):
            return '''public class {className} {n}{{
{t}private static {className} instance = null; 
{t}
{t}private {className}() {n}{u}{{
{t}{t}
{t}}}
{t}
{t}public static {className} getInstance() {n}{u}{{
{t}{t}if (instance == null) {n}{u}{u}{{
{t}{t}{t}instance = new {className}(); 
{t}{t}}}
{t}{t}return instance; 
{t}}}
}}'''.format(className = className, n=self.newLine(newLine), t=self.seperator(space), u = self.conditionalSpace(space, newLine))
        else:
            return '''public class {className} {n}{{
{t}
{t}public {className}() {n}{u}{{
{t}{t}
{t}}}
{t}
}}'''.format(className = className, n=self.newLine(newLine), t=self.seperator(space), u = self.conditionalSpace(space, newLine))
    
    def getFileTypeName(self):
        return 'Java File'
    def getFileExtension(self):
        return '.java'
    def getOptions(self):
        return {'Singleton':{'type':'bool'},'New line bracket':{'type':'bool'}, 'Space Indent':{'type':'int', 'min':-1,'max':8}}
    def getTabTrigger(self):
        return -1