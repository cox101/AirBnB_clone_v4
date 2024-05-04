#!/usr/bin/python3
"""Starts a Flash Web Application."""
from os import environ
from flask import Flask, render_template
import uuid
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    """Remove the current SQLAlchemy Session."""
    storage.close()

@app.route('/0-hbnb', strict_slashes=False)
def hbnb():
    """Render the HBNB page."""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    st_ct = [(state, sorted(state.cities, key=lambda city: city.name)) for state in states]

    amenities = sorted(storage.all(Amenity).values(), key=lambda amenity: amenity.name)
    places = sorted(storage.all(Place).values(), key=lambda place: place.name)

    return render_template('0-hbnb.html', states=st_ct, amenities=amenities,
                           places=places, cache_id=uuid.uuid4())

if __name__ == "__main__":
    """Main Function."""
    app.run(host='0.0.0.0', port=5000)

