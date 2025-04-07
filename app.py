from flask import Flask, render_template, request, redirect

import data_processing as dp
import initialize as init
import query as q

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handles requests to the root path ('/').

    If the request method is POST, it processes the search query and redirects to '/result'.
    If the query is deemed bad, it redirects to the '404.html' page.

    Returns:
        response: Flask render_template or redirect response.
    """
    global uquery, fs, squery

    if request.method == 'POST':
        squery = request.form.get('query')
        uquery, query_tags = dp.process(squery, stop_words_array)
        fs = 1

        if type(uquery) is int:
            return redirect('404.html')

        return redirect('/result')

    return render_template('index.html')


# Result page
@app.route('/result', methods=['GET', 'POST'])
def queries():
    """
    Handles requests to the '/result' path.

    If fs is 1, it retrieves data based on the processed query and renders the 'result.html' template.
    Handles POST requests for further actions (viewing sitting, speaker, or party details).

    Returns:
        response: Flask render_template or redirect response.
    """
    global sitting_id, data, speaker_name, party_name, squery, uquery, querries, fs

    if fs == 1:
        data = q.get_sittings(uquery, Data, index_dict, words_dict, tags_dict)
        querries = render_template('result.html', queryDetails=data, uquery=squery)

    if request.method == 'POST':
        if "sitting" in request.form:
            sitting_id = request.form.get('sitting')
            return redirect('/sitting')
        elif "speaker" in request.form:
            speaker_name = request.form.get('speaker')
            return redirect('/speaker')
        elif "party" in request.form:
            party_name = request.form.get('party')
            return redirect('/party')

    return querries


@app.route('/sitting', methods=['GET', 'POST'])
def sitting():
    """
    Handles requests to the '/sitting' path.

    Retrieves sitting information and renders the 'sitting.html' template.
    Handles POST requests for further actions (viewing speaker or party details).

    Returns:
        response: Flask render_template or redirect response.
    """
    global sitting_id, data, speaker_name, party_name, Data, tags_dict, fs
    data = q.get_sitting_info(sitting_id, Data, index_dict, tags_dict)
    fs += 1

    if request.method == 'POST':
        if "speaker" in request.form:
            speaker_name = request.form.get('speaker')
            return redirect('/speaker')
        elif "party" in request.form:
            party_name = request.form.get('party')
            return redirect('/party')

    return render_template('sitting.html', toPrint=data)


@app.route('/speaker', methods=['GET', 'POST'])
def speaker():
    """
    Handles requests to the '/speaker' path.

    Retrieves sittings by speaker and renders the 'speaker.html' template.
    Handles POST requests for further actions (viewing sitting or party details).

    Returns:
        response: Flask render_template or redirect response.
    """
    global sitting_id, data, speaker_name, party_name, Data, tags_dict, member_dict, fs
    sittings = q.get_sittings_by_speaker(speaker_name, Data, index_dict, tags_dict, member_dict)
    fs += 1

    if request.method == 'POST':
        if "sitting" in request.form:
            sitting_id = request.form.get('sitting')
            return redirect('/sitting')
        elif "party" in request.form:
            party_name = request.form.get('party')
            return redirect('/party')

    return render_template('speaker.html', sittings=sittings, speaker_name=speaker_name), 404


@app.route('/party', methods=['GET', 'POST'])
def party():
    """
    Handles requests to the '/party' path.

    Retrieves sittings by party and renders the 'party.html' template.
    Handles POST requests for further actions (viewing sitting or speaker details).

    Returns:
        response: Flask render_template or redirect response.
    """
    global sitting_id, data, speaker_name, party_name, Data, tags_dict, party_dict, member_dict, fs
    data = q.get_sittings_by_party(party_name, Data, index_dict, tags_dict, party_dict, member_dict)
    fs += 1

    if request.method == 'POST':
        if "sitting" in request.form:
            sitting_id = request.form.get('sitting')
            return redirect('/sitting')
        elif "speaker" in request.form:
            speaker_name = request.form.get('speaker')
            return redirect('/speaker')

    return render_template('party.html', sittings=data, party_name=party_name), 404


@app.errorhandler(404)
def page_not_found():
    """
    Handles 404 errors by rendering the '404.html' template.

    Returns:
        response: Flask render_template response.
    """
    return render_template('404.html'), 404


if __name__ == '__main__':
    """
    Initializes global variables and starts the Flask application.

    Note: Ensure the global variables (Data, index_dict, words_dict, member_dict, party_dict, tags_dict, 
    stop_words_array) are initialized before running the application.
    """
    global Data, index_dict, words_dict, member_dict, party_dict, tags_dict, stop_words_array, fs
    Data, index_dict, words_dict, stop_words_array, member_dict, party_dict, tags_dict = init.init()
    fs = 0
    app.run(debug=False)
