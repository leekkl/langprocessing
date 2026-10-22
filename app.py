from shiny.express import input, ui
from shinywidgets import render_plotly
import pandas as pd

ui.input_selectize(
    "var", "Select variable",
    choices=["score_sci_avg", "score_math_avg", "score_env_avg"]
)

@render_plotly
def hist():
    import plotly.express as px
    df = pd.read_excel("PISA_dataset3_mean.xlsx")
    random.seed(100)
    df = df.sample(n=5000)
    return px.histogram(df, x=input.var())
