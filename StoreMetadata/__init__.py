import azure.functions as func
import logging

def main(metadata: dict, outputTable: func.Out[func.SqlRow]):
    logging.info("Writing metadata to SQL...")

    outputTable.set(
        func.SqlRow({
            "file_name": metadata.get("file_name"),
            "file_size_kb": metadata.get("file_size_kb"),
            "width": metadata.get("width"),
            "height": metadata.get("height"),
            "format": metadata.get("format")
        })
    )
