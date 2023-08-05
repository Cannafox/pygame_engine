from src.config_manager import config_manager
from src.application import application

def main():
    print("Initialization...")
    config = config_manager.ConfigManager()

    print("Starting application...")
    app = application.Application(config)

    app.run()


if __name__ == "__main__":
    main()
