import os.path
from flask import Blueprint, request, render_template, current_app, redirect, url_for
from access import login_required, group_required

from db_work import select, call_proc
from sql_provider import SQLProvider

from with_auth.access import *

blueprint_report = Blueprint('bp_report', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

report_list = [{"rep_name": "Отчет о месячной выручке", "rep_id": "1"}, {"rep_name": "Другой отчет", "rep_id": "2"}]
report_url = {'1': {'create_rep':'bp_report.create_rep1', 'view_rep':'bp_report.view_rep1'}, '2': {'create_rep':'pass', 'view_rep':'pass'}}

@blueprint_report.route('/', methods=['GET', 'POST'])
@group_required
def start_report():
    if request.method == 'GET':
        print("GET_start_report")
        return render_template('menu_report.html', report_list = report_list)
    else:
        print("POST_start_report")
        rep_id = request.form.get('rep_id')
        print('rep_id=', rep_id)
        if request.form.get('create_rep'):
            url_rep = report_url[rep_id]['create_rep']

        else:
            url_rep = report_url[rep_id]['view_rep']
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
            res = call_proc(current_app.config['db_config'], 'reported', rep_year, rep_month)
            print('res=', res)
            return render_template('report_created.html')
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
            return render_template('result_rep1.html', schema = schema, result = product_result)
        else:
            return "Repeat input"


