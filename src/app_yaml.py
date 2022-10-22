import pytermgui as ptg

with open(args.file, "r") as file:
    namespace = ptg.YamlLoader().load(args.file)

with ptg.WindowManager() as manager:
    manager.add(namespace.MainWindow.center())

    popup = namespace.PopupWindow.center()
    popup.bind(ptg.keys.CTRL_W, lambda window, _: window.close())

    button = ptg.get_widget("button-definition")
    button.onclick = lambda *_: manager.add(popup)

    manager.run()
