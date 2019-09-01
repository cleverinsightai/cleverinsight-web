from app import app
from flask import request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'csv', 'CSV'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/research', methods=['GET', 'POST'])
def research():
    topics = [
        {'title': 'Predicting Power Demand and Reduce Wastage', 'description': "<p>The average electricity use in India during the 2016-17 FY was a staggering 1,122 kWh per capita. Out of this, the industrial consumption was 40%, followed by residential consumption at 24%. This is all to say that the power demand is surging beyond expectations as the population increases year-on-year.</p><p>Predicting power supply and demand, understanding the consumption pattern of households, classifying this by region/district/blocks, etc. are just some of the ways we can use data science in this sector. The resources I have mentioned below are enough to get you started and even go beyond that.</p>", 'category': 'Electricity'},
        {'title': 'Predicting Yield, Improve Soil & Forecasting demand', 'description': "<p>The agriculture industry needs the use of data science more than any other right now. 40% of our population is employed in this field but unfortunately, agriculture’s contribution to the nation’s economy is a paltry 16% of the overall GPD. Given how critical this sector is, should that number not be significantly higher?</p><p>There are a lot of facets in agriculture that can be worked upon – predicting monthly/quarterly/annual yield, forecasting demand, analyzing weather patterns to decide when to sow, predicting the prices of vegetables so as to pick which crop to sow, etc.</p>", 'category': 'Agriculture'},
        {'title': 'Water wastage & Distribution', 'description': "<p>The most critical resource of all, and one of the most misused in India. It seems we see a drought every summer in quite a lot of rural areas, and the situation does not seem to be improving. The water usage is increasing each year and unless we properly assess the usage, it could end up turning into a crisis very soon. You can predict things like the predicted water level, the usage in certain areas in order to send adequate water supply tanks there in time, etc. You can come up with more ideas as you think about the challenges in this sector.</p>", 'category': 'Water'},
        {'title': 'Affordable Healthcare & Demand', 'description': "<p>According to Wikipedia, 58% of the hospitals in India are private along with a mind-boggling 81% doctors.</p><p>The current infrastructure is just not good enough to handle the growing demands and the surging population. This is where data science can step in and ease the burden. Predicting things like how many days will a patient be admitted so as to calculate the proper allotment of beds, child mortality rate, heart issues, diabetes, etc. are some of the points you can work with for starters. The NITI Aayog initiative is already working on quite a lot of these points</p>", 'category': 'Healthcare'}

    ]
    return render_template('research.html', topics=topics)


@app.route('/mentors', methods=['GET', 'POST'])
def mentors():
    mentors = [
        { 'first_name' : 'Kothandaraman', 'last_name': 'Sridharan', 'bio': 'Engineering in Indian Institute of Science, Bangalore, Entrepreneurial Management from Stanford University. Cofounder, CEO and the Board of Director of BFL-Mphasis Software.'},
        { 'first_name' : 'Bastin', 'last_name': 'Robins .J', 'bio': 'A seasoned Data Scientist who has successfully built data products for largest FMCG and Retail, Banking, Telecom, Social, Government' },
        { 'first_name' : 'Anand', 'last_name': 'S', 'bio': 'Acknowledged as one of the top data scientists in the country. He leads the organisation in translating technology and innovation into processes and products that transform businesses.'},        
        { 'first_name' : 'Dr. Regi', 'last_name': 'Mathew', 'bio': 'PhD in Agriculture Management from IIM Ahmedabad and Post Graduate in Engineering from IIT Kharagpur. Former AVP-Analytics at GENPACT.'},
        { 'first_name' : 'Dr. Vandana', 'last_name': 'Bhagat', 'bio': 'PhD in Advanced Query Optimization. Esteemed professor in the area of computer science and data science.'},
        { 'first_name' : 'Dr. Chandrika', 'last_name': 'Kambam', 'bio': 'PhD in Advanced Query Optimization. Esteemed professor in the area of computer science and data science.'},
        { 'first_name' : 'Dr. Harsha', 'last_name': 'Doddihal', 'bio': 'PhD in Advanced Query Optimization. Esteemed professor in the area of computer science and data science.'},
    ]
    return render_template('mentors.html', mentors=mentors)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return ""

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        _file = request.files['file']
        if _file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if _file and allowed_file(_file.filename):
            filename = secure_filename(_file.filename)
            _file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            flash('File uploaded successfully')
            return redirect('/')
        else:
            flash('Invalid file')
    return redirect('/')
