from BaseClass import BaseClass
class DashClass(BaseClass):
    __instance__ = None
    def __init__(self):
        if DashClass.__instance__ is None:
            DashClass.__instance__ = self
            super().__init__()
        else:
            pass
    @staticmethod
    def getInstance():
        if not DashClass.__instance__:
            DashClass()
        return DashClass.__instance__
    
    def generateClass(self, className, options = {}):
        space = options['Space Indent']
        return '''import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = []
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.title = \''''+className+'''\'
app.layout = html.Div(
{t}children=[
{t}{t}
{t}]
)


if __name__ == '__main__':
{t}app.run_server(debug=True)'''.format(className = className, t=self.seperator(space))
    def getFileTypeName(self):
        return 'Python File'
    def getFileExtension(self):
        return '.py'
    def getOptions(self):
        return {'Space Indent':{'type':'int', 'min':0,'max':8}}
    def getTabTrigger(self):
        return 0