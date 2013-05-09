from flask import Flask
import os
import threading
from functools import wraps
from flask import request, Response
import json
from datetime import datetime

html = """ 
<!DOCTYPE html>
<html>
<head>
       <style type="text/css">
               input#stopbutton {
                       width: 250px;
                       height: 100px;
                       font-size: 28px;
                       color: #FF0000;
               }
               input#coffeebutton {
                       width: 250px;
                       height: 100px;
                       font-size: 28px;
                       color: #008000;
               }
               input#coffeeoz {
                       width: 80px;
                       height: 60px;
                       font-size: 28px;
                       text-align: center;
               }
       </style>
<title>Coffee controller</title>
<script src="http://code.jquery.com/jquery-1.9.1.js"></script>
<script>
    $(document).ready(function(){
        $("#coffeebutton").click(function(){
            $.ajax({
                type: "POST",
                url: "/coffee",
                data: {"size": $("#coffeeoz").val()}
            })
        });
        $("#stopbutton").click(function(){
            $.post('/killall')
        });
    });
</script>
</head>
<body>
<font size = 16>
    I want to make <br>&nbsp;<input id="coffeeoz" type="number" name="quantity" min="12" max="100" value="16">&nbsp;ounces of coffee<br>
</font>
</body>
</html>
"""

def timesince(dt, default="just now"):
    """
    Returns string representing "time since" e.g.
    3 days ago, 5 hours ago etc.
    """

    now = datetime.utcnow()
    diff = now - dt
    
    periods = (
        (diff.days / 365, "year", "years"),
        (diff.days / 30, "month", "months"),
        (diff.days / 7, "week", "weeks"),
        (diff.days, "day", "days"),
        (diff.seconds / 3600, "hour", "hours"),
        (diff.seconds / 60, "minute", "minutes"),
        (diff.seconds, "second", "seconds"),
    )

    for period, singular, plural in periods:
        
        if period:
            return "%d %s ago" % (period, singular if period == 1 else plural)

    return default

@app.route('/')
def index():
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')
