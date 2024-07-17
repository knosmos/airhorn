import graphics
import get_events
import time
import datetime

WARNING_TIME = 20 * 60
POLL_INTERVAL = 60
SNOOZE_TIME = 5 * 60

last_event = None
while True:
    next_event = get_events.get_next()
    if next_event:
        start, summary = next_event
        if start != last_event:
            print(f"Next event: {summary} at {start}")
            start_time = datetime.datetime.fromisoformat(start)
            time_to_event = start_time.timestamp() - time.time()
            if time_to_event < WARNING_TIME:
                print(f"Launch alert! Time to event is {int(time_to_event)} seconds")
                ret = graphics.alert(summary, str(start_time))
                if ret == "snooze":
                    time.sleep(SNOOZE_TIME)
                elif ret == "dismiss":
                    last_event = start
                continue
    time.sleep(POLL_INTERVAL)