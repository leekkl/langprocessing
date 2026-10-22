from shiny.express import input, ui
from shinywidgets import render_altair
import pandas as pd

ui.input_selectize("var", "Select variable", choices=["score_sci_avg", "score_math_avg, score_env_avg"])

@render_altair
def hist():
    import altair as alt
    from palmerpenguins import load_penguins
    df = pd.read_excel("PISA_dataset3_mean.xlsx")
    return (
        alt.Chart(df)
        .mark_bar()
        .encode(x=alt.X(f"{input.var()}:Q", bin=True), y="count()")
    )
