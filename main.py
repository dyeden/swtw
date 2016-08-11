from exportar_sw import exportarsw

pathjson = "dados_sw/data.json"
projectid = 22222 #pegar no site do teamwork
apitoken = 'aaaaaaaaa' #pegar no site do teamwork
userid = 1111111 #pegar no site do teamwork

e = exportarsw(pathjson, projectid, apitoken, userid)
e.run()


