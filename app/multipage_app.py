import panel as pn

# Définir les différentes pages de l'application
def page1():
    return pn.Column(
        pn.pane.Markdown("## Page 1"),
        pn.pane.Markdown("Ceci est le contenu de la première page.")
    )

def page2():
    return pn.Column(
        pn.pane.Markdown("## Page 2"),
        pn.pane.Markdown("Ceci est le contenu de la deuxième page.")
    )

def page3():
    return pn.Column(
        pn.pane.Markdown("## Page 3"),
        pn.pane.Markdown("Ceci est le contenu de la troisième page.")
    )

# Créer une instance de template
template = pn.template.MaterialTemplate(title="Mon Application Multipage")

# Ajouter des liens de navigation dans la barre latérale
nav = pn.Tabs(
    ('Page 1', page1),
    ('Page 2', page2),
    ('Page 3', page3),
)
template.main.append(nav)

# Afficher l'application
template.servable()
