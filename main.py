
# Import necessary modules
from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Define the routes
@app.route('/')
def home():
    """Renders the homepage."""
    return render_template('index.html')

@app.route('/articles')
def articles():
    """Renders the articles page."""
    return render_template('articles.html')

@app.route('/stories')
def stories():
    """Renders the stories page."""
    return render_template('stories.html')

@app.route('/quizzes')
def quizzes():
    """Renders the quizzes page."""
    return render_template('quizzes.html')

@app.route('/resources')
def resources():
    """Renders the resources page."""
    return render_template('resources.html')

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
