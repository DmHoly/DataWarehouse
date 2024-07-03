from taipy.gui import Gui
import taipy.gui.builder as tgb
# https://docs.taipy.io/en/latest/manuals/reference/pkg_taipy.gui.builder/

pages_md = """
# Getting started with Taipy GUI
My text: <|{text}|>
<|{text}|input|>
<|Run local|button|on_action=on_button_action|>

"""

if __name__ == '__main__':


    Gui(pages_md).run()