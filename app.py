import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import numpy as np

mob_mon = pd.read_csv("training.csv")
mob_mon = mob_mon.drop(["ID"], axis=1)

mob_mon = mob_mon.rename(
    columns={
        "Q1": "age",
        "Q2": "gender",
        "Q3": "marital_status",
        "Q6": "land_ownership",
        "Q13": "mobile_money_usage",
    }
)


mob_mon_incomes = mob_mon[
    [
        "Q8_1",
        "Q8_2",
        "Q8_3",
        "Q8_4",
        "Q8_5",
        "Q8_6",
        "Q8_7",
        "Q8_8",
        "Q8_9",
        "Q8_10",
        "Q8_11",
    ]
]

income_type = {
    "Q8_1": "salaries",
    "Q8_2": "trading",
    "Q8_3": "service",
    "Q8_4": "piece_work",
    "Q8_5": "rental_income",
    "Q8_6": "interest",
    "Q8_7": "pension",
    "Q8_8": "social_welfare",
    "Q8_9": "rely_on_someone",
    "Q8_10": "dont_get_money",
    "Q8_11": "other",
}


mob_mon = mob_mon.rename(
    columns={
        "Q8_1": "salaries",
        "Q8_2": "trading",
        "Q8_3": "service",
        "Q8_4": "piece_work",
        "Q8_5": "rental_income",
        "Q8_6": "interest",
        "Q8_7": "pension",
        "Q8_8": "social_welfare",
        "Q8_9": "rely_on_someone",
        "Q8_10": "dont_get_money",
        "Q8_11": "other",
    }
)
mob_mon.gender = ["male" if each == 1 else "female" for each in mob_mon.gender]
mob_mon["Age_by_decades"] = mob_mon.age.apply(lambda x: int(x / 10) * 10)

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    children=[
        html.H1(children="Financial Services in Tanzania"),
        html.Div(
            children="""
        Dash: In this Dashboard I aim to inform the user of the financial services in 
        Tanzania, on how the populations access financial sercives through the usage of 
        mobile money and also look at their demographics and how they earn their money.
                    """
        ),
        dcc.Graph(
            id="ages",
            figure={
                "data": [
                    {
                        "x": mob_mon["Age_by_decades"],
                        "y": mob_mon["mobile_money"] == 0,
                        "type": "bar",
                        "name": "without mobile money",
                    },
                    {
                        "x": mob_mon["Age_by_decades"],
                        "y": mob_mon["mobile_money"] == 1,
                        "type": "bar",
                        "name": "with mobile money",
                    },
                ],
                "layout": {"title": "Ages on Mobile Money"},
            },
        ),
        dcc.Graph(
            id="classification",
            figure={
                "data": [
                    {
                        "x": mob_mon["Age_by_decades"],
                        "y": mob_mon["mobile_money_classification"] == 0,
                        "type": "bar",
                        "name": "No income and MM",
                    },
                    {
                        "x": mob_mon["Age_by_decades"],
                        "y": mob_mon["mobile_money_classification"] == 1,
                        "type": "bar",
                        "name": "no MM but has income",
                    },
                    {
                        "x": mob_mon["Age_by_decades"],
                        "y": mob_mon["mobile_money_classification"] == 2,
                        "type": "bar",
                        "name": "Has MM",
                    },
                    {
                        "x": mob_mon["Age_by_decades"],
                        "y": mob_mon["mobile_money_classification"] == 3,
                        "type": "bar",
                        "name": "MM Plus",
                    },
                ],
                "layout": {"title": "Mobile Money Classification"},
            },
        ),
        dcc.Graph(
            id="gender",
            figure={
                "data": [
                    {
                        "x": mob_mon["gender"],
                        "y": mob_mon["mobile_money"] == 0,
                        "type": "bar",
                        "name": "without mobile money",
                    },
                    {
                        "x": mob_mon["gender"] == 2,
                        "y": mob_mon["mobile_money_classification"] == 0,
                        "type": "bar",
                        "name": "with mobile money",
                    },
                    {
                        "x": mob_mon["gender"],
                        "y": mob_mon["mobile_money"] == 1,
                        "type": "bar",
                        "name": "without mobile money",
                    },
                    {
                        "x": mob_mon["gender"] == 2,
                        "y": mob_mon["mobile_money_classification"] == 1,
                        "type": "bar",
                        "name": "with mobile money",
                    },
                ],
                "layout": {"title": "Gender on Mobile Money"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
