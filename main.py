# Run: uvicorn main:app --host 127.0.0.1 --port 8000

import json
import falcon
import falcon.asgi


# falcon.asgi.App instances are callable ASGI apps...
# in larger applications the app is created in a separate file
app = falcon.asgi.App()


def getUsers():
    users = []
    for index in range(1, 1001):
        strIndex = str(index)
        firstName = "FirstName" + strIndex
        lastName = "LastName" + strIndex
        framework = "Python (FastAPI)"
        users.append({
            "index": index,
            "FirstName": firstName,
            "LastName": lastName,
            "age": 25,
            "framework": framework,
        })
    return users


class Users:
    async def on_get(self, req, resp):
        resp.body = json.dumps(getUsers())


# http://127.0.0.1:8000/users
app.add_route('/users', Users())


if __name__ == "__main__":
    app.run()
