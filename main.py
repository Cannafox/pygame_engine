from src.application import application

def main():
    print("Starting application...")
    app = application.Application()
    while app.run():
        print("a")


if __name__ == "__main__":
    main()
