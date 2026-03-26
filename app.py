from flask import *
import nltk
nltk.download("vader_lexicon")
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import time

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
	if request.method == "POST":
		file = request.files["file"]
		data = file.read().decode("utf-8")
		lines = data.splitlines()[1:]
		sia = SentimentIntensityAnalyzer()
		result = "reviews,score,label\n"
		for line in lines:
			ps = sia.polarity_scores(line.strip())
			if ps["compound"] >= 0.05:
				label = "Positive"
			elif ps["compound"] <= -0.05:
				label = "Negative"
			else:
				label = "Neutral"
			result += line + "," + str(ps["compound"]) + "," + label + "\n"
		
		import os
		file_path = os.path.join(app.root_path, "output.csv")
		with open(file_path, "w") as f:
			f.write(result)
		return send_file(file_path, as_attachment=True)

	else:
		return render_template("home.html")

#app.run(debug=True, use_reloader=True)
