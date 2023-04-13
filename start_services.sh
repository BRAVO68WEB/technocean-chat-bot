cd app/
# Start rasa server with nlu model
rasa run --model models --enable-api --cors "*" --debug \
          -p 8000