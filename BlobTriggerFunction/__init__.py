import logging
import azure.functions as func
import azure.durable_functions as df

def main(blob: func.InputStream, starter: str):
    client = df.DurableOrchestrationClient(starter)
    instance_id = client.start_new("OrchestratorFunction", None, {
        "path": blob.name
    })

    logging.info(f"Started orchestration with ID = '{instance_id}'.")
