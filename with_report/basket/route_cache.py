import os.path

from flask import Blueprint, request, render_template, current_app, redirect, session, url_for

from access import login_required, group_required
from db_work import select_dict
from sql_provider import SQLProvider
from db_context_manager import DBConnection

from cache.wrapper import fetch_from_cache

blueprint_order = Blueprint('bp_order', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

@blueprint_order.route('/', methods=['GET', 'POST'])
@group_required
def waiter_list():
    db_config = current_app.config['db_config']
    cache_config = current_app.config['cache_config']
    cached_select = fetch_from_cache('all_items_cached', cache_config)(select_dict)
    if request.method == 'GET':
        sql1 = provider.get('waiter_id.sql')
        waiter_id = select_dict(db_config, sql1)
        print(waiter_id)
        items = []
        for id_W in waiter_id:
            items.append(id_W['id_W'])
        print(items.sort())
        sql2 = provider.get('table_id.sql')
        table_id = select_dict(db_config, sql2)
        print(table_id)
        items_T = []
        for id_T in table_id:
            items_T.append(id_T['id_T'])
        print(items_T.sort())
        return render_template('waiter.html',items = items, items_T=items_T )
    else:
        session['waiter_id'] = request.form.get('waiter_id')
        session['tabel_id'] = request.form.get('tabel_id')
        return redirect(url_for('bp_order.order_index'))

@blueprint_order.route('/', methods=['GET', 'POST'])
@group_required
def order_index():

    db_config = current_app.config['db_config']
    cache_config = current_app.config['cache_config']
    cached_select = fetch_from_cache('all_items_cached', cache_config)(select_dict)
    print('cached_select=', cached_select)
    if request.method == 'GET':
        sql = provider.get('all_items.sql')
        # items = select_dict(db_config, sql)
        items = cached_select(db_config, sql)
        basket_items = session.get('basket', {})
        return render_template('basket_order_list.html', items=items, basket=basket_items)
    else:
        prod_id = request.form.get('prod_id')
        sql = provider.get('select_item.sql', prod_id=prod_id)
        items = select_dict(db_config, sql)  # сделать новый sql который достает только нужные item

        add_to_basket(prod_id, items)

        return redirect(url_for('bp_order.order_index'))


def add_to_basket(prod_id, items: dict):
    # item_description = [item for item in items if str(item['prod_id']) == str(prod_id)]
    # print('Item_description before = ', item_description)
    # item_description = item_description[0]
    curr_basket = session.get('basket', {})
    if prod_id in curr_basket:
        curr_basket[prod_id]['amount'] = curr_basket[prod_id]['amount'] + 1
    else:
        curr_basket[prod_id] = {
            'prod_name': items[0]['prod_name'],
            'prod_price': items[0]['prod_price'],
            'amount': 1
        }
        session['basket'] = curr_basket
        session.permanent = True
    return True


@blueprint_order.route('/save_order', methods=['GET', 'POSt'])
@group_required
def save_order():
    user_id = session.get('user_id')

    current_basket = session.get('basket', {})
    print(0)
    order_id = save_order_with_list(current_app.config['db_config'], user_id, current_basket)
    if order_id:
        session.pop('basket')
        return render_template('order_created.html', order_id=order_id)
    else:
        return 'Error...'


def save_order_with_list(dbconfig: dict, user_id: int, current_basket: dict):
    with DBConnection(dbconfig) as cursor:
        if cursor is None:
            raise ValueError('Курсор не создан')
        print(1)
        _sql1 = provider.get('insert_order.sql',  table_id = str(session.get('tabel_id')), waiter_id=str(session.get('waiter_id')) )
        result1 = cursor.execute(_sql1)
        print(2)
        if result1 == 1:
            _sql2 = provider.get('select_order_id.sql', user_id = session.get('waiter_id'))
            cursor.execute(_sql2)
            order_id = cursor.fetchall()[0][0]
            print('order_id = ', order_id)
            if order_id:
                for key in current_basket:
                    print(key, current_basket[key]['amount'])
                    prod_amount = current_basket[key]['amount']
                    _sql3 = provider.get('insert_order_list.sql', order_id=order_id, prod_id=key,
                                         prod_amount=prod_amount)
                    cursor.execute(_sql3)
                return order_id


@blueprint_order.route('/clear-basket')
@group_required
def clear_basket():
    if 'basket' in session:
        session.pop('basket')
    return redirect(url_for('bp_order.order_index'))
