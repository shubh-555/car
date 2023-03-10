import json
import pickle
import numpy as np


class car_price ():

    def __init__(self,data):
        self.data=data


    def loading_files(self):
        with open('artifacts/car_info.json','r') as file:
            self.car_info=json.load(file)

        with open('artifacts/car_prise_pred.pkl','rb') as file:
            self.car_model=pickle.load(file)   



    def price_prediction(self):
        self.loading_files()

        Year = self.data['html_year']
        Present_Price = self.data['html_Present_Price']
        Kms_Driven = self.data['html_Kms_Driven']
        FUEL = self.data['html_fuel_type']
        TYPE_OF_SELLER = self.data['html_seller_type']
        TRANSMISSION_TYPE = self.data['html_trasmission']
        Owner = self.data['html_owner']

        Fuel_Type = self.car_info["Fuel_Type"][FUEL]
        Seller_Type = self.car_info["Seller_Type"][TYPE_OF_SELLER]
        Transmission = self.car_info["Transmission"][TRANSMISSION_TYPE]



        user_data=np.zeros(len(self.car_info['column_name']))

        user_data[0]= Year
        user_data[1]= Present_Price
        user_data[2]= Kms_Driven
        user_data[3]= Fuel_Type
        user_data[4]= Seller_Type
        user_data[5]= Transmission
        user_data[6]= Owner

        result=self.car_model.predict([user_data])[0]
        

        return result
     


            