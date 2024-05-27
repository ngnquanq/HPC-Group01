from pydantic import BaseModel

class CatDogResponse(BaseModel):
    """
    This class is used to create a CatDogResponse object for the FastAPI app.
    It contains the probabilities of the predictions.
    """
    probs: list = []
    best_prob: float = -1.0
    predicted_id: int = -1
    predicted_class: str = ""
    predictor_name: str = ""

