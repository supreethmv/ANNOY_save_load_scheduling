# ANNOY_save_load_scheduling
This repository is a demo for handling the scheduling of save and load functionality provided by the library ANNOY(Approximate Nearest Neighbor)

When trying to load and save the model in production, we shoud handle the exception that can occur, Gotta observe, the exception can occur either while saving or while loading, (may run to this issue in a very acute possibility, but it's good to be taken care of.) <br/>

ANNOY:<br/>
https://github.com/spotify/annoy

Install ANNOY:<br/>
pip install annoy

Reproduce error:<br/>
In the first terminal:<br/>
python .\annoy_database_update.py
<br/>
In another terminal:<br/>
python .\annoy_rec_service.py
<br/><br/>

Solution:
In the first terminal:<br/>
python .\annoy_database_update.py
<br/>
In another terminal:<br/>
python .\annoy_rec_service_exception_handled.py
<br/>
