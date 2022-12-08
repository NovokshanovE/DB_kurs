import os.path
import json
from flask import Blueprint, request, render_template, current_app, redirect, url_for
from access import login_required, group_required

from db_work import select, call_proc
from sql_provider import SQLProvider

from with_auth.access import *

blueprint_report = Blueprint('bp_report', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))
report_list = json.load(open('data_files/report_list.json', encoding='utf-8'))
report_url = json.load(open('data_files/report_url.json', encoding='utf-8'))
print(report_list)
#report_list[0]["rep_name"] = "Отчет о продажах за месяц"
#report_list[1]["rep_name"] = "Другой отчет"
@blueprint_report.route('/', methods=['GET', 'POST'])
@group_required
def start_report():
    if request.method == 'GET':
        print("GET_start_report")

        if('message' in session):
            message = session.get('message')
            session.pop('message')
            return render_template('menu_report.html', report_list = report_list, message = message)
        else:
            return render_template('menu_report.html', report_list=report_list)
    else:
        print("POST_start_report")
        rep_id = request.form.get('rep_id')
        print('rep_id=', rep_id)
        if request.form.get('create_rep'):
            url_rep = report_url[rep_id]['create_rep']

        elif request.form.get('view_rep'):
            url_rep = report_url[rep_id]['view_rep']
        elif request.form.get('update_rep'):
            url_rep = report_url[rep_id]['update_rep']
        print('url_rep=', url_rep)
        return redirect(url_for(url_rep))

@blueprint_report.route('/create_rep1', methods=['GET', 'POST'])
@group_required
def create_rep1():
    if request.method == 'GET':
        print("GET_create")
        return render_template('report_create.html')
    else:
        print("POST_create")
        rep_month = request.form.get('input_month')
        rep_year = request.form.get('input_year')
        print("Loading...")
        if rep_year and rep_month:
            _sql = provider.get('check_rep.sql', in_month=rep_month, in_year=rep_year)

            check = select(current_app.config['db_config'], _sql)[0][0][0]
            print(check)
            if(check == 0):
                res = call_proc(current_app.config['db_config'], 'reported', rep_year, rep_month)
                print('res=', res)
                return render_template('report_created.html')
            else:
                session['message'] = 'Отчет уже создан'
                return redirect(url_for('bp_report.start_report'))

        else:
            return "Repeat input"

@blueprint_report.route('/update_rep1', methods=['GET', 'POST'])
@group_required
def update_rep1():
    if request.method == 'GET':
        print("GET_create")
        return render_template('report_create.html')
    else:
        print("POST_create")
        rep_month = request.form.get('input_month')
        rep_year = request.form.get('input_year')
        print("Loading...")
        if rep_year and rep_month:
            _sql = provider.get('check_rep.sql', in_month=rep_month, in_year=rep_year)

            check = select(current_app.config['db_config'], _sql)[0][0][0]
            print(check)
            if (check != 0):
                res = call_proc(current_app.config['db_config'], 'report_update', rep_year, rep_month)
                print('res=', res)
                return render_template('report_updated.html')
            else:
                session['message'] = 'Отчет еще не создан'
                return redirect(url_for('bp_report.start_report'))


        else:
            return "Repeat input"
@blueprint_report.route('/view_rep1', methods=['GET', 'POST'])
@group_required
def view_rep1():
    if request.method == 'GET':
        return render_template('view_rep.html')
    else:
        rep_month = request.form.get('input_month')
        rep_year = request.form.get('input_year')
        print(rep_year, rep_month)
        if rep_year and rep_month:
            _sql = provider.get('rep1.sql', in_year=rep_year, in_month = rep_month)
            product_result, schema = select(current_app.config['db_config'], _sql)
            return render_template('result_rep1.html', schema = ['Блюдо', 'Количество','Заработок с этого блюда за месяц'], result = product_result,
                                   date = str(rep_year)+ '-' + str(rep_month))
        else:
            return "Repeat input"


@blueprint_report.route('/create_rep2', methods=['GET', 'POST'])
@group_required
def create_rep2():
    if request.method == 'GET':
        print("GET_create")
        return render_template('report_create.html')
    else:
        print("POST_create")
        rep_month = request.form.get('input_month')
        rep_year = request.form.get('input_year')
        print("Loading...")
        if rep_year and rep_month:
            _sql = provider.get('check_rep2.sql', in_month=rep_month, in_year=rep_year)

            check = select(current_app.config['db_config'], _sql)[0][0][0]
            print(check)
            if(check == 0):
                res = call_proc(current_app.config['db_config'], 'report_waiter', rep_year, rep_month)
                print('res=', res)
                return render_template('report_created.html')
            else:
                session['message'] = 'Отчет уже создан'
                return redirect(url_for('bp_report.start_report'))

        else:
            return "Repeat input"

@blueprint_report.route('/update_rep2', methods=['GET', 'POST'])
@group_required
def update_rep2():
    if request.method == 'GET':
        print("GET_create")
        return render_template('report_create.html')
    else:
        print("POST_create")
        rep_month = request.form.get('input_month')
        rep_year = request.form.get('input_year')
        print("Loading...")
        if rep_year and rep_month:
            _sql = provider.get('check_rep2.sql', in_month=rep_month, in_year=rep_year)

            check = select(current_app.config['db_config'], _sql)[0][0][0]
            print(check)
            if (check != 0):
                res = call_proc(current_app.config['db_config'], 'report_waiter_update', rep_year, rep_month)
                print('res=', res)
                return render_template('report_updated.html')
            else:
                session['message'] = 'Отчет еще не создан'
                return redirect(url_for('bp_report.start_report'))


        else:
            return "Repeat input"
@blueprint_report.route('/view_rep2', methods=['GET', 'POST'])
@group_required
def view_rep2():
    if request.method == 'GET':
        return render_template('view_rep.html')
    else:
        rep_month = request.form.get('input_month')
        rep_year = request.form.get('input_year')
        print(rep_year, rep_month)
        if rep_year and rep_month:
            _sql = provider.get('rep2.sql', in_year=rep_year, in_month = rep_month)
            product_result, schema = select(current_app.config['db_config'], _sql)
            print(schema)
            return render_template('result_rep1.html', schema = ['Имя', 'Фамилия', 'Сделано заказов на сумму'], result = product_result,
                                   date = str(rep_year) + '-' + str(rep_month))
        else:
            return "Repeat input"
