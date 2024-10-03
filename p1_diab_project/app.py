from flask import *
import pickle

f = None
try:
	f = open("diab.model", "rb")
	model = pickle.load(f)
except Exception as e:
	print("issue", e)
finally:
	if f is not None:
		f.close()

app = Flask(__name__)

@app.route("/")


def home():
	if request.args.get("fs") and request.args.get("fu"):
		fs = float(request.args.get("fs"))
		fu = request.args.get("fu")
		if fu == "no":
			d = [[fs, 1, 0]]
		else:
			d = [[fs, 0, 1]]
		ans = model.predict(d)
		res = ans[0]
		if res == "NO":
			msg = "You dont have diabetes still take care"
		else:
			msg = "You might have diabetes. Please consult your doctor"
		return render_template("home.html", msg = msg)
	
	else:
		return render_template("home.html")


if __name__ == "__main__":
	app.run(debug = True, use_reloader = True)