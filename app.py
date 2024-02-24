import os
from LLMModel import LLMModel
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/recommendationfromopenai', methods=['GET'])
def getRecommendations():
   query = request.args.get('ask')
   print(query)
   llm_model=LLMModel()
   llm_items = llm_model.get_llm_items(query)
   if query:
       print('Request for hello page received with name=%s' % query)
       return llm_items
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return "No results found"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
