from flask import Flask, request, render_template
from text_processor import generate_blobs

app = Flask(__name__)

@app.errorhandler(404)
def handle_not_found_error(error):
    """Error handling for 404 Not Found"""
    return render_template('404.html'), 404

@app.errorhandler(UnicodeDecodeError)
def handle_internal_server_error(error):
    """Error handling for 500 Internal Server Error"""
    app.logger.error("Unicode Decode Error occurred as: %s", str(error))
    return render_template('500.html'), 500

@app.errorhandler(500)
def handle_internal_server_error(error):
    """Error handling for 500 Internal Server Error"""
    app.logger.error("Internal Server Error occurred as: %s", str(error))
    return render_template('500.html'), 500
        
@app.route('/error-route')
def trigger_internal_server_error():
    """Raise an excepton to simulate internal server error"""
    raise Exception("Simulated internal server error")

@app.route('/')
def index():
    """Renders the index page."""
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
    """Handles file upload and generates text blobs."""
    file = request.files['file']
    if file and file.filename.endswith('.txt'):
        text = file.read().decode('utf-8')
        blobs = generate_blobs(text)
        return render_template('blobs.html', blobs=blobs)
    else:
        error_message = 'Invalid File Format, Please upload a text file'
        return render_template('400.html', error_message=error_message), 400

if __name__ == '__main__':
    app.run(debug=True)
