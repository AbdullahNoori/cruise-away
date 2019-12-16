from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.vacation
vacations = db.vacations
from flask import Flask, render_template,  request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def vacations_index():
    """Show all vacations."""
    return render_template('index.html', vacations=vacations.find())

@app.route('/vacations/new')
def vacations_new():
    """Create a new vacation."""
    return render_template('new.html')



# Note the methods parameter that explicitly tells the route that this is a POST
@app.route('/vacations', methods=['POST'])
def vacations_submit():
    """Submit a new vacation."""
    # Grab the image urls and make a list out of them
    images = request.form.get('images').split(',')
    # call our helper function to create the list of links
    vacation = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'image': request.form.get('image')
    }
    vacations.insert_one(vacation)
    return redirect(url_for('vacations_index'))
    
@app.route('/vacations/<vacation_id>')
def vacations_show(vacation_id):
    """Show a single playlist."""
    vacation = vacations.find_one({'_id': ObjectId(vacation_id)})
    return render_template('show.html', vacation=vacation)

@app.route('/vacations/<vacation_id>/edit')
def vacations_edit(vacation_id):
    """Show render vacait_edit."""
    vacation= vacations.find_one({'_id': ObjectId(vacation_id)})
    return render_template('edit.html', vacation=vacation)

@app.route('/vacations/<vacation_id>', methods=['POST'])
def vacation_update(vacation_id):
    """Submit an edited vacation."""
    # Grab the video IDs and make a list out of them
    images = request.form.get('images').split(',')
    # call our helper function to create the list of links
    vacation = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'images': images,
    }

    vacations.update_one(
        {'_id': ObjectId(vacation_id)},
        {'$set': vacation})
    return redirect(url_for('vacations_show', vacation_id=vacation_id))

@app.route('/vacations/<vacation_id>/delete', methods=['POST'])
def vacation_delete(vacation_id):
    """Action to delete a comment."""
    vacations.delete_one({'_id': ObjectId(vacation_id)})
    return redirect(url_for('vacations_index'))


if __name__ == '__main__':
    app.run()




