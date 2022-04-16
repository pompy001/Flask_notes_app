"""
we can do this because whereever we pu a __init__.py file that folder become a python package
by default it will run all in __init__ file
"""
from website import create_app

app = create_app()
if __name__ =="__main__":
    app.run(debug =True)
