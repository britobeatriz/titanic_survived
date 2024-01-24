# libs
import gradio as gr
import joblib as jb


def predict(Sex, Age, Pclass):
    # valores = pd.DataFrame({
    #     "Sex":[Sex],
    #     "Age":[Age],
    #     "Pclass":[Pclass]
    # })
    mdl = jb.load('model.pk1')
    
    if Pclass == 'A':
        Pclass = 1
    elif Pclass == 'B':
        Pclass = 2
    else: 
        Pclass = 3

    pred = mdl.predict_proba([[Sex,Age,Pclass]])[0]
    return {"Did not survive:" + pred[0]+ "survived:" + pred[1]}

demo = gr.Interface(
    fn=predict,
    inputs=[gr.Dropdown(['male','female'], type="index"),gr.Number(value=0),gr.Dropdown(['A','B','C'], type="index")],
    outputs="label"
)

demo.launch()