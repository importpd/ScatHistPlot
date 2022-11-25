import numpy as np
import matplotlib.pyplot as plt


def scathistplot(x: list, y: list, xlabel: str = 'x', ylabel: str = 'y', histlabel: str = 'Frequency'):
    """A combined scatter-histogram plot for displaying (large) volumes of 2D data.

    A way to display closely spaced/overlapping 2D data. Looking only at a regular
    scatter plot in such case might hide potential density variations. Hence, combining
    the scatter with two histograms.

    Params
    ------
        x: list of float or int
        y: list of float or int
        xlabel: str
            Optional. Default is 'x'.
        ylabel: str
            Optional. Default is 'y'.
        histlabel: str
            Optional. Default is 'Frequency'.
    """
    plt.figure()
    scatter_axes = plt.subplot2grid((3, 3), (1, 0), rowspan=2, colspan=2)
    x_hist_axes = plt.subplot2grid((3, 3), (0, 0), colspan=2, sharex=scatter_axes)
    y_hist_axes = plt.subplot2grid((3, 3), (1, 2), rowspan=2, sharey=scatter_axes)

    scatter_axes.plot(x, y, 'k.', markersize=8)
    scatter_axes.grid(alpha=0.3)
    scatter_axes.set_xlabel(xlabel)
    scatter_axes.set_ylabel(ylabel)

    x_hist_axes.hist(x, edgecolor='grey', color='black')
    y_hist_axes.hist(y, orientation='horizontal', edgecolor='grey', color='black')

    x_hist_axes.xaxis.tick_top()
    x_hist_axes.set_xlabel(xlabel)
    x_hist_axes.xaxis.set_label_position('top')
    x_hist_axes.set_ylabel(histlabel)
    x_hist_axes.grid(alpha=0.3)

    y_hist_axes.yaxis.tick_right()
    y_hist_axes.xaxis.tick_top()
    y_hist_axes.set_xlabel(histlabel)
    y_hist_axes.xaxis.set_label_position('top')
    y_hist_axes.set_ylabel(ylabel)
    y_hist_axes.yaxis.set_label_position('right')
    y_hist_axes.grid(alpha=0.3)

    plt.subplots_adjust(wspace=0.05, hspace=0.05)
    plt.show()


# Generate example data
x = np.random.normal(0, 1, 5000)
y = np.random.normal(0, 1, 5000)

# Call the ScatHistPlot function
scathistplot(x, y, xlabel='x', ylabel='y', histlabel='Frequency')
