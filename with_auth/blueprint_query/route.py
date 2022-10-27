import os
from flask import Blueprint, request, render_template, current_app
from db_work import select
from sql_provider import SQLProvider

from with_auth.access import *

blueprint_query = Blueprint('bp_query', __name__, template_folder='templates')

provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_query.route('/queries', methods=['GET', 'POST'])
def queries():
    if request.method == 'GET':
        return render_template('product_form.html')
    else:
        input_product = request.form.get('product_name')
        if input_product:
            _sql = provider.get('product.sql', input_product=input_product)
            product_result, schema = select(current_app.config['db_config'], _sql)
            print(product_result, schema)
            return render_template('db_result.html', schema=schema, result=product_result )
        else:
            return "Repeat input"



@blueprint_query.route('/querie', methods=['GET', 'POST'])
@group_required
def querie():
    #if(session.get('user_group', None)):
    #    return "Repeat input"
    #else:
    return render_template('queries_menu.html')

@blueprint_query.route('/queries1', methods=['GET', 'POST'])
def queries1():
    if request.method == 'GET':
        return render_template('queries1.html')
    else:
        input_product = request.form.get('product_name')
        print(input_product)
        if input_product:
            _sql = provider.get('queries1.sql', input_product=input_product)
            product_result, schema = select(current_app.config['db_config'], _sql)
            print(product_result, schema)
            return render_template('db_result.html', schema=['id', 'Название', 'Цена'], result=product_result)
        else:
            return "Repeat input"


@blueprint_query.route('/queries2', methods=['GET', 'POST'])
def queries2():
    if request.method == 'GET':
        return render_template('queries2.html')
    else:
        input_data = request.form.get('input_data')
        print(input_data)
        if input_data:
            _sql = provider.get('queries2.sql', input_data=input_data)
            product_result, schema = select(current_app.config['db_config'], _sql)
            return render_template('db_result.html', schema=[f'Сумма заказов месяц:{input_data}'], result=product_result)
        else:
            return "Repeat input"


@blueprint_query.route('/queries3', methods=['GET', 'POST'])
def queries3():
    if request.method == 'GET':
        return render_template('queries3.html')
    else:
        input_data = request.form.get('input_data')
        if input_data:
            _sql = provider.get('queries3.sql', input_data=input_data)
            product_result, schema = select(current_app.config['db_config'], _sql)
            return render_template('db_result.html', schema=['id', 'Паспортные данные', 'Устроился', "Уволился","Зарплата","День рождения", "Имя", "Фамилия"], result=product_result)
        else:
            return "Repeat input"