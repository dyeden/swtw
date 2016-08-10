# -*- coding: utf-8 -*-
import json
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


def read_json(path_sw_file):
    text = codecs.open(path_sw_file, 'rt', encoding='utf-8').read()
    data = json.loads(text, encoding='utf8')

def inserir_hora(project_id, path_sw_file):

    project_id = 221896
    date = datetime.date(2016,8,9)
    duration = datetime.timedelta(hours=1, minutes=10)
    user_id = USER_ID
    description = "testando teamwork"
    start_time = datetime.datetime.now()
    # instance.save_project_time_entry(project_id, date, duration, user_id,description, start_time)

read_json("/home/dyeden/ProjetosPython/teamwork_api/swtw/dados_sw/data.json")