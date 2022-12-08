import json

from flask import Flask, render_template, redirect, session, url_for
from auth.route import blueprint_auth
from blueprint_query.route import blueprint_query
from blueprint_report.route import blueprint_report
from blueprint_edit.route import blueprint_edit
from basket.route import blueprint_order #'''_cache'''

app = Flask(__name__)
app.secret_key = 'SuperKey'

app.register_blueprint(blueprint_auth, url_prefix='/auth')
app.register_blueprint(blueprint_report, url_prefix='/report')
app.register_blueprint(blueprint_query, url_prefix='/zaproses')
app.register_blueprint(blueprint_edit, url_prefix='/edit')
app.register_blueprint(blueprint_order, url_prefix='/order')

app.config['db_config'] = json.load(open('data_files/db_config.json'))
app.config['access_config'] = json.load(open('data_files/access.json'))
#app.config['cache_config'] = json.load(open('data_files/cache.json'))

@app.route('/', methods=['GET', 'POST'])
def menu_choice():
    if 'user_id' in session:
        if session.get('user_group', None):
            return render_template('internal_user_menu.html')
        else:
            return render_template('external_user_menu.html')
    else:
        return redirect(url_for('blueprint_auth.start_auth'))


@app.route('/exit')
def exit_func():
    if 'user_id' in session:
        session.clear()
    return 'Работа в системе завершена'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)

# Чем доступ внутр. отличается от внешних?
# Все внутренние - сотрудники компании
# Доступ регламентируется ролями
# По логину и паролю опредееляется роль
# Для внутреннего важна роль - все права доступа к обработчикам определена роль
# Это концепция внутренних пользователей - через роль
# Внешние пользователи могут достать только те записи, которые относятся к его ID
# Это концепция внешних пользовательей - через ID
