import PySimpleGUI as sg

# criando layout


def criar_janela_inicial():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas', layout=linha, key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]

    return sg.Window('TO DO list', layout=layout, finalize=True)


# criar janela
janela = criar_janela_inicial()

# regras da janela
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [
                             [sg.Checkbox(''), sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela_inicial()
