class BaseClass:
    def __init__(self):
        pass
    def seperator(self,space):
        if(isinstance(space, int) and space>self.getTabTrigger()):
            return ' ' * space
        else:
            return '\t'
    def conditionalSpace(self,space,newLine):
        if(not newLine):
            return ''
        else:
            return self.seperator(space)
    def newLine(self, yes):
        if(yes):
            return '\n'
        else:
            return ''
    def getFileName(self, filename):
        return filename + self.getFileExtension()
    def getFileTypes(self):
        return ((self.getFileTypeName(), self.getFileExtension()),)
    def getFileTypeName(self):
        raise NotImplementedError('subclasses must override getFileTypeName()!')
    def getFileExtension(self):
        raise NotImplementedError('subclasses must override getFileExtension()!')
    def getOptions(self):
        raise NotImplementedError('subclasses must override getOptions()!')
    def getTabTrigger(self):
        raise NotImplementedError('subclasses must override getTabTrigger()!')
    def generateClass(self):
        raise NotImplementedError('subclasses must override generateClass()!')
    def recursiveReplace(self, s = '', parameters = {}):
        done = True
        openChar = '{'
        closeChar = '}'
        for key, value in parameters:
            lookFor = openChar + key + closeChar
            if lookFor in s:
                s.replace(lookFor, value)
                done = False
        if(done):
            return s
        self.recursiveReplace(self, s, parameters)