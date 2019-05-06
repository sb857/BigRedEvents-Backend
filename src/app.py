import json
from flask import Flask, request
from backend import Building, Host, Event
from backend import db

app = Flask(__name__)
db_filename = 'eventplanner.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def root():
    return 'Welcome to Big Red Events!!'

@app.route('/api/buildings/getAll/')
def get_buildings():
    """Returns all the buildings"""
    buildings = Building.query.all()
    if(buildings is not None):
        res = {'success': True, 'data': [Building.serialize() for building in buildings]}
        return json.dumps(res), 200
    return json.dumps({'success':False, 'error':'No buildings to display'}),404

@app.route('/api/buildings/get/<int:id>/')
def get_building_byid(id):
    """
    returns the building with <id>
    """
    building = Building.filter_by(id=id).first()
    if(building is not  None):
        return json.dumps({'success':True,'data':building.serialize()}),201
    return json.dumps({'success':False, 'error':'No such building found'}),404

@app.route('/api/buildings/create/',methods = ['POST'])
def create_building():
    """
    Adds a building accordint to the entered info.
    """
    post_body = json.loads(request.data)
    building = Building(

        name = post_body.get('name')
    )
    db.session.add(building)
    db.session.commit()
    return json.dumps({'success':True, 'data':building.serialize()}), 201

@app.route('/api/events/getAll/')
def get_events():
    """
    Returns all the events
    """
    events = Event.query.all()
    all_events = [event.serialize() for event in events]
    if(events is not None):
        res = {'success': True, 'data': {"events" : all_events}}
        return json.dumps(res), 200
    return json.dumps({'success':False, 'error':'No Events to display'}),404

@app.route('/api/events/get/<int:id>/')
def get_event_byid(id):
    """
    returns the event with <id>
    """
    event = Event.query.filter_by(id=id).first()
    if(event is not None):
        return json.dumps({'success':True,'data':event.serialize()}),201
    return json.dumps({'success':False, 'error':'No such event found'}),404

@app.route('/api/events/create/',methods = ['POST'])
def create_event():
    """
    Adds a event according to the entered info.
    """
    post_body = json.loads(request.data)
    event = Event(
        name = post_body.get('name',''),
        date = post_body.get('date',''),
        time = post_body.get('time', ''),
        tags = post_body.get('tags', ''),
        description = post_body.get('description', 'Not Specified'),
        organizerName = post_body.get('organizerName', 'Not Specified'),
        organizerContact = post_body.get('organizerContact', 'Not Specified'),
        dorm_id = post_body.get('dorm_id'),
    )
    db.session.add(event)
    db.session.commit()
    return json.dumps({'success':True, 'data':event.serialize()}), 201

@app.route('/api/events/delete/<int:id>/',methods = ['DELETE'])
def delete_event(id):
    """
    Deletes the event corresponding to id
    Parameter id: The event id for which the event is to be deleted
    """
    event = Event.query.filter_by(id = id).first()
    if event is not None:
        db.session.delete(event)
        db.session.commit()
        return json.dumps({'success': True, 'data': event.serialize()}), 201
    return json.dumps({'success': False, 'error': 'Event not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
