===================
Welcome to peccary!
===================

A mind-numbingly simple wrapper around the `plotly JavaScript library`_.

∘
`MIT license <https://github.com/bwoodsend/peccary/blob/master/LICENSE>`_
∘
`Bug reports <https://github.com/bwoodsend/peccary/issues>`_
∘
`Support <https://github.com/bwoodsend/peccary/discussions>`_


Installation
------------

To install peccary, run the following in your terminal:

.. code-block:: console

    pip install "git+ssh://git@github.com/bwoodsend/peccary.git"


Usage
-----

The API of ``peccary`` is designed to be so thin that there's no API
reinvention involved.
It is just `plotly's JavaScript API` but with written in Python syntax rather
than JavaScript.
This guide will therefore cover the conversion only and from there onwards you
can just refer to the examples in `plotly's JavaScript API`_ documentation.

Every plotly scene consists of three key elements:

* An HTML div which plotly will draw into.

* ``data`` - A list of dictionaries: Each dictionary corresponds to a trace
  which can be a line, a group scatter points, a heatmap, a series of bars in a
  bar chart, etc.

* ``layout`` - A dictionary: Scene-wide parameters which configure axis titles,
  units, limits, logarithmic vs linear scales, size, shape and aspect ratio,
  etc. If no customisation is needed then this parameter may be omitted.

In ``peccary``, the HTML div corresponds to a ``peccary.Scene()``, each trace in
``data`` is added via ``scene.plot()``, and the ``layout`` is provided
either as keyword arguments to ``peccary.Scene()`` or by writing to the ``dict``
stored at ``scene.layout``.

Finally, a JavaScript example converted to ``peccary``!
Below is a generic plotly JavaScript example adopted `from their own
documentation
<https://plotly.com/javascript/line-and-scatter/#line-and-scatter-plot>`_.

.. code-block:: javascript

    var trace1 = {
      x: [1, 2, 3, 4],
      y: [10, 15, 13, 17],
      mode: 'markers',
      type: 'scatter'
    };

    var trace2 = {
      x: [2, 3, 4, 5],
      y: [16, 5, 11, 9],
      mode: 'lines',
      type: 'scatter'
    };

    var trace3 = {
      x: [1, 2, 3, 4],
      y: [12, 9, 15, 12],
      mode: 'lines+markers',
      type: 'scatter'
    };

    var data = [trace1, trace2, trace3];
    var layout = {
        title: 'My first plotly graph written in Python!'
    }

    Plotly.newPlot('myDiv', data, layout);


And here is the same example but written in Python.

.. code-block:: python

    import peccary

    # Create a scene with the optional `title` layout key set.
    scene = peccary.Scene(title="My first plotly graph written in Python!")

    # Add traces 1, 2 and 3. Keys in JavaScript's maps correspond to keyword
    # arguments to scene.plot(). You can do this as many times as you like.
    scene.plot(x=[1, 2, 3, 4], y=[10, 15, 13, 17], mode="markers", type="scatter")
    scene.plot(x=[2, 3, 4, 5], y=[16, 5, 11, 9], mode="lines", type="scatter")
    scene.plot(x=[1, 2, 3, 4], y=[12, 9, 15, 12], mode="lines+markers", type="scatter")

    # Then to quickly see your graph, use the builtin microserver. Note that
    # this will block until you kill it with Control+C (keyboard interrupt).
    scene.preview()

    # To export to standalone HTML complete with the plotlyjs import and basic
    # HTML headers required to keep most browsers happy, use:
    html = scene.to_html(standalone=True)

    # Or to export to HTML suitable to be substituted into a larger HTML
    # document, simply omit the `standalone` option.
    html = scene.to_html()
    # Note that your HTML document will require the library import
    #   <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    # somewhere at the top in order for the graphs to materialize.

That's all there is to it. Happy plotting!


.. _`plotly's JavaScript API`: https://plotly.com/javascript/
.. _`plotly JavaScript library`: https://plotly.com/javascript/
