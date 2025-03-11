This site hosts a database of real California vanity plate applications from 2015–2016, including the applicant’s reasoning and a DMV reviewer’s comments. Each plate was either approved or rejected, offering a glimpse into what people tried to put on their cars and how the DMV ruled on them.

The custom RESTful API powering the site runs on AWS, leveraging S3 for storage/hosting, Lambda for processing, API Gateway for request handling, CloudFront for HTTPS, and WAF for throttling the API. You can call it if you want (max five calls per second), but there’s really no reason to—it just serves up this weird little slice of bureaucratic decision-making at scale.

Call the API: GET @ https://fqu0j94n59.execute-api.us-east-2.amazonaws.com/Running 
