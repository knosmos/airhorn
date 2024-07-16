import graphics
import get_events
import time
import datetime

WARNING_TIME = 10 * 60

while True:
    start, summary = get_events.get_next()
    if start:
        print(f"Next event: {summary} at {start}")
        start_time = datetime.datetime.fromisoformat(start)
        time_to_event = start_time.timestamp() - time.time()
        if time_to_event < WARNING_TIME:
            print(f"Launch alert! Time to event is {int(time_to_event)} seconds")
            graphics.alert(summary, str(start_time))
            break
        time.sleep(60)
    else:
        time.sleep(60)