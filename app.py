
from flask import Flask, jsonify, request  # type: ignore[reportMissingImports]

app = Flask(__name__)


# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}


# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]


# Helper function to find an event by its ID
def find_event(event_id):
    for event in events:
        if event.id == event_id:
            return event
    return None


# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code
    # Read the JSON data sent by the client
    data = request.get_json(silent=True)

    # Check that the request contains a valid JSON object
    if not isinstance(data, dict):
        return jsonify({"error": "A valid JSON object is required"}), 400

    # TODO: Task 3 - Implement the Loop and Process Each Element
    # Check that the title is provided and is not empty
    title = data.get("title")

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "A non-empty title is required"}), 400

    # Generate a unique ID for the new event
    new_id = max((event.id for event in events), default=0) + 1

    # Create the new event and add it to the list
    new_event = Event(new_id, title.strip())
    events.append(new_event)

    # TODO: Task 4 - Return and Handle Results
    # Return the created event with status code 201
    return jsonify(new_event.to_dict()), 201


# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    # Find the event with the requested ID
    event = find_event(event_id)

    # Return 404 if the event does not exist
    if event is None:
        return jsonify({"error": "Event not found"}), 404

    # Read the JSON data sent by the client
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "A valid JSON object is required"}), 400

    # TODO: Task 3 - Implement the Loop and Process Each Element
    # Validate the new title
    title = data.get("title")

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "A non-empty title is required"}), 400

    # Update the event's title
    event.title = title.strip()

    # TODO: Task 4 - Return and Handle Results
    # Return the updated event with status code 200
    return jsonify(event.to_dict()), 200


# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    # Find the event to delete
    event = find_event(event_id)

    # Return 404 if the event does not exist
    if event is None:
        return jsonify({"error": "Event not found"}), 404

    # TODO: Task 3 - Implement the Loop and Process Each Element
    # Remove the event from the in-memory list
    events.remove(event)

    # TODO: Task 4 - Return and Handle Results
    # Return a confirmation and the deleted event
    return jsonify({
        "message": "Event deleted successfully",
        "event": event.to_dict()
    }), 200


if __name__ == "__main__":
    app.run(debug=True)

