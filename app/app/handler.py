import upyog as upy

def handle(event, context):
    response = upy.Response()

    try:
        pass
    except Exception as e:
        response.set_error(
            upy.Response.INTERNAL_SERVER_ERROR,
            str(e),
        )

    return response.json()