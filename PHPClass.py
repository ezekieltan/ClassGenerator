from BaseClass import BaseClass
class PHPClass(BaseClass):
    __instance__ = None
    def __init__(self):
        if PHPClass.__instance__ is None:
            PHPClass.__instance__ = self
            super().__init__()
        else:
            pass
    @staticmethod
    def getInstance():
        if not PHPClass.__instance__:
            PHPClass()
        return PHPClass.__instance__
    def generateClass(self, className, options = {}):
        space = options['Space Indent']
        singleton = options['Singleton']
        newLine = options['New line bracket']
        if(singleton):
            return '''<?php
class {className}{n}{{
{t}private static $instance = null;
{t}
{t}private function __construct(){n}{u}{{
{t}{t}
{t}}}
{t}public static function getInstance(){n}{u}{{
{t}{t}if (self::$instance == null){n}{u}{u}{{
{t}{t}{t}self::$instance = new {className}();
{t}{t}}}
{t}{t}return self::$instance;
{t}}}
}}
?>'''.format(className = className, n=self.newLine(newLine), t=self.seperator(space), u = self.conditionalSpace(space, newLine))
        else:
            return '''<?php
class {className}{n}{{
{t}public function __construct(){n}{u}{{
{t}{t}
{t}}}
}}
?>'''.format(className = className, n=self.newLine(newLine), t=self.seperator(space), u = self.conditionalSpace(space, newLine))
    
    def getFileTypeName(self):
        return 'PHP File'
    def getFileExtension(self):
        return '.php'
    def getOptions(self):
        return {'Singleton':{'type':'bool'},'New line bracket':{'type':'bool'}, 'Space Indent':{'type':'int', 'min':-1,'max':8}}
    def getTabTrigger(self):
        return -1