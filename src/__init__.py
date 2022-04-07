import json
from flask import Flask,request
from flaskext.mysql import MySQL


app = Flask(__name__)
app.config['MYSQL_DATABASE_USER']='admin'
app.config['MYSQL_DATABASE_PASSWORD']='1234'
app.config['MYSQL_DATABASE_DB']='torneo'
app.config['SECRET_KEY']='secretkey'
mysql = MySQL()
mysql.init_app(app)

#cursor.execute(
#    '''
#    ''',("",0)
#)
#Le_pasas_una_tupla_para_guardar_info_para_insertar_%s=string_%d_pa_numeros

#si vamos a hacer un select
#cursor.fetchall()
#Cuando insert o update
#mysql.get_db().commit()

@app.get('/')
def hola():
    print(mysql.get_db().cursor())
    return 'Hola como estas'

@app.get('/equipos')
def index():
    cursor = mysql.get_db().cursor()
    
    cursor.execute(
        '''
        SELECT `nombre` FROM `equipo`
        '''
    )
    users=cursor.fetchall()
    users_json=json.dumps(users)
    users_str="Los equipos en la liga son: "+str(users_json).replace("[","").replace("]","").replace('"','')
    return users_str

@app.get('/partidosHoy')
def partidosDEF():
    cursor = mysql.get_db().cursor()
    
    cursor.execute(
        '''
        
        '''
    )
    partidos=cursor.fetchall()
    partidos_json=json.dumps(partidos)
    partidos_str="Los partidos para el día de hoy son: "+str(partidos_json).replace("[","").replace("]","").replace('"','')
    return partidos_str

@app.post('/agrPartido')
def addPart():
    json_request = request.get_json()
    cursor = mysql.get_db().cursor()
    cursor.execute(
    '''
    INSERT INTO `partidos` (`fecha`)
    VALUES ('{fecha}')
    '''.format(
        fecha=json_request["fecha"]
    ))
    mysql.get_db().commit()
    cursor.execute(
        '''
        SELECT MAX(codigo) FROM `partidos`
        '''
    )
    ultid=cursor.fetchall()
    ultid_json=json.dumps(ultid)
    ultid_str="Partido insertado correctamente, tu id es: "+str(ultid_json).replace("[","").replace("]","").replace('"','')
    return ultid_str