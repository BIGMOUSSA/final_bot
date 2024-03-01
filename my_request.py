import requests
import json
def send_request_and_store_result(query):
    # URL of the FASPI API endpoint you want to query
    faspi_url = "http://host.docker.internal:8000/predict"

    # Parameters to include in the request, if any
    data = {
        "text" : query
        # Add more parameters as needed
    }

    try:
        # Sending GET request to the FASPI API
        response = requests.post(faspi_url, json=data)

        # Checking if the request was successful (status code 200)
        if response.status_code == 200:
            # Assuming the response is JSON, you can parse it and store it
            result = response.json()

            # Store the result in a file, database, or any other desired storage
            print("Request successful. Result stored.")
            return result["answer"]
            #with open('faspi_result.json', 'w') as f:
            #    json.dump(result, f)

            
        else:
            print(f"Error: Failed to retrieve data. Status code: {response.status_code}")

    except requests.RequestException as e:
        print(f"Error: Failed to make request - {e}")

if __name__ == "__main__":
    query = "how was industy activity in 2022"
    send_request_and_store_result(query=query)
