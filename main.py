import graphics
import get_events
import time
import datetime

WARNING_TIME = 10 * 60

while True:
    start, summary = get_events.get_next()
    if start:
        start_time = datetime.datetime.fromisoformat(start).timetuple()
        print(start_time)
        time_to_event = time.mktime(start_time) - time.time()
        if time_to_event < WARNING_TIME:
            graphics.alert(summary, str(start_time))
            break
        time.sleep(60)
    else:
        time.sleep(60)