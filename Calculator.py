#Importing library for making GUI
import PySimpleGUI as psg

#Applying theme to GUI
psg.theme('DarkGrey14')

#Making GUI
column_1=[
    [psg.Button('7',size=(4,2)),psg.Button('8',size=(4,2)),psg.Button('9',size=(4,2))],
    [psg.Button('4',size=(4,2)),psg.Button('5',size=(4,2)),psg.Button('6',size=(4,2))],
    [psg.Button('1',size=(4,2)),psg.Button('2' , size=(4,2)),psg.Button('3',size=(4,2))],
    [psg.Button('**',size=(4,2),key="-Power-"),psg.Button('0',size=(4,2)),psg.Button('.',size=(4,2),key="-Decimal-")]
    ]

column_2=[
    [psg.Button('x',size=(4,2),key="-Multiply-")],
    [psg.Button("-",size=(4,2),key="-Minus-")],
    [psg.Button("+",size=(4,5),key="-Plus-")]
]

column_3=[
    [psg.Button("/",size=(4,2),key="-Division-")],
    [psg.Button("%",size=(4,2),key="-Modulus-")],
    [psg.Button("CE",size=(4,2),key="-Cancel-")],
    [psg.Button("=",size=(4,2),key="-Equal-")]
]
layout =[
    [psg.I(font=(None,30),size=(13,2),key="-INPUT-")] , 
    [psg.Column(column_1),psg.VerticalSeparator(),psg.Column(column_2),psg.Column(column_3)]
]

#Assigning work to different buttons
window = psg.Window("Calculator",layout)
l=[str(i) for i in range(10)]
history=''
operator = ["-Modulus-","-Division-","-Plus-","-Power-","-Minus-","-Multiply-"]
while True:
    events,values = window.read()
    print(events,values)                                                         #Command to show GUI
    
    if events == psg.WIN_CLOSED:
        window.close()                                                           #Command to close GUI using cross button
        break
    
    elif events in l:
        history+=events
        window["-INPUT-"].update(history)                                        #Command to show input given by user 
    
    elif events == "-Decimal-":
        history+="."
        window["-INPUT-"].update(history)                                        #Command to use decimals
    
    elif events == "-Cancel-":
        history=history[0:len(history)-1]
        window["-INPUT-"].update(history)                                        #Command to Delete previous input
    
    elif events in operator:
        operation=events
        num_1 = float(history)                                                   #Command for using different operator
        history =''
    
    elif events == "-Equal-":
        num_2 = float(history)                                                   #Command for calculating appropriate result
    
        if operation=="-Division-":
            result=num_1/num_2
    
        elif operation=="-Plus-":
            result=num_1+num_2
    
        elif operation=="-Minus-":
            result=num_1-num_2
    
        elif operation=="-Multiply-":
            result=num_1*num_2
    
        elif operation=="-Modulus-":
            result=num_1%num_2
    
        elif operation=="-Power-":
            result=num_1**num_2
    
        window["-INPUT-"].update(float(result))                                    #Command for showing results