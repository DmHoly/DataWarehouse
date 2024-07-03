import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import panel as pn

# Initialize Panel (no need to specify extensions here)
pn.extension()

def generate_time_series(nb_sample, nb_point, nb_feature):
    data = {}
    for i in range(nb_sample):
        data['sample_'+str(i)] = { 'feature_'+str(j): np.random.randn(nb_point) for j in range(nb_feature)}
    df = pd.DataFrame(data)
    return df.T

# Generate time series data
df = generate_time_series(10, 100, 5)

# Widgets for selection
sample_select = pn.widgets.Select(name='Sample', options=[f'sample_{i}' for i in range(10)])
# Replace the TextInput with a MultiSelect widget
feature_select = multi_choice = pn.widgets.MultiChoice(name='Features', value=['feature_0'],
    options=[f'feature_{i}' for i in range(5)])

# Function to update the plot
def update_plot(event=None):
    fig, ax = plt.subplots()
    sample_to_plot = sample_select.value
    # Use the selected features directly
    for feature in feature_select.value:
        if feature in df.loc[sample_to_plot].index:
            ax.plot(df.loc[sample_to_plot, feature], label=feature)
    ax.legend()
    plt.close(fig)
    return fig

# Initial plot
initial_plot = update_plot()

# Create a Matplotlib pane that will display the plot
mpl_pane = pn.pane.Matplotlib(initial_plot, tight=True)

# Define a function that updates the Matplotlib pane
def update_mpl_pane(event):
    mpl_pane.object = update_plot()

# Watch for changes to the widgets and update the plot accordingly
sample_select.param.watch(update_mpl_pane, 'value')
feature_select.param.watch(update_mpl_pane, 'value')

# Organize the layout
layout = pn.Column(pn.Row(sample_select, feature_select), mpl_pane)

# Serve the application
layout.servable()