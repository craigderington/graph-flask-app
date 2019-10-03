#!.env/bin/python
# app.py

import os
from db import db_session, init_db
from flask import Flask
from schema import schema
from flask_graphql import GraphQLView

app = Flask(__name__)
app.debug = True
app.secret_key = os.urandom(64)
app.port = 5580

example_query = """
{
  allDataCenters {
    edges {
      node {
        id
        name
        fabric
      }
    }
  }
}
"""
# add endpoint
app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    # init_db() => only when creating a new database
    app.start()
