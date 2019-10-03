#!.env/bin/python
# app.py

from db import db_session, init_db
from flask import Flask
from schema import schema
from flask_graphql import GraphQLView

app = Flask(__name__)
app.debug = True

example_query = """
{
  allDataCenters(sort: [NAME_ASC, ID_ASC]) {
    edges {
      node {
        id
        name
        department {
          id
          name
        }
        role {
          id
          name
        }
      }
    }
  }
}

// all depts

{ allDepartments {
    edges {
      node {
        id
        name
      }
    }
  } 
}
"""



app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    # init_db()
    app.run(
      host="0.0.0.0",
      port=5580,
      debug=app.debug    
)