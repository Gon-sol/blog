from ext import app
from routes import main, main2, register, log_in, logout, no_post_selected_page, create_post, posts_page

app.run(debug=True, host="0.0.0.0")