# -*- coding: utf-8 -*-
import json
import teamwork
import datetime

class exportarsw(object):

    def __init__(self, pathjson, projectid, apitoken, userid):
        self.pathjson = pathjson
        self.projectid = projectid
        self.userid = userid
        self.instance = teamwork.Teamwork('terras.teamwork.com', apitoken)

    def read_json(self, path_sw_file):
        text = open(path_sw_file, 'rt').read()
        data = json.loads(text, encoding='utf8')
        return data

    def inserir_hora(self, project_id, path_sw_file):

        data = self.read_json(path_sw_file)

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
            description = task
            self.instance.save_project_time_entry(project_id, date, duration, self.userid, description, start_time)

    def run(self):
        self.inserir_hora(self.projectid, self.pathjson)
