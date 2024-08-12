from bottle import Bottle, template, run, route, request, redirect, patch
from template import template as t
from template import template_klgi
import sqlite3

conn = sqlite3.connect('BVdb.db')
cur = conn.cursor()

def go_main():
    return redirect('/')
def tags():
    cur.execute("""SELECT DISTINCT(parent)  FROM BV ORDER BY parent""")
    parent = list(map(lambda a: a[0], cur.fetchall()))
    return parent

@route('/')
def index():
    if request.query.ordering:
        ordering = request.query.ordering
    else:
        ordering ='klgi'
    if request.query.parent:
        parent = request.query.parent
        print(parent)
        cur.execute(f"""SELECT klgi, name, amount,
        CASE WHEN pictures = 1 THEN "Сделан" ELSE "Нету" END AS new_pic, parent, id
        FROM BV
        WHERE parent = '{parent}'
        ORDER BY {ordering}""")
    else:
        cur.execute(f"""SELECT klgi, name, amount,
CASE WHEN pictures = 1 THEN "Сделан" ELSE "Нету" END AS new_pic, parent, id
FROM BV
ORDER BY {ordering}""")
    data = cur.fetchall()
    data = {'data':data, 'parent': tags()}
    return template(t, data=data)

@route('/', method='POST')
def add_klgi():
    klgi = request.forms.getunicode('klgi')
    name = request.forms.getunicode('name')
    amount = request.forms.getunicode('amount')
    pictures = request.forms.getunicode('pictures')
    parent = request.forms.getunicode('parent')
    if klgi:
        cur.execute(f"""INSERT INTO BV(klgi, name, amount, pictures, parent)
                    VALUES ('{klgi}', '{name}', {amount}, {pictures}, '{parent}')""")
        conn.commit()
        go_main()
        


@route('/item/<klgi_id>')
def item(klgi_id=''):
    cur.execute(f"""SELECT klgi, name, amount, pictures, parent, id
FROM BV
WHERE id={klgi_id}""")
    filds_names = ('klgi', 'name', 'amount', 'pictures', 'parent', 'klgi_id')
    data = dict(zip(filds_names, cur.fetchone()))
    print(data)
    return template(template_klgi, data=data)


@route('/item/<klgi_id>', method='POST')
def update_item(klgi_id=''):
    print(klgi_id)
    klgi = request.forms.getunicode('klgi')
    name = request.forms.getunicode('name')
    amount = request.forms.getunicode('amount')
    pictures = request.forms.getunicode('pictures')
    parent = request.forms.getunicode('parent')
    print(klgi, name, amount, pictures, parent)
    cur.execute(f"""UPDATE BV SET klgi='{klgi}',
name='{name}',
amount= '{amount}',
pictures='{pictures}',
parent='{parent}'
WHERE id='{klgi_id}';""")
    conn.commit()
    print('Успешно')
    go_main()

@route('/item/dell/<klgi_id>', method='POST')
def dell_item(klgi_id=''):
    print('функция работает')
    cur.execute(f"""DELETE FROM BV WHERE id ={klgi_id}""")
    go_main()

    
run(host='localhost', port=8080)

