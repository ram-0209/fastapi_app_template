"""
    common json response structure
"""
from src.config.http_status_codes import HttpStatusCodes
from src.dto.response_dto import Response


def create_response(message: str, status: str, data: str = None):
    """function for mapping the response

    Args:
        message (str): _description_
        status (str): _description_
        data (str, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    final_response = Response()
    final_response.message = message
    final_response.status = status
    final_response.data = data
    return final_response


def create_api_response(
    success: bool, result=None, success_message=None, failure_message=None
):
    """Function for API Response

    Args:
        success (bool): _description_
        result (_type_, optional): _description_. Defaults to None.
        success_message (_type_, optional): _description_. Defaults to None.
        failure_message (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    if success:
        status_code = HttpStatusCodes.StatusCodes.SUCCESS_OK_200
        status_description = (
            success_message
            if success_message
            else HttpStatusCodes.StatusCodesDescription.SUCCESS_OK_200
        )
    else:
        status_code = HttpStatusCodes.StatusCodes.NOT_FOUND_404
        status_description = (
            failure_message
            if failure_message
            else HttpStatusCodes.StatusCodesDescription.NOT_FOUND_404
        )

    return create_response(status_description, status_code, result)
