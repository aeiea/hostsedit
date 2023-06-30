import PySimpleGUI as sg
import webbrowser, elevate
elevate.elevate()
hosts_path = 'c:/Windows/System32/drivers/etc/hosts'
# hosts_path = './hosts.sample'
hosts = open(hosts_path)
hosts_data: list[list[str]] = []
sg.theme('SystemDefaultForReal')
def read_hosts() -> None:
    for i in hosts.readlines():
        if not ('#' in i) and not (i.split() in hosts_data) and not (i.split() == []):
            hosts_data.append(i.split())
def change_entry(index) -> None:
    sg.theme('SystemDefaultForReal')
    layout = [
        [sg.Text('IP: '), sg.Input(hosts_data[index][0])],
        [sg.Text('Hostnames(comma separated): '), sg.Input(', '.join([hosts_data[index][i] for i in range(1, len(hosts_data[index]))]))],
        [sg.Button('Done')]
    ]
    popup = sg.Window('Edit HOSTS entry', layout = layout, icon='icon.ico')
    while True:
        event, values = popup.read()
        if event == sg.WIN_CLOSED:
            popup.close()
            break
        if event == 'Done':
            print([values[0]] + [i.strip() for i in values[1].split(',')])
            hosts_data[index] = [values[0]] + [i.strip() for i in values[1].split(',')]
            popup.close()
            break

def convert_to_table(d: list[list[str]]) -> list[list[str]]:
    nl = [['']]*len(d)
    for i, v in enumerate(d):
        nl[i] = [v[0], ', '.join([v[s] for s in range(1, len(v))])]
    return nl
def apply_changes() -> None:
    hosts_file = open(hosts_path, 'w')
    hosts_file.truncate(0)
    for i in hosts_data:
        hosts_file.write(' '.join(i) + '\n')
    hosts_file.close()
read_hosts()
layout = [
    [sg.Text('HostsEdit v0.0.1 - The incredibly scuffed HOSTS editor')],
    [sg.Table(convert_to_table(hosts_data), ['IP','Hostnames'], num_rows=20, key='table', enable_click_events=True, col_widths=5)],
    [sg.Button('New Entry'), sg.Button('Edit Entry'), sg.Button('Delete Entry')],
    [sg.Text('Licensed under AGPLv3+ | star the ', pad=((0, 0), (0,0))), sg.Text('project', tooltip='https://github.com/aeiea/hostsedit', key='project_url', font=('', 10, 'underline'), enable_events=True, pad=((0, 0), (0,0))), sg.Text(' on github!', pad=((0, 0), (0,0)))],
    [sg.Button('Save'), sg.Button('Exit')]
]
window = sg.Window('HostEdit v0.0.1', layout, icon='icon.ico')
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Save':
        apply_changes()
        break
    if event == 'New Entry':
        hosts_data.append(['127.0.0.1', 'localhost'])
        change_entry(len(hosts_data) - 1)
        window['table'].update(values = hosts_data)
    if event == 'Edit Entry':
        if values['table'] == []:
            sg.popup('Please select a row', title='Invalid Selection')     
        else:
            change_entry(values['table'][0])
            window['table'].update(values = hosts_data)
    if event == 'Delete Entry':
        if values['table'] == []:
            sg.popup('Please select a row', title='Invalid Selection')     
        else:
            if sg.popup_ok_cancel('Cannot undo deletion: Continue?') == 'OK':
                del hosts_data[values['table'][0]]
                window['table'].update(values = hosts_data)
    if event == 'project_url':
        webbrowser.open('https://github.com/aeiea/hostsedit')