import numpy as np
import pickle 
import streamlit as st

# loading the saved model 
loaded_model = pickle.load(open('C:/Users/Lenovo/Documents/Minor project/trained_model.sav','rb')) 

#creating a function for prediction

def price_prediction(input_data):
    
    input_data_as_arr =  np.asarray(input_data)

    #reshape the array
    input_data_reshape = input_data_as_arr.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshape)
    
    return prediction[0]  
        
    #changing input data to numpy array
    input_data_as_arr = np.asarray(input_data)

    #reshape the array
    input_data_reshape = input_data_as_arr.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshape)
    
    return prediction[0] 


def main():
    
    # giving a title
    st.title('House Price Prediction')
    
    OverallQual = st.number_input('Overall quality',step=1)
    YearBuilt = st.number_input('Year Built',step=1)
    YearRemodAdd = st.number_input('Year of renovation',step=1)
    BsmtFinSF = st.number_input('Basement Area')
    firstFlrSF = st.number_input('First Floor Area')
    GrLivArea = st.number_input('Ground Living Area')
    FullBath = st.number_input('No of Full Bath',step=1)
    TotRmsAbvGrd = st.number_input('Total Rooms above ground',step=1)
    Fireplaces = st.number_input('No of Fireplaces',step=1)
    GarageArea = st.number_input('Garage Area')
  
    
  
    # code for prediction
    price = ''
    
    #creating a button for prediction 
    if st.button('House Price Predict'):
        price = price_prediction([OverallQual, YearBuilt, YearRemodAdd, BsmtFinSF, firstFlrSF, GrLivArea, FullBath, 
                                  TotRmsAbvGrd, Fireplaces, GarageArea])

        rounded_price = round(price, 2)
        st.success(f'Rs{price:.2f}')
        
        
if __name__ == '__main__':
    main() 

