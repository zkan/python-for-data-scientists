import flask
import pickle


app = flask.Flask(__name__)
model = None


@app.route('/predict', methods=['POST'])
def predict():
    if flask.request.method == 'POST':
        with open('./knn.pkl', 'rb') as f:
            model = pickle.load(f)

        data = flask.request.get_json()
        pred = model.predict(data['data'])
        results = {
            'results': pred.tolist()
        }

        return flask.jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
