from flask import render_template
from connexion.resolver import RestyResolver
import connexion
import prance
from typing import Any, Dict
from pathlib import Path

app = connexion.App(__name__, specification_dir='./')

# Create a URL route in our application for "/"
@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

def get_bundled_specs(main_file: Path) -> Dict[str, Any]:
    parser = prance.ResolvingParser(str(main_file.absolute()), 
        lazy = True, strict = False, backend = 'openapi-spec-validator')
    parser.parse()
    return parser.specification

# If we're running in stand alone mode, run the application
if __name__ == '__main__':    
    app.add_api(get_bundled_specs(Path("./swagger.yml")), resolver = connexion.RestyResolver("api"))
    app.run(host='0.0.0.0', port=8080, debug=True)