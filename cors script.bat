call activate rasa-hbl-dem
timeout 1
rasa run --credentials ./credentials.yml  --enable-api --auth-token XYZ123 --model ./models --endpoints ./endpoints.yml --cors "*"

::PAUSE >null
