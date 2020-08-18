from flask import Flask , render_template , url_for


#import pdb
#pdb.set_trace()


app = Flask(__name__)

@app.route("/")

def index():
	return render_template('index.html')

#def dummy_api():
#	return "Madras Medical WebApplication : Vaccination"

if __name__ == "__main__":
	app.run(debug = True)