from taipy.gui import Gui, Markdown
from Reac_component_py.my_react_library import MyReactLibrary

my_lib = MyReactLibrary()

gui = Gui(page=Markdown('''
# My Custom Page
<|my_react_library.dynamic_react_element content="Hello from Dynamic React!"|>
'''))

gui.run()