import panel as pn
pn.extension()

# Add the CSS directly
pn.config.raw_css.append("""
.background-transparent {
    background-color: transparent;
}
.superpose img {
    width: 100%;
    height: 100%;
    object-fit: cover; 
}
.bouton-position {
    position: absolute;
    top: 82%; /* Ajustez selon les besoins */
    left: 50%; /* Ajustez selon les besoins */
    transform: translate(-50%, -50%); /* Centrer le bouton par rapport à ses coordonnées top et left */
    z-index: 10; /* bouton est au-dessus de l'image */
}
.formulaire-au-dessus {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 10;
}
.bouton-arrondi {
    border-radius: 20px; /* Arrondi des coins */
    padding: 10px 20px; /* Taille du padding pour une forme allongée */
    font-size: 16px; /* Taille de la police */
}
/* General Styles */
body, html {
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
    overflow-x: hidden;
}

/* Header Styles */
.header {
    background-color: #2C3E50; /* Dark blue shade */
    color: #ECF0F1; /* Light grey */
    padding: 10px 20px;
    text-align: center;
    font-size: 24px;
}

/* Sidebar Styles */
.sidebar {
    background-color: #34495E; /* Darker blue shade */
    color: #ECF0F1;
    padding: 20px;
    width: 200px;
    min-height: 100vh; /* Full height */
    box-shadow: 2px 0 5px rgba(0,0,0,0.5); /* Adds depth with a shadow */
    transition: width 0.5s; /* Smooth transition for retracting/expanding */
}

.sidebar.hidden {
    width: 0; /* Retract sidebar */
    overflow: hidden;
    transition: width 0.5s;
}

/* Sidebar Item Styles */
.sidebar-item {
    margin: 10px 0;
    cursor: pointer;
    transition: background-color 0.3s;
}

.sidebar-item:hover {
    background-color: #3D566E; /* Slightly lighter blue for hover effect */
}

/* Central Zone Styles */
.central-zone {
    padding: 20px;
    margin-left: 220px; /* Adjust based on sidebar width */
    transition: margin-left 0.5s;
}

.central-zone.fullwidth {
    margin-left: 0; /* When sidebar is retracted */
    transition: margin-left 0.5s;
}

/* Button Styles */
.button-primary {
    background-color: #3498DB; /* Blue */
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px; /* Rounded corners */
    cursor: pointer;
    transition: background-color 0.3s;
}

.button-primary:hover {
    background-color: #2980B9; /* Darker blue on hover */
}
""")
class App:
    def __init__(self):
        self.background_image = r"C:\Users\Mehdi\PycharmProjects\DataWarehouse\ressources\Application_logo.jpeg"
        self.login_form = self.create_login_form()
        self.button = pn.widgets.Button(name=' Enter ', button_type='primary', width=200, height=50,
                                        css_classes=['bouton-arrondi', 'bouton-position'])

        # Utilisez css_classes pour appliquer le style de superposition
        self.app = pn.Column(
            pn.pane.JPG(self.background_image, sizing_mode='stretch_both', css_classes=['superpose']),
            self.button,
            align='center',
            sizing_mode='stretch_both'
        )
        #-----------------------------------------
        self.button.on_click(self.show_blank_page)

    def create_header(self):
        return pn.Row(pn.pane.Markdown("# Header", css_classes=['header']), align='center')

    def create_sidebar(self):
        sidebar_content = pn.Column("Item 1", "Item 2", css_classes=['sidebar-item'], align='start')
        toggle_button = pn.widgets.Toggle(name='Show/Hide Sidebar', button_type='primary', value=True,
                                          css_classes=['button-primary'])
        sidebar = pn.Column(toggle_button, sidebar_content, css_classes=['sidebar'], width=200, sizing_mode='fixed')

        # Correctly use jslink with a JS callback
        toggle_button.jslink(sidebar, code={'value': '''
            if (source.active) {
                target.style.display = 'block';
            } else {
                target.style.display = 'none';
            }
        '''})
        return sidebar

    def create_central_zone(self):
        return pn.Column("Central content goes here", css_classes=['central-zone'], align='center')

    def show_blank_page(self, event):
        self.app.clear()
        _home_page = self.home_page()
        self.app.append(_home_page)

    def home_page(self):
        header = self.create_header()
        sidebar = self.create_sidebar()
        central_zone = self.create_central_zone()
        # Layout that includes the header at the top, and below it a row with the sidebar and central zone
        layout = pn.Column(header, pn.Row(sidebar, central_zone, sizing_mode='stretch_width'),
                           sizing_mode='stretch_width')
        return layout

    def create_login_form(self):
        username_input = pn.widgets.TextInput(name='Username', placeholder='Enter Username')
        password_input = pn.widgets.PasswordInput(name='Password', placeholder='Enter Password')
        login_button = pn.widgets.Button(name='Login', button_type='primary')
        # Appliquez css_classes ici aussi pour le positionnement absolu
        form = pn.Column(username_input, password_input, login_button, align='center', css_classes=['formulaire-au-dessus'])
        return form

    def run(self):
        self.app.servable()
        self.app.show()

if __name__ == '__main__':
    app_instance = App()
    app_instance.run()