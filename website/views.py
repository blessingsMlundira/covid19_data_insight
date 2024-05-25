from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


# visualization data
# MongoDB connection string
CONNECTION_STRING = "mongodb+srv://blessingsmlundira:vjOUpGcniJ1QuRMo@cluster0.71vdfjx.mongodb.net/test?retryWrites=true&w=majority"

# Connect to MongoDB
client = MongoClient(CONNECTION_STRING)
db = client.get_database('covid19_database')
collection = db.get_collection('covid19_data')

# Retrieve data from MongoDB
results = collection.find()
df = pd.DataFrame(list(results))

@views.route('/tables', methods=['GET', 'POST'])
def tables():
    # Convert DataFrame to HTML table
    table_html = df.to_html(classes='table table-striped', index=False)
    return render_template('tables.html', table_html=table_html, user=current_user)


@views.route('/graph_visuals', methods=['GET', 'POST'])
def graph_visuals():
    # Generate visualizations
    plots = []
    sns.set(style="whitegrid")

    # Age Distribution
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(df['Age'], bins=20, kde=True, ax=ax)
    ax.set_title('Age Distribution of COVID-19 Patients')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    plots.append(plot_to_img(fig))

    # Test Results Distribution
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.countplot(data=df, x='TestResult', ax=ax)
    ax.set_title('Test Results Distribution')
    ax.set_xlabel('Test Result')
    ax.set_ylabel('Count')
    plots.append(plot_to_img(fig))

    # Daily Positive Cases
    positive_cases = df[df['TestResult'] == 'Positive']
    positive_cases_daily = positive_cases.groupby('DateTested').size().reset_index(name='PositiveCases')
    fig, ax = plt.subplots(figsize=(14, 7))
    sns.lineplot(x='DateTested', y='PositiveCases', data=positive_cases_daily, marker='o', ax=ax)
    ax.set_title('Daily Positive COVID-19 Cases')
    ax.set_xlabel('Date Tested')
    ax.set_ylabel('Number of Positive Cases')
    plots.append(plot_to_img(fig))

    # Correlation Matrix
    numeric_data = df[['Age', 'Hospitalized', 'Recovered']]
    correlation_matrix = numeric_data.corr()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
    ax.set_title('Correlation Matrix')
    plots.append(plot_to_img(fig))

    # Hospitalization and Recovery Rate by Gender
    gender_analysis = df.groupby('Gender').agg({
        'Age': 'mean',
        'Hospitalized': 'mean',
        'Recovered': 'mean'
    }).reset_index()
    gender_analysis['Hospitalized'] *= 100
    gender_analysis['Recovered'] *= 100

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 14))
    sns.barplot(x='Gender', y='Hospitalized', data=gender_analysis, palette='viridis', ax=ax1)
    ax1.set_title('Hospitalization Rate by Gender')
    ax1.set_ylabel('Hospitalization Rate (%)')

    sns.barplot(x='Gender', y='Recovered', data=gender_analysis, palette='viridis', ax=ax2)
    ax2.set_title('Recovery Rate by Gender')
    ax2.set_ylabel('Recovery Rate (%)')

    plots.append(plot_to_img(fig))

    return render_template('graph.html', plots=plots, user=current_user)

def plot_to_img(fig):
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return plot_url
    