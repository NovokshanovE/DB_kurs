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
    print('cached_select= ', cached_select)
    if request.method == 'GET':
        sql1 = provider.get('waiter_id.sql')
        waiter_id = select_dict(db_config, sql1)
        #waiter_id = select_dict(db_config, sql1)
        print('w_id',waiter_id)
        items = []
        for id_W in waiter_id:
            items.append(id_W['id_W'])
        print(items.sort())
        sql2 = provider.get('table_id.sql')
        table_id = select_dict(db_config, sql2)
        print('t_id', table_id)
        items_T = []
        for id_T in table_id:
            items_T.append(id_T['id_T'])
        items_T.sort()
        print('sort', items_T)
        return render_template('waiter.html',items = items, items_T=items_T )
    else:
        session['waiter_id'] = request.form.get('waiter_id')
        session['tabel_id'] = request.form.get('tabel_id')
        return redirect(url_for('bp_order.order_index'))

@blueprint_order.route('/oreder', methods=['GET', 'POST'])
@group_required
def order_index():
    print("tabel_id = ", session.get('tabel_id'))
    db_config = current_app.config['db_config']
    cache_config = current_app.config['cache_config']
    cached_select = fetch_from_cache('all_items_cached', cache_config)(select_dict)
    print('cached_select=', cached_select)
    if request.method =='GET':
        sql = provider.get('all_items.sql')
        items = cached_select(db_config, sql)
        basket_items = session.get('basket', {})
        print(items)
        return render_template('basket_order_list.html', items = items, basket = basket_items)
    else:
        prod_id = request.form.get('prod_id')
        print(prod_id)
        sql = provider.get('select_item.sql', prod_id = prod_id)
        items = select_dict(db_config, sql) #сделать новый sql который достает только нужные item
        print(items)
        add_to_basket(prod_id, items)

        return redirect(url_for('bp_order.order_index'))


def add_to_basket(prod_id, items: dict):
    print("tabel_id = ", session.get('tabel_id'))
    # item_description = [item for item in items if str(item['prod_id']) == str(prod_id)]
    # print('Item_description before = ', item_description)
    # item_description = item_description[0]
    curr_basket = session.get('basket', {})
    print(session)
    print(-1)
    if prod_id in curr_basket:
        print(-2)
        curr_basket[prod_id]['amount'] = curr_basket[prod_id]['amount']+1
    else:
        print(-3)
       # print(curr_basket[prod_id])
        curr_basket[prod_id] = {
            'name_dishes': items[0]['name_dishes'],
            'price': items[0]['price'],
            'amount': 1
        }
        print(session)
        session['basket'] = curr_basket
        session.permanent = True
    return True


@blueprint_order.route('/save_order', methods = ['GET', 'POSt'])
@group_required
def save_order():
    print("tabel_id = ", session.get('tabel_id'))
    user_id = session.get('user_id')
    #amount = session.get('Order_amount')
    #print(session)

    current_basket = session.get('basket', {})
    #print(current_basket)
    #amount = current_basket[str(user_id)]['amount']
    #print(amount)
    print(0)
    order_id = save_order_with_list(current_app.config['db_config'], user_id, current_basket)
    if order_id:
        if('basket' in session):
            session.pop('basket')

            return render_template('order_created.html',order_id = order_id)
        else:
            return redirect(url_for('menu_choice'))
    else:
        return 'Error...'


def save_order_with_list(dbconfig:dict, user_id: int, current_basket:dict):
    print("tabel_id = ", session.get('tabel_id'))
    with DBConnection(dbconfig) as cursor:
        if cursor is None:
            raise ValueError('Курсор не создан')
        print(1)
        print(session.get('tabel_id'))
        _sql1 = provider.get('insert_order.sql',  table_id = str(session.get('tabel_id')), waiter_id=str(session.get('waiter_id')) )
        print(_sql1)
        result1 = cursor.execute(_sql1)
        print(2)
        if result1 == 1:
            _sql2 = provider.get('select_order_id.sql', user_id = session.get('waiter_id'))
            print(_sql2)
            cursor.execute(_sql2)
            order_id = cursor.fetchall()[0][0]
            print('order_id = ', order_id)
            if order_id:
                for key in current_basket:
                    print('Key:', key, current_basket[key]['amount'])
                    prod_amount = current_basket[key]['amount']
                    _sql3 = provider.get('insert_order_list.sql', order_id=order_id, prod_id=key, prod_amount = prod_amount)
                    print(_sql3)
                    cursor.execute(_sql3)
                print('order_id=', order_id)
                return order_id


@blueprint_order.route('/clear-basket')
@group_required
def clear_basket():
    if 'basket' in session:
        session.pop('basket')
    return redirect(url_for('bp_order.order_index'))
