from BaseClass import BaseClass
class ReactClass(BaseClass):
    __instance__ = None
    def __init__(self):
        if ReactClass.__instance__ is None:
            ReactClass.__instance__ = self
            super().__init__()
        else:
            pass
    @staticmethod
    def getInstance():
        if not ReactClass.__instance__:
            ReactClass()
        return ReactClass.__instance__
    def generateClass(self, className, options = {}):
        space = options['Space Indent']
        newLine = options['New line bracket']
        constructor = options['Constructor']
        if(constructor):
            constructorString = '''
{t}constructor() {n}{u}{{
{t}{t}super();
{t}}}
'''.format(className = className, n=self.newLine(newLine), t=self.seperator(space), u = self.conditionalSpace(space, newLine))
        else:
            constructorString = ''
        return '''import React from 'react';
export default class {className} extends React.Component {{
{constructorString}
{t}state = {n}{u}{{
{t}{t}
{t}}}

{t}render() {n}{u}{{
{t}{t}return(
{t}{t}{t}<div>
{t}{t}{t}   
{t}{t}{t}</div>
{t}{t});
{t}}}
}}'''.format(constructorString = constructorString, className = className, n=self.newLine(newLine), t=self.seperator(space), u = self.conditionalSpace(space, newLine))
    def getFileTypeName(self):
        return 'React File'
    def getFileExtension(self):
        return '.jsx'
    def getOptions(self):
        return {'New line bracket':{'type':'bool'},'Constructor':{'type':'bool'}, 'Space Indent':{'type':'int', 'min':-1,'max':8}}
    def getTabTrigger(self):
        return -1