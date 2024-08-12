template ="""
<html>
<head>
    <meta charset="utf-8">
    <title>Main</title>

    <style>
        body{
            text-align:center;
            }
        table{
            width:50%;
            margin: 0 auto;
            border-collapse:collapse;
            }
        th, td{
            border: 1px solid black;
            padding: 10px
        }
        th{
            background-color: #f2f2f2;
        }
        .menu{
            position:fixed;
            top:0;
            left:0;
            width:200px;
            padding:20px;
        }
    </style>
</head>
<body>
    <div class='menu'}
    <ul>
        <li><a href='/'>На главную</a></li>
        <li><a href='#botom'>Добавить запись</a></li>
        %for parent in data['parent']:
            <a href='/?parent={{parent}}'> {{parent}}</a>
        %end
    </ul>
    </div>
    <h1> Table </h1>
        
        <table>
        <tr>
            <td><a href='/?ordering=klgi'> КЛГИ </a></td>
            <td><a href='/?ordering=name'> ИМЯ </a></td>
            <td><a href='/?ordering=amount'> Количество </a></td>
            <td><a href='/?ordering=pictures'>Сделан ли чертеж</a></td>
            <td><a href='/?ordering=parent'>Вхождение</a></td>
        </tr>
        %for row in data['data']:
            <tr>
                <td><a href='item/{{row[5]}}'>{{row[0]}}</a></td>
                <td>{{row[1]}}</td>
                <td>{{row[2]}}</td>
                <td>{{row[3]}}</td>
                <td>{{row[4]}}</td>
            </tr>
        %end
            <tr>
            <form action='/' method='post' accept-charset='utf-8'>
                <td><input name='klgi' type='text'></td>
                <td><input name='name' type='text'></td>
                <td><input name='amount' type='text'></td>
                <td><input name='pictures' type='text'></td>
                <td><input name='parent' type='text'></td>
                <td><button type='submit'> Send </button> </td>
            </form>
            </tr>
        </table>
        <a name='botom'></a>
</body>
</html>

"""

template_klgi ="""
<html>
<head>
    <meta charset="utf-8">
    <title>Main</title>

</head>
<body>
        <h2><a href='/'> На главную </a></h2>
        <form action='/item/{{data['klgi_id']}}' method='post' accept-charset='utf-8'>
            <ul>
                <li>klgi: <input name='klgi' type='text' value={{data['klgi']}}></li>
                <li>name: <input name='name' type='text' value={{data['name']}}></li>
                <li>amount: <input name='amount' type='text' value={{data['amount']}}></li>
                <li>pictures: <input name='pictures' type='text' value={{data['pictures']}}></li>
                <li>parent: <input name='parent' type='text' value={{data['parent']}}></li>
                <li><button type='submit'> Send </button> </li>
            </ul>
        </form>
    <form action='/item/dell/{{data['klgi_id']}}' method='post' accept-charset='utf-8'>
        <p><button type='submit'> Delete </button> </p>
    </form>
</body>
</html>"""

