import json

from flask import Flask, render_template, session, redirect, url_for
from auth.route import blueprint_auth
from blueprint_query.route import blueprint_query
from blueprint_report.route import blueprint_report
from blueprint_edit.route import blueprint_edit
from basket.route_cache import blueprint_order
from access import login_required


app = Flask(__name__)
app.secret_key = 'SuperKey'


app.register_blueprint(blueprint_auth, url_prefix='/auth')
app.register_blueprint(blueprint_query, url_prefix='/zaproses')
app.register_blueprint(blueprint_report, url_prefix='/report')
app.register_blueprint(blueprint_edit, url_prefix='/edit')
app.register_blueprint(blueprint_order, url_prefix='/order')


app.config['db_config'] = json.load(open('data_files/db_config.json'))
app.config['access_config'] = json.load(open('data_files/access.json'))
app.config['cache_config'] = json.load(open('data_files/cache.json'))

@app.route('/', methods=['GET', 'POST'])
@login_required
def menu_choice():
    #if 'user_id' in session:
    if session.get('user_group', None):
        return render_template('internal_user_menu.html')
    else:
        return render_template('external_user_menu.html')
    #else:
      #  redirect(url_for('blueprint_auth.start_auth'))
   

@app.route('/exit')
@login_required
def exit_func():
    session.clear()
    return 'До свиданья, заходите к нам еще.'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
