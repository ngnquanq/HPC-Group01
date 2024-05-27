from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app):
    """
    This function sets up the CORS middleware for the FastAPI app.

    Parameters:
    - app (FastAPI): The FastAPI app to which the middleware will be added.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
