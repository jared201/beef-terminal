import sys
import pytermgui as ptg

PTG_CONFIG = """\
config:
    Window:
        styles:
            border: &border-style "[60]{item}"
            corner: *border-style
    Button:
        styles:
            labels: "[@235 108 bold]{item}"
    Splitter:
        chars:
            separator: "  "
markup:
    title: 210 bold
    body: 245 italic
"""
with ptg.WindowManager() as manager:
    # INITIALIZE a loader and load the config
    loader = ptg.YamlLoader()
    loader.load(PTG_CONFIG)

    # Create a new test window
    manager.add(
        ptg.Window()
        + "[title] This is our title"
        + ""
        + {"[body]First Key": ["First Button"]}
        + {"[body]Second Key": ["Second Button"]}
        + {"[body]Third Key": ["Third Button"]}
        + ""
        + ["Exit", lambda *_: manager.stop()]
    )

    manager.run()
