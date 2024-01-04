from website import create_app
from website.getAI import main_get_news
import threading

app = create_app()

if __name__ == '__main__':

    t1 = threading.Thread(target=app.run)
    t2 = threading.Thread(target=main_get_news, args=(2500, app))

    # app.run(debug=True)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
