"""
    common json response structure
"""
from src.dto.response_dto import Response


def create_response(message: str, status: str, data: str = None):
    """
    function for mapping the response
    """
    final_response = Response()
    final_response.message = message
    final_response.status = status
    final_response.data = data
    return final_response
