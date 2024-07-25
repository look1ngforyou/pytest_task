import logging
import os


def setup_logging():
    try:
        # Ensure the directory for the log file exists
        log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
        print(f"Log directory is: {log_dir}")  # Debugging statement

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            print(f"Created log directory: {log_dir}")  # Debugging statement
        else:
            print(f"Log directory already exists: {log_dir}")  # Debugging statement

        log_path = os.path.join(log_dir, 'logs.log')
        print(f"Log file will be created at: {log_path}")  # Debugging statement

        logging.basicConfig(
            filename=log_path,
            level=logging.INFO,
            filemode="w",
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        logging.info("Logging is configured.")
    except Exception as e:
        print(f"Error setting up logging: {e}")