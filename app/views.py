"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import os
from app import app,db
from flask import render_template, request, redirect, url_for, flash, send_from_directory 
from app.models import propertyDetails
from app.forms import propertyForm
from werkzeug.utils import secure_filename


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Joshua McIntosh")

@app.route('/properties/create', methods=["GET","POST"])
def crt_property():
    form = propertyForm()
    if request.method=='POST' and form.validate_on_submit():
        prop_title=request.form['prop_title']
        prop_bedrooms=request.form['prop_bedrooms']
        prop_bathrooms=request.form['prop_bathrooms']
        prop_location=request.form['prop_location']
        prop_price=request.form['prop_price']
        prop_type=request.form['prop_type']
        prop_descrip=request.form['prop_descrip']
        prop_img=request.form['prop_img']
        photo=secure_filename(prop_img.filename)
        prop_img.save(os.path.join(app.config['UPLOAD_FOLDER'], prop_img))
        propty=propertyDetails(prop_title,prop_bedrooms,prop_bathrooms,prop_location,prop_price,prop_type,prop_descrip,photo)
        db.session.add(propty)
        db.session.commit()
        flash('Property added successfully', 'success')
        return redirect(url_for('properties'))
    return render_template('create.html', form=form)
    

@app.route('/properties')
def disp_properties():
    properties=propertyDetails.query.all()
    return render_template('properties.html', properties=properties)

@app.route('/properties/<propertyid>')
def disp_property(propertyid):
    indv_property=propertyDetails.query(propertyDetails).filter(propertyDetails.id == propertyid).first()
    return render_template('property.html', indv_property=indv_property)


@app.route('/img-upload/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(),app.config[UPLOAD_FOLDER]), filename)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
