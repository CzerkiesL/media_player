from screeninfo import get_monitors

def get_screen():
    for monitor in get_monitors():
        if monitor.is_primary:
            return {
                "width" : monitor.width - 150,
                "height" : monitor.height - 150
            }