from taipy.gui.extension import ElementLibrary, Element, ElementProperty, PropertyType

class MyReactLibrary(ElementLibrary):
    def get_name(self) -> str:
        return "my_react_library"

    def get_elements(self) -> dict:
        return {
            "dynamic_react_element": Element(
                "content",
                {
                    "content": ElementProperty(PropertyType.String, "Default Content"),
                },
                self.render_dynamic_react_element
            )
        }

    def render_dynamic_react_element(self, properties) -> str:
        return '<div id="dynamic-root"></div><script src="/Reac_component_py/dynamic_react_element.js"></script>'
