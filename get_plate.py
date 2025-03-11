import boto3
import csv
import random
import json

# S3 setup
BUCKET_NAME = "liscensedb"  
CSV_FILE_KEY = "liscense.csv"  

s3 = boto3.client("s3")

def lambda_handler(event, context):
    try:
        # Download CSV file from S3
        response = s3.get_object(Bucket=BUCKET_NAME, Key=CSV_FILE_KEY)
        lines = response["Body"].read().decode("utf-8").splitlines()
        
        # Read CSV into a list of dictionaries
        reader = csv.DictReader(lines)
        data = list(reader)

        # Ensure there's data before selecting a row
        if not data:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "CSV file is empty or unreadable."}),
                "headers": {"Content-Type": "application/json"},
            }

        # Pick a random row
        random_row = random.choice(data)

        # Extract only the required fields
        plate = random_row.get("plate", "").strip()
        customer_meaning = random_row.get("customer_meaning", "").strip()
        reviewer_comments = random_row.get("reviewer_comments", "").strip()
        status = random_row.get("status", "").strip()

        # Manually construct the JSON response
        json_output = f'{{"plate": "{plate}", "customer_meaning": "{customer_meaning}", "reviewer_comments": "{reviewer_comments}", "status": "{status}"}}'

        # Return JSON response
        return {
            "statusCode": 200,
            "body": json_output,
            "headers": {"Content-Type": "application/json"},
        }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {"Content-Type": "application/json"},
        }
