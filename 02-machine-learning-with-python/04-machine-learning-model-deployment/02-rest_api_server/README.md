```sh
curl -X POST -H "Content-Type: application/json" -d '{"data": [[3, 5, 4, 2]]}' http://localhost:5000/predict
curl -X POST -H "Content-Type: application/json" -d '{"data": [[3, 5, 4, 2], [5, 4, 3, 2]]}' http://localhost:5000/predict
```

PythonAnywhere

```sh
mkvirtualenv --python=/usr/bin/python3.6 my-virtualenv
workon my-virtualenv
pip install flask scikit-learn
```
