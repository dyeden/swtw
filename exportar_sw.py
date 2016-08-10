# -*- coding: utf-8 -*-
import teamwork
import unicodecsv
import codecs
import datetime
import csv
from cStringIO import StringIO
# inserir as credenciais
TW_KEY = 'fdafdafa'
USER_ID = 84684684
#
# instance = teamwork.Teamwork('terras.teamwork.com', TW_KEY)
teste = """"date","Person","Used time","Description","Item id","Item name","Task id","Task name","Link"
"1/8/2016","Dyeden Monteiro","4","","1756","T: BigData: elaborar proposta de frontend - Part 3","6344","Inserção do serviço na AWS","https://www.scrumwise.com/scrum/#/time-entry/id-60727-4278-1"
"1/8/2016","Dyeden Monteiro","3","","1756","T: BigData: elaborar proposta de frontend - Part 3","6345","Pesquisa: Como ler dados raster de forma paralela - Part 1","https://www.scrumwise.com/scrum/#/time-entry/id-60727-4278-5"
"4/8/2016","Dyeden Monteiro","3","","1756","T: BigData: elaborar proposta de frontend - Part 3","6494","Pesquisa sensores e obtenção dos dados  raster  (Resource-sat, sentinel, modis ...) Part1","https://www.scrumwise.com/scrum/#/time-entry/id-60727-4314-12"
"4/8/2016","Dyeden Monteiro","4","","1756","T: BigData: elaborar proposta de frontend - Part 3","6493","Pesquisa sensores e obtenção dos dados  raster  (Resource-sat, sentinel, modis ...) Part2","https://www.scrumwise.com/scrum/#/time-entry/id-60727-4314-15"
"5/8/2016","Dyeden Monteiro","1","","1756","T: BigData: elaborar proposta de frontend - Part 3","6495","Reunião Carlos","https://www.scrumwise.com/scrum/#/time-entry/id-60727-4314-25"
"""

def read_csv(path_sw_file):
    # text = open(path_sw_file, "r", )
    text = codecs.open(path_sw_file, 'rt', encoding='utf-8')
    # print text
    f = StringIO(teste)
    # print f.readlines()
    reader = unicodecsv.reader(text,delimiter=",", encoding='utf-8')
    row = reader.next()
    print row
    row = reader.next()
    print row
    row = reader.next()
    print row


    # with open(path_sw_file) as csvfile:
    #     # reader = csv.DictReader(text, delimiter=",")
    #     reader = unicodecsv.reader(text, encoding='utf-8')
    #     for row in reader:
    #         print row
    #         # print(row["Date"], row["Person"])

def inserir_hora(project_id, path_sw_file):
    # project_id: Project ID
    # date: datetime.date Date of time entry
    # duration: datetime.timedelta Duration
    # user_id: Integer Id of person
    # description: String Id of person
    # start_time: datetime.timedelta

    project_id = 221896
    date = datetime.date(2016,8,9)
    duration = datetime.timedelta(hours=1, minutes=10)
    user_id = USER_ID
    description = "testando teamwork"
    start_time = datetime.datetime.now()
    instance.save_project_time_entry(project_id, date, duration, user_id,description, start_time)

read_csv("./dados_sw/Scrumwise Time Log 2016-08-09_teste.csv")