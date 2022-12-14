import os.path

from flask import Blueprint, request, render_template, current_app

from access import login_required, group_required
from db_work import select_dict
from sql_provider import SQLProvider


blueprint_edit = Blueprint('bp_edit', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

@blueprint_edit.route('/', methods=['GET'])
def show_all_products():
    _sql = provider.get('all_products.sql')
    products = select_dict(current_app.config['db_config'], _sql)
    return render_template('all_products.html', products=products)


@blueprint_edit.route('/', methods=['POST'])
def edit_product():
    action = request.form.get('action')
    prod_id = request.form.get('prod_id')
    if action == 'edit_prod':
        _sql = provider.get('one_prod.sql', prod_id = prod_id)
        product = select_dict(current_app.config['db_config'], _sql)[0]
        return render_template('product_update.html', product=product)
    if action == 'del_prod':
        message = del_prod(prod_id)
        return render_template('update_ok.html', message=message)
    if action == 'update_prod':
        message = update_prod(prod_id)
        return render_template('update_ok.html', message=message)


def update_prod(prod_id):
    _sql = provider.get('one_prod.sql', prod_id = prod_id)
    product = select_dict(current_app.config['db_config'], _sql)
    if request.method == 'GET':
        return render_template('product_update.html', product = product)
    else:
        prod_name = request.form.get('prod_name')
        prod_price = request.form.get('prod_price')
        prod_id = request.form.get('prod_id')
        if prod_name:
            _sql = provider.get('update_prod.sql', prod_name=prod_name, prod_price=prod_price, prod_id = prod_id)
            print(_sql)
            return render_template('show_all_products.html')
        else:
            return "Repeat input"


def del_prod(prod_id):
    message = 'Product has been deleted'
    return message


@blueprint_edit.route('/insert_prod', methods=['GET'])
def insert_prod():
    product = {}
    return render_template('product_update.html', product = product)


# @blueprint_edit.route('/insert_prod', methods=['POST'])
# def insert_prod():
#     message = 'Product has been inserted in data base'
#     return render_template('update_ok.html', message = message)