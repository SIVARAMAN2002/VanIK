from flask import Flask,render_template,request
from reviews_scraper import Process
app = Flask(__name__)

app.debug = True
@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        genre = request.form['genre']
        result = Process(location,genre)
        #result = "In the heart of the bustling city, a small cafe stands as a hidden gem, offering respite to weary souls. The aroma of freshly brewed coffee wafts through the air, embracing visitors in its warm embrace. The cozy atmosphere welcomes you with its dimly lit interior, soft jazz playing in the background, and comfortable armchairs. Patrons sit in quiet conversation, lost in their thoughts, or engrossed in a good book. The cafe's walls are adorned with local artwork, adding a touch of creativity to the space. Baristas behind the counter skillfully craft intricate latte designs, turning each cup into a work of art. The menu boasts an array of pastries, from flaky croissants to decadent chocolate cake. As the day progresses, the cafe transforms into a hub of productivity, with laptops open and the clatter of keyboards. It's a place where time seems to slow down, and a sense of community flourishes, making it a cherished spot in the midst of urban chaos."
    else:
        result = None

    return render_template('home.html', result=result)

if (__name__ == '__main__'):
    app.run(debug=True)

