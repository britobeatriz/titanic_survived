import gradio as gr
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


data = pd.read_csv('train.csv')

X = data[["Sex","Age","Pclass"]].copy()
y = data["Survived"]

X["Sex"] =X["Sex"].map({"male":0, "female":1})
X = X.fillna(-1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)

mdl = DecisionTreeClassifier(random_state=0, min_samples_leaf=6)
mdl.fit(X_train, y_train)

p = mdl.predict(X_test)

def predict(Sex, Age, Pclass):
    valores = pd.DataFrame({
        "Sex":[Sex],
        "Age":[Age],
        "Pclass":[Pclass]
    })
    if mdl.predict(valores) == [0]:
        return "Não há chances de sobreviver"
    else: 
        return "Há chances de sobreviver"

listaDropdown = [1,2,3]

demo = gr.Interface(
    fn=predict,
    inputs=[gr.Number(value=0),gr.Number(value=0),gr.Dropdown(listaDropdown)],
    outputs=[gr.Text]
)