import PySimpleGUI as sg


def criar_janela():
    sg.theme('Deult1')
    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]

    layout = [
        [sg.Frame('Tarefas', layout=linha, key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar'), sg.Text(
            'Total de tarefas: '), sg.Text('0', key='total_tarefas')],
        [sg.Text('Informações adicionais')],
        [sg.Multiline(default_text='', size=(50, 3),
                      font=('Arial', 12), key='informacoes')]
    ]

    return sg.Window('Gerenciador de Tarefas', layout=layout, finalize=True)


janela = criar_janela()
contador = 0

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [
                             [sg.Checkbox(''), sg.Input('')]])
        contador += 1
        janela['total_tarefas'].update(str(contador))
    elif event == 'Resetar':
        janela.close()
        janela = criar_janela()
        contador = 0

janela.close()
