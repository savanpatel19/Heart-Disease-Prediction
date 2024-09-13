import gradio as gr
import pickle as pkl

from sklearn.ensemble import RandomForestClassifier

model = pkl.load(open('model.pkl', 'rb'))




def predict(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    pred = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    pred = [float(i) if not i.isdigit() else i for i in pred]
    pred = model.predict([pred])
    return "High risk of Heart disease" if pred[0]==1 else "Low risk of Heart disease"

data_description = """
   age: age in years

    sex: sex (1 = male; 0 = female)

    cp: chest pain type
    - Value 0: typical angina
    - Value 1: atypical angina
    - Value 2: non-anginal pain
    - Value 3: asymptomatic

    trestbps: resting blood pressure (in mm Hg on admission to the hospital)
    chol: serum cholestoral in mg/dl

    fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)

    restecg: resting electrocardiographic results
    - Value 0: normal
    - Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
    - Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria

    thalach: maximum heart rate achieved

    exang: exercise induced angina (1 = yes; 0 = no)

    oldpeak = ST depression induced by exercise relative to rest

    slope: the slope of the peak exercise ST segment
    
    - Value 0: upsloping
    - Value 1: flat
    --Value 2: downsloping


    ca: number of major vessels (0-3) colored by flourosopy

    thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
    and the label

    condition: 0 = no disease, 1 = disease
"""



with gr.Blocks() as demo:
    gr.Label("Heartguard AI", size="xxl")
    gr.Markdown(data_description)

    age = gr.Textbox(label="Age")
    sex = gr.Textbox(label="Sex")
    cp = gr.Textbox( label="Chest Pain Type")
    trestbps = gr.Textbox(label="Resting Blood Pressure")
    chol = gr.Textbox(label="Serum Cholestoral in mg/dl")
    fbs = gr.Textbox(label="Fasting Blood Sugar > 120 mg/dl")
    restecg = gr.Textbox( label="Resting Electrocardiographic Results")
    thalach = gr.Textbox(label="Maximum Heart Rate Achieved")
    exang = gr.Textbox( label="Exercise Induced Angina")
    oldpeak = gr.Textbox(label="ST Depression Induced by Exercise Relative to Rest")
    slope = gr.Textbox( label="Slope of the Peak Exercise ST Segment")
    ca = gr.Textbox( label="Number of Major Vessels Colored by Flourosopy")
    thal = gr.Textbox(label="Thal")

    btn = gr.Button("Predict")
    out = gr.Textbox(label="Output Label")

    examples = gr.Examples(examples=[[69,1,0,160,234,1,2,131,0,0.1,1,1,0],[65,1,0,138,282,1,2,174,0,1.4,1,1,0],[63,1,0,145,233,1,2,150,0,2.3,2,0,1]],
                           inputs = [age, sex ,cp ,trestbps ,chol ,fbs ,restecg ,thalach ,exang ,oldpeak ,slope ,ca ,thal]
                           )

    btn.click(fn=predict, inputs=[age, sex ,cp ,trestbps ,chol ,fbs ,restecg ,thalach ,exang ,oldpeak ,slope ,ca ,thal],
               outputs=out)

demo.launch(share=True)
    

