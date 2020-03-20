import os.path
from flask import Flask, redirect, url_for, render_template
import os
import json
import run_backend
import time

app = Flask(__name__, template_folder='templates')

app.config.update(
    SEND_FILE_MAX_AGE_DEFAULT = 0
)

def get_predictions():
    
    videos = []
    
    new_videos_json = "new_videos.json"
    if not os.path.exists(new_videos_json):
        run_backend.update_db()
    
    last_update = os.path.getmtime(new_videos_json) * 1e9
    
    #if time.time_ns() - last_update > (720*3600*1e9): ## 1 month +-
        #run_backend.update_db()
    
    with open("new_videos.json",'r') as data_file:
        for line in data_file:
            line_json = json.loads(line)
            videos.append(line_json)
    
    predictions = []
    
    for video in videos:
        predictions.append((video['video_id'], video['title'], float(video['score'])))
        
        
    predictions = sorted(predictions, key=lambda x: x[2], reverse=True)[:30]
    
    predictions_formatted = []
    
    for e in predictions:
        predictions_formatted.append("<tr><th><a href=\"{link}\">{title}</a></th><th>{score}</th></tr>".format(
        title=e[1], link=e[0],score=e[2]))
        
    return predictions, last_update, 
    

    
@app.route('/')
def main_page():
    preds, last_update = get_predictions()
    return render_template("index.html", preds=preds)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')