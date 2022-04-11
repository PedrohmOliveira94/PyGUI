from re import match

import PySimpleGUI as sg

layout = [
    [sg.Text('0 km/h', key='-SPEED-')],
    [sg.Input(key='-INPUT-'), sg.Spin(['km/h', 'miles/h'], key='-METRIC-'), sg.Button('Convert', key='-BUTTON1-')]
]
window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON1-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            if values['-METRIC-'] == 'km/h':
                output = int(input_value)*0.6214
                window['-SPEED-'].update(str(output) + ' Miles/h')
            else:
                output = int(input_value) / 0.6214
                window['-SPEED-'].update(str(output) + ' KM/h')


window.close()