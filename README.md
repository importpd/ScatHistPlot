# ScatHistPlot

## Table of contents
1. [Introduction](#introduction)
2. [Purpose](#purpose)
3. [How to](#howto)
4. [Dependencies](#dependencies)

## Introduction <a id="introduction"></a>

A combined scatter-histogram plot for displaying (large) volumes of 2D data.

## Purpose

A way to display closely spaced/overlapping 2D data. Looking only at a regular
scatter plot in such case might hide potential density variations. Hence, combining the scatter
with two histograms.

Extreme example:

<img src="img/img_1.png" width=50% height=50%>

## How to <a id="howto"></a>

Below is a code snippet of calling the function and generating output using example data and default axes labeling.
```
x = np.random.normal(0, 1, 5000)
y = np.random.normal(0, 1, 5000)
scathistplot(x, y, xlabel='x', ylabel='y', histlabel='Frequency')
```
The code produces the following plot:

<img src="img/img.png" width=50% height=50%>

## Dependencies <a id="dependencies"></a>

|  Package   | Mandatory |           Description            |
|:----------:|:---------:|:--------------------------------:|
| matplotlib |    yes    |                -                 |
|   NumPy    |    no     | for generating example data only |
