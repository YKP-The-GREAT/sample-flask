from flask import Flask
from flask_restful import Resource, Api, reqparse

import json

 
import ast  ### for string to dict

# Create app object(instance) from Flask library
app = Flask(__name__)


# Create api object using flask-app pbject
api = Api(app)



class ParkingLots(Resource):

	def get(self):

		# Exract the information from Query params
		parser = reqparse.RequestParser()
		parser.add_argument('location', location="json")
		attached_info = parser.parse_args()

		# Get the data from DB
		with open("parkinglots_data.json") as f:
			data = json.load(f)

		user_requested_location = attached_info["location"]
		parkinglots = data[user_requested_location]

		# Generate response
		response = {
			"msg": "OK",
			"data": parkinglots
		}

		return response

	def post(self):
        
        # Exract the information from Query params
		parser = reqparse.RequestParser()
		parser.add_argument('location', location="json")
		parser.add_argument('parkinglots', location="json")
		attached_info = parser.parse_args()   
		loc = attached_info["location"]
		park = attached_info["parkinglots"]
		# new_info = {loc: park}

		# Get the data from DB
		with open("parkinglots_data.json") as f:
			data = json.load(f)

		# Adding new loc and park to the dictionary
		data[loc] = ast.literal_eval(park)

		# Push the data to DB
		with open("parkinglots_data.json", "w") as f:
			json.dump(data, f, indent = 4)

        
		# Generate Response
		response = {
			"msg": "Added",
			# loc: park
			"data": data
			# "parkinglots": park
			}
    
		return response

	def put(self):
		# Exract the information from Query params
		parser = reqparse.RequestParser()
		parser.add_argument('location', location="json")
		parser.add_argument('parkinglots', location="json")
		attached_info = parser.parse_args()   
		loc = attached_info["location"]
		park = attached_info["parkinglots"]
		# new_info = {loc: park}

		# Get the data from DB
		with open("parkinglots_data.json") as f:
			data = json.load(f)

		# Update loc for new park to the dictionary
		data[loc] = ast.literal_eval(park)

		# Push the data to DB
		with open("parkinglots_data.json", "w") as f:
			json.dump(data, f, indent = 4)
        
		# Generate Response
		response = {
			"msg": "Updated",
			# loc: park
			"data": data
			# "parkinglots": park
			}
    
		return response

	def patch(self):
		# Exract the information from Query params
		parser = reqparse.RequestParser()
		parser.add_argument('location', location="json")
		parser.add_argument('parkinglots', location="json")
		attached_info = parser.parse_args()   
		loc = attached_info["location"]
		park = attached_info["parkinglots"]
		# new_info = {loc: park}

		# Get the data from DB
		with open("parkinglots_data.json") as f:
			data = json.load(f)

		# Checking loc

		# If park exist: remove park from the loc's list
		if(park in data[loc]):
			data[loc].remove(park)

		# If new park: add park to the loc's list
		elif(park not in data[loc]):
			data[loc].append(park)


		# Push the data to DB
		with open("parkinglots_data.json", "w") as f:
			json.dump(data, f, indent = 4)
        
		# Generate Response
		response = {
			"msg": "Updated differently",
			# loc: park
			"data": data
			# "parkinglots": park
			}
    
		return response

	def delete(self):
		# Exract the information from Query params
		parser = reqparse.RequestParser()
		parser.add_argument('location', location="json")
		attached_info = parser.parse_args()   
		loc = attached_info["location"]

		# Get the data from DB
		with open("parkinglots_data.json") as f:
			data = json.load(f)

		# Deleting dictionary[loc]
		del data[loc]

		# Push the data to DB
		with open("parkinglots_data.json", "w") as f:
			json.dump(data, f, indent = 4)
        
		# Generate Response
		response = {
			"msg": "Deleted",
			# loc: park
			"data": data
			# "parkinglots": park
			}
    
		return response


class ParkingLots_v2(Resource):

	def get(self, location):

		# Get the data from DB
		with open("parkinglots_data.json") as f:
			data = json.load(f)

		parkinglots = data[location]

		# Generate response
		response = {
			"msg": "OK",
			"data": parkinglots
		}

		return response




api.add_resource(ParkingLots, '/api/parkinglots')
api.add_resource(ParkingLots_v2, '/api/parkinglots/<string:location>')


# Run the flask-app server
if __name__ == "__main__":
	app.run(debug=True)









'''
Exercise:

	Add new parking lots

		URL: localhost:5000/api/parkinglots POST

		Input(JSON):
		{
		    "parkinglot": {
		        "austin": ["austin main str", "austin suburb"]
		    }
		}

	Update parking lots

		URL: localhost:5000/api/parkinglots PUT

			Input(JSON):
			{
			    "parkinglot": {
			        "austin": []
			    }
			}

	Delete parking lots

		URL: localhost:5000/api/parkinglots/sfo DELETE



-----
Understanding

	Url (GET/DELETE): Read or Delete resource
		- Query Params
		- e.g. localhost/api/parkinglot/123450

	Body (POST/PUT/PATCH): Create or Update the resource
		- Raw data (Text/Json)
		- form-data
			e.g.
				name => Alex
				email => alex@g.com 



'''
















