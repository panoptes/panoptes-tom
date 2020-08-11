from django import template
from datetime import datetime, timedelta

from tom_observations.utils import get_sidereal_visibility

from plotly import offline
import plotly.graph_objs as go


register = template.Library()


@register.inclusion_tag("custom_tags/partials/visibility_params.html")
def visibility_params(target, facility, length=7, interval=60, airmass_limit=None):
    """
    Displays form and renders plot for visibility calculation. Using this templatetag to render a plot requires that
    the context of the parent view have values for start_time, end_time, and airmass.
    """

    visibility_graph = ""
    start_time = datetime.now()
    end_time = start_time + timedelta(days=length)

    visibility_data = get_sidereal_visibility(target, start_time, end_time, interval, airmass_limit)
    plot_data = [
        go.Scatter(x=data[0], y=data[1], mode="lines", name=site)
        for site, data in visibility_data.items()
    ]
    layout = go.Layout(
        title="Visibility Over Time",
        title_x=0.5,
        titlefont=dict(size=18),
        xaxis=dict(title="Time (UTC)", titlefont=dict(size=16)),
        yaxis=dict(title="Airmass", titlefont=dict(size=16), autorange="reversed"),
    )
    visibility_graph = offline.plot(
        go.Figure(data=plot_data, layout=layout), output_type="div", show_link=False
    )

    return {"visibility_graph": visibility_graph}

