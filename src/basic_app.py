import pytermgui as ptg

with ptg.WindowManager() as manager:
    window = ptg.Window(
        "[wm-title]My first window","",
        ["Exit", lambda *_: manager.stop()],
    )
    manager.add(window)
    manager.run()
