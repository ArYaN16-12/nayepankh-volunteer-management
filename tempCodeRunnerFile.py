@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect('/admin')