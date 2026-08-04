import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

logging.info("Application Started")
logging.warning("Low Memory")
logging.error("Something Went Wrong")