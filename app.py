from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global data
applications = [
    {"company": "Netflix", "role": "Frontend Developer", "status": "Applied", "date_applied": "2024-02-01", "deadline": "2024-02-10"},
    {"company": "Google", "role": "Data Analyst", "status": "Interview", "date_applied": "2024-01-20", "deadline": "2024-02-22"},
    {"company": "Facebook", "role": "Backend Engineer", "status": "Rejected", "date_applied": "2024-01-05", "deadline": "2024-02-15"},
    {"company": "Microsoft", "role": "UI/UX Designer", "status": "Interview", "date_applied": "2024-01-25", "deadline": "2024-03-01"},
]

activities = [
    {"date": "2024-02-01", "activity": "Completed Python assignment", "status": "Completed"},
    {"date": "2024-01-28", "activity": "Mentor meeting", "status": "Scheduled"},
]

# Dashboard route
@app.route('/')
def dashboard():
    stats = {
        "total_applications": len(applications),
        "active_tickets": sum(1 for act in activities if act['status'] not in ['Completed', 'Rejected']),
        "upcoming_deadlines": sum(1 for app in applications if app['deadline'] > "2024-01-31")
    }
    return render_template("dashboard.html", applications=applications, activities=activities, stats=stats)

# Applications page
@app.route('/applications')
def applications_page():
    stats = {
        "total_applications": len(applications),
        "active_tickets": sum(1 for act in activities if act['status'] not in ['Completed', 'Rejected']),
        "upcoming_deadlines": sum(1 for app in applications if app['deadline'] > "2024-01-31")
    }
    return render_template("applications.html", applications=applications, stats=stats)

# Other pages
@app.route('/tickets')
def tickets_page():
    return render_template("tickets.html")

# Show form to add a new application
@app.route('/application/new')
def new_application():
    return render_template("create_new_applications.html")


# Show form to add a new activity
@app.route('/activity/new')
def new_activity():
    return render_template("create_new_activity.html")

# Handle form submission
@app.route('/activity/add', methods=['POST'])
def add_activity():
    new_act = {
        "date": request.form['date'],
        "activity": request.form['activity'],
        "status": request.form['status']
    }
    activities.append(new_act)
    return redirect(url_for('dashboard'))  # Redirect to dashboard after adding

@app.route('/profile')
def profile_page():
    return render_template("profile.html")

@app.route('/settings')
def settings_page():
    return render_template("settings.html")

# Edit/Delete routes
@app.route('/application/edit/<int:id>')
def edit_application(id):
    app_data = applications[id]
    return f"Edit page for {app_data['company']}"

@app.route('/application/delete/<int:id>')
def delete_application(id):
    applications.pop(id)
    return redirect(url_for('applications_page'))


if __name__ == "__main__":
    app.run(debug=True)
