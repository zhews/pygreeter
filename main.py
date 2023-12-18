from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from prometheus_client import make_asgi_app
import uvicorn

from greeter import greet

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
def get_greeting(name: str = "") -> str:
    output = greet(name)
    return output


metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

resource = Resource(attributes={SERVICE_NAME: "pygreeter"})
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="jaeger:4317", insecure=True))
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)


FastAPIInstrumentor.instrument_app(app)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
