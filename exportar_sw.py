# -*- coding: utf-8 -*-
import json
import teamwork
import datetime


# inserir as credenciais
TW_KEY = 'desk380viper'
USER_ID = 155031

instance = teamwork.Teamwork('terras.teamwork.com', TW_KEY)


def read_json(path_sw_file):
    text = open(path_sw_file, 'rt').read()
    data = json.loads(text, encoding='utf8')
    return data

def inserir_hora(project_id, path_sw_file):

    data = read_json(path_sw_file)

    dia = 0
    month = 0
    start_time = datetime.datetime.now()
    almoco = False

    for tarefa in data:
        task = tarefa['Task name']
        datesw = tarefa['Date'].split("/")
        usedtime = tarefa['Used time']


        duration = datetime.timedelta(hours=usedtime)

        if dia != int(datesw[0]) or month != int(datesw[1]):

            #reiniciar para as 09:00
            start_time = datetime.datetime(day=int(datesw[0]), month=int(datesw[1]), year=int(datesw[2]),
                                       hour = 9, minute=0, second=0)

            dia = int(datesw[0])
            month = int(datesw[1])
            almoco = False

        else:
            #adicionar a hora do almoco
            if start_time.hour > 12 and almoco == False:
                start_time = start_time + datetime.timedelta(hours=1)
                almoco = True
            start_time = start_time + duration

        date = datetime.date(day=int(datesw[0]), month=int(datesw[1]), year=int(datesw[2]))

        user_id = USER_ID
        description = task
        instance.save_project_time_entry(project_id, date, duration, user_id, description, start_time)


inserir_hora(221896, "/home/dyeden/ProjetosPython/teamwork_api/swtw/dados_sw/data.json")