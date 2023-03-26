from flask import jsonify
from google.cloud import bigquery

def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    if request.method == 'OPTIONS':
        headers['Access-Control-Allow-Methods'] = 'POST'
        headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return ('', 204, headers)
    else:
        request_json = request.get_json()

    
        # Replace with your project ID and view ID
        project_id = 'burner-manchoud1'
        view_id = 'bbb_hackathon_data.VW_DRIVER_CURATED_DETAILS'

        # Create a BigQuery client object
        client = bigquery.Client()

        # Construct the query
        query = f"""
            SELECT *
            FROM `{project_id}.{view_id}`
            where Customer_ID= "{request_json["Customer_ID"]}"
        """
        print(query)
        
        # Execute the query
        query_job = client.query(query)

        # Convert the results to a list of dictionaries
        results = []
        for row in query_job:
            results.append(dict(row.items()))



        # Return the results as a JSON string
        try:
            headers = {
                'Access-Control-Allow-Origin': '*'
            }
            return {'response': results[0],"message":"success"},200,headers
        except:
            return {"message":"error"},500
        
