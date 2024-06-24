from taipy.gui import Gui
import taipy.gui.builder as tgb
# https://docs.taipy.io/en/latest/manuals/reference/pkg_taipy.gui.builder/

if __name__ == '__main__':
    show = True
    some_content = "Training app"
    with tgb.Page() as page:

        tgb.html("h1", "Hello, world!")
        with tgb.expandable("Data selector"):
            with tgb.layout(columns="2 2"):
                with tgb.part():
                    tgb.text("1st column content")
                with tgb.part():
                    tgb.text("2nd column content")

        with tgb.expandable("Model selector"):
            tgb.text("Select model")
        with tgb.expandable("Viewer selector"):
            tgb.text("Select viewer")

    Gui(page).run()