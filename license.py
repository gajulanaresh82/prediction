import streamlit as st
import numpy as np
import pandas as pd



import pickle


from sklearn.metrics import confusion_matrix,accuracy_score,classification_report,f1_score,ConfusionMatrixDisplay








model=pickle.load(open(r"C:\Users\Keyush\Desktop\research python\Projects\License status prediction\licprediction.pkl",'rb'))




def make_prediction(city,state,license_description,license_number,application_type,conditional_approval,ssa,latitude,longitude,completion_to_start,start_to_expiry,approval_to_issuance,completion_to_payment):

    # Prepare input data
    input_data = np.array([city,state,license_description,license_number,application_type,conditional_approval,ssa,latitude,longitude,completion_to_start,start_to_expiry,approval_to_issuance,completion_to_payment]).reshape(1, -1)

    # Predict with the loaded model
    prediction = model.predict(input_data)
    if prediction==0:
        return 'license  is cancelled'
    elif  prediction == 1:
        return 'license is issued'
    elif  prediction == 2:
        return 'license is in inquiry'
    elif  prediction ==3:
        return 'license is revoked'
    else:
        return 'license  is revoked and appealed'
        
      
    
# Main function to run the Streamlit app
def main():
    st.title("License Status Prediction App")
    st.header("Enter the below details to know  the status")
    

    city = st.number_input("city", value=0.0)
    state = st.number_input("state", value=0.0)
    license_description = st.number_input("license_description", value=0.0)
    license_number = st.number_input("license_number", value=0.0)
    application_type = st.number_input("application_type", value=0.0)
    conditional_approval = st.number_input("conditional_approval", value=0.0)
    ssa= st.number_input("ssa", value=0.0)
    latitude = st.number_input("latitude", value=0.0)
    longitude = st.number_input("longitude", value=0.0)
    completion_to_start = st.number_input("completion_to_start", value=0.0)
    start_to_expiry  = st.number_input("start_to_expiry ", value=0.0)
    approval_to_issuance = st.number_input("approval_to_issuance", value=0.0)
    completion_to_payment= st.number_input("completion_to_payment", value=0.0)
    

    if st.button("Predict"):
        prediction = make_prediction(city,state,license_description,license_number,application_type,conditional_approval,ssa,latitude,longitude,completion_to_start,start_to_expiry,approval_to_issuance,completion_to_payment)
        st.write("Prediction:", prediction)
        
    

if __name__ == "__main__":
    main()