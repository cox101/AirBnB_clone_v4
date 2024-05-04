#!/usr/bin/python3
"""Starts a Flash Web Application."""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
import uuid

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    """Remove the current SQLAlchemy Session."""
    storage.close()

@app.route('/2-hbnb', strict_slashes=False)
def hbnb():
    """Renders the HBNB page."""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    states_with_cities = [(state, sorted(state.cities, key=lambda city: city.name)) for state in states]

    amenities = sorted(storage.all(Amenity).values(), key=lambda amenity: amenity.name)
    places = sorted(storage.all(Place).values(), key=lambda place: place.name)

    return render_template('2-hbnb.html', states=states_with_cities, amenities=amenities,
                           places=places, cache_id=uuid.uuid4())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

