
"""APP ENV"""
export FLASK_APP=app
export FLASK_ENV='development'
export FLASK_DEBUG=true

""" DATABSE ENV """
export DATABASE_URL='postgres://ohimydbamxhozq:4874b53b0e2a0403128a5f871f3007ea9e90c04c5f0c7590b24ae6b60ef1cfb1@ec2-63-32-7-190.eu-west-1.compute.amazonaws.com:5432/d59sliljil0g1o' # this only for developing
export DATABASE_TRACK_MODIFICATIONS=true

"""AUTH ENV"""
export AUTH0_DOMAIN="fax.us.auth0.com"
export ALGARITHMS="RS256"
export API_AUDIENCE="agency"

"""TOKENS MUST REUIREED!"""
export PRODCUER_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpYdEhxdFY2S3B3UzhVMGFHRFRocCJ9.eyJpc3MiOiJodHRwczovL2ZheC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE0NGEzZGQ3NTczNjQwMDZhMDllYzY1IiwiYXVkIjoiYWdlbmN5IiwiaWF0IjoxNjMyMDM0MjU0LCJleHAiOjE2MzIwNDE0NTQsImF6cCI6Imw0WnFqWjdCM3Z0cUprckEzZlU1d2J3M2NLWGd5SjhrIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.Ac_FwUQO3I56ksEitG858mCIemhHWK3I9I_HunlZQEphvY4MmIAHw5yzYgQQO-hDLlDzPyV5PaNXEOCTtAn63fLgZqzm8oqKq2-EUu36SlrJBcW5-tQS6pB7ndMJ8bNSOw23xVG3OOc7KmVHy3i2YADi2YszVQ5eCzcudgkRvfieYJssTD8RafExgZQhw7RBTQFriHwQ2ZC3I5rvu1uA5X4DFk1pQ29i2JXJH6eF9Jz4f02e8isLNGWLXUagyToNwv6Y2kbUFkZrodQdNl8O35wjqpTuD03LJX5ZVem-u8p8y7Pjhq6mEXJmaG4j4DxAgOsxLmjZkKuvDZyOaLXPjg"
export DIRECTOR_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpYdEhxdFY2S3B3UzhVMGFHRFRocCJ9.eyJpc3MiOiJodHRwczovL2ZheC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE0NDgzZTYwMDU3NGYwMDcwMTI4MmMxIiwiYXVkIjoiYWdlbmN5IiwiaWF0IjoxNjMyMDM0MTcxLCJleHAiOjE2MzIwNDEzNzEsImF6cCI6Imw0WnFqWjdCM3Z0cUprckEzZlU1d2J3M2NLWGd5SjhrIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.TMgiWZuE2d0HZb-FKungReUxvoHKhvlrTsOIyaWroYeXogGJakYpKQpc7hQbTCsp2shRKYjZcxeozBlh74B8inje9eJ-3Nq5jN4ySjGwcKbdu8Kaell263z-GQWdPpxlPzX_mrznjEULfUTSAG97z9NdN9LOdARBck4EPHibAHoRotEteNtGwqpbxlZV0kCTFxwr6Lyi-llNt0baJuDFoasgWkAhXDtOfB4nJaI334duO_qMMB7fySiGXlveeqxksFTh9wMXv9XIp40D3kZbCHSwWJPeNKCT89d2rbcrIYN6dYCC03WrWY-H9J3_BUEInfSso6a5rnhOuc03cQJVkQ"