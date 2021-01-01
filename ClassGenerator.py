import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import copy

from Factory import Factory
languageList = Factory.getInstance().getLanguageList()
currentLanguageClass = None

def getAllOptionsToDict(d):
    ret = {}
    for k,v in d.items():
        ret[k] = v.get()
    return ret

def updatePreview():
	global currentLanguageClass
	print(testOptions)
	previewTkString.set(
		os.path.join(pathNameTkString.get(),preFixTkString.get() + classNameTkString.get()+currentLanguageClass.getInstance().getFileExtension())
		+ '\n\n'
        + currentLanguageClass.getInstance().generateClass(classNameTkString.get(), options = getAllOptionsToDict(testOptions))
	)
def execute():
	if(len(classNameTkString.get())<1):
		messagebox.showinfo(title='Invalid name', message='Invalid name')
	else:
		toWrite = currentLanguageClass.getInstance().generateClass(classNameTkString.get(), options = getAllOptionsToDict(testOptions))
		
		f = filedialog.asksaveasfile(filetypes =currentLanguageClass.getInstance().getFileTypes(), initialfile=preFixTkString.get() + classNameTkString.get()+currentLanguageClass.getInstance().getFileExtension(), initialdir = pathNameTkString.get(), mode='w')
		if f is None:
			return
		f.write(toWrite)
		f.close()
		messagebox.showinfo(title='Done', message='Done')
testOptions = {}
def renderOptions(languageId):
    global testOptions
    global currentLanguageClass
    print(languageId)
    currentLanguageClass = Factory.getInstance().getClassInstance(languageList[languageId])
    optionsLabel = ttk.Frame(window)
    for k,v in currentLanguageClass.getInstance().getOptions().items():
        t = v['type']
        label = ttk.Label(optionsLabel, text=k)
        label.pack(side=tk.LEFT)
        if(t=='int'):
            testOptions[k] = tk.IntVar()
            scale = ttk.Scale(optionsLabel, variable = testOptions[k], command=lambda s:testOptions[k].set('%0.0f' % float(s)), from_=v['min'], to=v['max'])
            scale.pack(side=tk.LEFT)
            scaleLabel = ttk.Label(optionsLabel, textvariable = str(testOptions[k]))
            scaleLabel.pack(side=tk.LEFT)
            
        else:
            testOptions[k] = tk.BooleanVar()
            button = ttk.Checkbutton(optionsLabel, variable=testOptions[k], onvalue=True, offvalue=False)
            button.pack(side=tk.LEFT)
        
        
    optionsLabel.grid(row=3, column=0, sticky='WE')

def renderButtons(selected):
    global buttonStyle
    
    languageButtons = ttk.Frame(window)
    for i, val in enumerate(languageList):
        languageButtons.grid_columnconfigure(i,weight=1)
        i = copy.deepcopy(i)
        button = ttk.Button(languageButtons, text=val, command=lambda arg1 = i: renderButtons(arg1))
        button.grid(row=0,column=i, sticky='WE')
        if(selected==i):
            button['state'] = tk.DISABLED
            
            
    languageButtons.grid(row=0, column=0, sticky='WE')
    renderOptions(selected)
        
window = tk.Tk()
window.title("Class Generator")
window.resizable(0,0)
window.minsize(500,600)

classNameTkString = tk.StringVar()
previewTkString = tk.StringVar()
preFixTkString = tk.StringVar()
pathNameTkString = tk.StringVar()
singletonCheckedTkBoolean = tk.BooleanVar()
singletonCheckedTkBoolean.set(False)

labels = ttk.Frame(window)
optionsLabel = ttk.Frame(window)

preFixLabel=ttk.Label(labels, text='Prefix')
preFixEntry = ttk.Entry(labels, textvariable=preFixTkString)

classNameLabel=ttk.Label(labels, text='Class name')
classNameEntry = ttk.Entry(labels, textvariable=classNameTkString)

labels2 = ttk.Frame(window)

pathNameLabel=ttk.Label(labels2, text='Path name')
pathNameEntry = ttk.Entry(labels2, textvariable=pathNameTkString)

renderButtons(0)

submitButton = ttk.Button(window, text='Go', command = execute)
previewButton = ttk.Button(window, text='Preview', command = updatePreview)
previewLabel = ttk.Label(window, textvariable = previewTkString)

preFixLabel.pack(side=tk.LEFT)
preFixEntry.pack(side=tk.LEFT)
classNameLabel.pack(side=tk.LEFT)
classNameEntry.pack(side=tk.LEFT, fill=tk.X, expand=1)

pathNameLabel.pack(side=tk.LEFT)
pathNameEntry.pack(side=tk.LEFT, fill = tk.X, expand=1)

labels.grid(row=1, column=0, sticky='WE')
labels2.grid(row=2, column=0, sticky='WE')
submitButton.grid(row=4, column=0, sticky='WE')
previewButton.grid(row=5, column=0, sticky='WE')
previewLabel.grid(row=6, column=0, sticky='WE')


window.grid_columnconfigure(0, weight=1)
window.mainloop()