from app import create_app

app = create_app()  #Create the app instance

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  #  This works for direct execution
