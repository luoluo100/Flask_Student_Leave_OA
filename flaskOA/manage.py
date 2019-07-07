from App.models import db
from App.views import app
db.create_all()
app.run(debug=True)