import matplotlib.pyplot as plt

def create_figure_in_cm(width_cm,height_cm):
    width_inch = width_cm / 2.54
    height_inch = height_cm / 2.54

    fig = plt.figure(figsize=(width_inch, height_inch))
    return fig
