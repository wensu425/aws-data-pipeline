{"filter":false,"title":"application.py","tooltip":"/EB/flask-app/application.py","undoManager":{"mark":34,"position":34,"stack":[[{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":[","],"id":2}],[{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":[" "],"id":3},{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["h"]},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["o"]}],[{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"remove","lines":["o"],"id":4},{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"remove","lines":["h"]}],[{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":["h"],"id":5},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["o"]},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["s"]},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":["t"]}],[{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"insert","lines":[" "],"id":6}],[{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"remove","lines":[" "],"id":7}],[{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"insert","lines":[" "],"id":8},{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":["="]}],[{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"insert","lines":[" "],"id":9}],[{"start":{"row":9,"column":31},"end":{"row":9,"column":33},"action":"insert","lines":["''"],"id":10}],[{"start":{"row":9,"column":32},"end":{"row":9,"column":33},"action":"insert","lines":["0"],"id":11},{"start":{"row":9,"column":33},"end":{"row":9,"column":34},"action":"insert","lines":["."]},{"start":{"row":9,"column":34},"end":{"row":9,"column":35},"action":"insert","lines":["0"]},{"start":{"row":9,"column":35},"end":{"row":9,"column":36},"action":"insert","lines":["."]},{"start":{"row":9,"column":36},"end":{"row":9,"column":37},"action":"insert","lines":["0"]},{"start":{"row":9,"column":37},"end":{"row":9,"column":38},"action":"insert","lines":["."]},{"start":{"row":9,"column":38},"end":{"row":9,"column":39},"action":"insert","lines":["0"]}],[{"start":{"row":9,"column":41},"end":{"row":42,"column":21},"action":"insert","lines":["from flask import Flask","","# print a nice greeting.","def say_hello(username = \"World\"):","    return '<p>Hello %s!</p>\\n' % username","","# some bits of text for the page.","header_text = '''","    <html>\\n<head> <title>EB Flask Test</title> </head>\\n<body>'''","instructions = '''","    <p><em>Hint</em>: This is a RESTful web service! Append a username","    to the URL (for example: <code>/Thelonious</code>) to say hello to","    someone specific.</p>\\n'''","home_link = '<p><a href=\"/\">Back</a></p>\\n'","footer_text = '</body>\\n</html>'","","# EB looks for an 'application' callable by default.","application = Flask(__name__)","","# add a rule for the index page.","application.add_url_rule('/', 'index', (lambda: header_text +","    say_hello() + instructions + footer_text))","","# add a rule when the page is accessed with a name appended to the site","# URL.","application.add_url_rule('/<username>', 'hello', (lambda username:","    header_text + say_hello(username) + home_link + footer_text))","","# run the app.","if __name__ == \"__main__\":","    # Setting debug to True enables debug output. This line should be","    # removed before deploying a production app.","    application.debug = True","    application.run()"],"id":12}],[{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"insert","lines":["a"],"id":13}],[{"start":{"row":0,"column":0},"end":{"row":42,"column":21},"action":"remove","lines":["from flask import Flask","","app = Flask(__name__)","","@app.route(\"/\")","def home():","    return \"Hello, World!\"a","    ","if __name__ == \"__main__\":","    app.run(debug=True, host = '0.0.0.0')from flask import Flask","","# print a nice greeting.","def say_hello(username = \"World\"):","    return '<p>Hello %s!</p>\\n' % username","","# some bits of text for the page.","header_text = '''","    <html>\\n<head> <title>EB Flask Test</title> </head>\\n<body>'''","instructions = '''","    <p><em>Hint</em>: This is a RESTful web service! Append a username","    to the URL (for example: <code>/Thelonious</code>) to say hello to","    someone specific.</p>\\n'''","home_link = '<p><a href=\"/\">Back</a></p>\\n'","footer_text = '</body>\\n</html>'","","# EB looks for an 'application' callable by default.","application = Flask(__name__)","","# add a rule for the index page.","application.add_url_rule('/', 'index', (lambda: header_text +","    say_hello() + instructions + footer_text))","","# add a rule when the page is accessed with a name appended to the site","# URL.","application.add_url_rule('/<username>', 'hello', (lambda username:","    header_text + say_hello(username) + home_link + footer_text))","","# run the app.","if __name__ == \"__main__\":","    # Setting debug to True enables debug output. This line should be","    # removed before deploying a production app.","    application.debug = True","    application.run()"],"id":14}],[{"start":{"row":0,"column":0},"end":{"row":33,"column":21},"action":"insert","lines":["from flask import Flask","","# print a nice greeting.","def say_hello(username = \"World\"):","    return '<p>Hello %s!</p>\\n' % username","","# some bits of text for the page.","header_text = '''","    <html>\\n<head> <title>EB Flask Test</title> </head>\\n<body>'''","instructions = '''","    <p><em>Hint</em>: This is a RESTful web service! Append a username","    to the URL (for example: <code>/Thelonious</code>) to say hello to","    someone specific.</p>\\n'''","home_link = '<p><a href=\"/\">Back</a></p>\\n'","footer_text = '</body>\\n</html>'","","# EB looks for an 'application' callable by default.","application = Flask(__name__)","","# add a rule for the index page.","application.add_url_rule('/', 'index', (lambda: header_text +","    say_hello() + instructions + footer_text))","","# add a rule when the page is accessed with a name appended to the site","# URL.","application.add_url_rule('/<username>', 'hello', (lambda username:","    header_text + say_hello(username) + home_link + footer_text))","","# run the app.","if __name__ == \"__main__\":","    # Setting debug to True enables debug output. This line should be","    # removed before deploying a production app.","    application.debug = True","    application.run()"],"id":15}],[{"start":{"row":33,"column":20},"end":{"row":33,"column":56},"action":"insert","lines":["host=’0.0.0.0′,port=8080, debug=True"],"id":16}],[{"start":{"row":33,"column":33},"end":{"row":33,"column":34},"action":"remove","lines":["′"],"id":17}],[{"start":{"row":33,"column":33},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":18},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"remove","lines":["    "],"id":19},{"start":{"row":33,"column":33},"end":{"row":34,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":33,"column":33},"end":{"row":33,"column":34},"action":"insert","lines":["'"],"id":20}],[{"start":{"row":33,"column":25},"end":{"row":33,"column":26},"action":"remove","lines":["’"],"id":21}],[{"start":{"row":33,"column":25},"end":{"row":33,"column":26},"action":"insert","lines":["'"],"id":22}],[{"start":{"row":17,"column":29},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":23}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"insert","lines":["a"],"id":24},{"start":{"row":18,"column":1},"end":{"row":18,"column":2},"action":"insert","lines":["p"]},{"start":{"row":18,"column":2},"end":{"row":18,"column":3},"action":"insert","lines":["p"]},{"start":{"row":18,"column":3},"end":{"row":18,"column":4},"action":"insert","lines":["l"]},{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"insert","lines":["i"]},{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"insert","lines":["c"]},{"start":{"row":18,"column":6},"end":{"row":18,"column":7},"action":"insert","lines":["a"]},{"start":{"row":18,"column":7},"end":{"row":18,"column":8},"action":"insert","lines":["t"]},{"start":{"row":18,"column":8},"end":{"row":18,"column":9},"action":"insert","lines":["i"]},{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"insert","lines":["o"]}],[{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"remove","lines":["o"],"id":25}],[{"start":{"row":18,"column":9},"end":{"row":18,"column":12},"action":"insert","lines":["   "],"id":26}],[{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"remove","lines":[" "],"id":27},{"start":{"row":18,"column":10},"end":{"row":18,"column":11},"action":"remove","lines":[" "]},{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"remove","lines":[" "]}],[{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"insert","lines":["o"],"id":28},{"start":{"row":18,"column":10},"end":{"row":18,"column":11},"action":"insert","lines":["n"]},{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"insert","lines":["."]},{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"insert","lines":["s"]},{"start":{"row":18,"column":13},"end":{"row":18,"column":14},"action":"insert","lines":["e"]},{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":["c"]},{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"insert","lines":["r"]},{"start":{"row":18,"column":16},"end":{"row":18,"column":17},"action":"insert","lines":["e"]},{"start":{"row":18,"column":17},"end":{"row":18,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"insert","lines":[" "],"id":29}],[{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"remove","lines":[" "],"id":30}],[{"start":{"row":18,"column":18},"end":{"row":18,"column":19},"action":"insert","lines":["_"],"id":31},{"start":{"row":18,"column":19},"end":{"row":18,"column":20},"action":"insert","lines":["k"]},{"start":{"row":18,"column":20},"end":{"row":18,"column":21},"action":"insert","lines":["e"]},{"start":{"row":18,"column":21},"end":{"row":18,"column":22},"action":"insert","lines":["y"]}],[{"start":{"row":18,"column":22},"end":{"row":18,"column":23},"action":"insert","lines":[" "],"id":32},{"start":{"row":18,"column":23},"end":{"row":18,"column":24},"action":"insert","lines":["="]}],[{"start":{"row":18,"column":24},"end":{"row":18,"column":25},"action":"insert","lines":[" "],"id":33}],[{"start":{"row":18,"column":25},"end":{"row":18,"column":27},"action":"insert","lines":["''"],"id":34}],[{"start":{"row":18,"column":26},"end":{"row":18,"column":27},"action":"insert","lines":["1"],"id":35},{"start":{"row":18,"column":27},"end":{"row":18,"column":28},"action":"insert","lines":["2"]},{"start":{"row":18,"column":28},"end":{"row":18,"column":29},"action":"insert","lines":["3"]},{"start":{"row":18,"column":29},"end":{"row":18,"column":30},"action":"insert","lines":["4"]},{"start":{"row":18,"column":30},"end":{"row":18,"column":31},"action":"insert","lines":["5"]}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":32},"action":"remove","lines":["application.secret_key = '12345'"],"id":36},{"start":{"row":17,"column":29},"end":{"row":18,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":19,"column":32},"end":{"row":19,"column":32},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1605646669919,"hash":"de7c4a751fb958f4eba0fc759ed3109c3cac2e8a"}