# grpc-asgiref

This repo is a test case for the thread handling of asgiref `sync_to_async`
under `grpc.aio.server`, related to this bug: https://github.com/django/asgiref/issues/214

# Testing

Install dependencies, either with `pip install -r requirements.txt` or `poetry install`.

Run pytest. With poetry:
```
poetry run pytest
```

Without poetry, activate your virtual environment, then:
```
pytest
```

With asgiref v3.5.0, the current thread under which a `sync_to_async`-decorated method runs is `"ThreadPoolExecutor-0_0"`, when it should be `"MainThread"`.

