# Flask Full CRUD RESTful API Lab

## Project Description

This project implements an Event Management REST API using Python and Flask.
It allows clients to create, update, and delete events through HTTP requests.

The application uses a custom Event class and an in-memory Python list
to simulate database storage. The API accepts JSON input and returns
structured JSON responses with appropriate HTTP status codes.

## Learning Objectives

- Implement RESTful endpoints using Flask.
- Handle POST, PATCH, and DELETE requests.
- Read JSON input using request.get_json().
- Use a custom Python class to represent events.
- Store and modify data using an in-memory list.
- Validate input and handle missing resources.
- Return appropriate HTTP status codes and JSON responses.

## Technologies Used

- Python 3
- Flask
- JSON
- Postman or curl for API testing

## Installation and Setup

### 1. Create and activate a virtual environment

On Linux:

    python3 -m venv .venv
    source .venv/bin/activate

### 2. Install Flask

    python -m pip install flask

### 3. Run the application

    python app.py

The server will run at:

    http://127.0.0.1:5000

Keep the terminal open while testing the API.

## Initial Event Data

The application starts with two events:

    [
        {
            "id": 1,
            "title": "Tech Meetup"
        },
        {
            "id": 2,
            "title": "Python Workshop"
        }
    ]

## API Endpoints

### 1. Create an Event

Method: POST

Endpoint: /events

Description: Creates a new event using a title supplied in JSON.

Example request body:

    {
        "title": "Hackathon"
    }

Example curl command:

    curl -X POST http://127.0.0.1:5000/events \
      -H "Content-Type: application/json" \
      -d '{"title": "Hackathon"}'

Example response:

    {
        "id": 3,
        "title": "Hackathon"
    }

Status code: 201 Created

A missing or invalid title returns 400 Bad Request.

### 2. Update an Event

Method: PATCH

Endpoint: /events/<event_id>

Description: Updates the title of an existing event.

Example request body:

    {
        "title": "Hackathon 2025"
    }

Example curl command:

    curl -X PATCH http://127.0.0.1:5000/events/1 \
      -H "Content-Type: application/json" \
      -d '{"title": "Hackathon 2025"}'

Example response:

    {
        "id": 1,
        "title": "Hackathon 2025"
    }

Status code: 200 OK

If the event does not exist, the API returns 404 Not Found.

### 3. Delete an Event

Method: DELETE

Endpoint: /events/<event_id>

Description: Removes an event from the in-memory list.

Example curl command:

    curl -X DELETE http://127.0.0.1:5000/events/2

Status code: 204 No Content. The response has no body.

If the event does not exist, the API returns 404 Not Found.

## Error Handling

The API returns JSON error messages for invalid requests.

Example:

    {
        "error": "A non-empty title is required"
    }

Status code: 400 Bad Request

For an event that cannot be found:

    {
        "error": "Event not found"
    }

Status code: 404 Not Found

## Data Storage

The application uses an in-memory list instead of a database.
Changes remain available while the server is running but are lost
when the application restarts.

## Testing

The API can be tested using Postman or curl.

Recommended tests:

1. Create an event with POST /events.
2. Update an event with PATCH /events/1.
3. Delete an event with DELETE /events/2.
4. Submit a request with a missing title and confirm status 400.
5. Request an event ID that does not exist and confirm status 404.
6. Try updating and deleting an event ID that does not exist.

## Conclusion

This project demonstrates the core operations of a RESTful API,
JSON request processing, input validation, resource lookup,
in-memory data mutation, and HTTP error handling.
