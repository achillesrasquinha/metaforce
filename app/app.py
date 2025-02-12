import upyog as upy

from aws_cdk import (
    App,
    Stack,
    aws_lambda as _lambda,
)

CONST = {
    "NAME": "meta",
}
CONST["PREFIX"] = upy.upper(CONST["NAME"])

PATH = {
    "BASE": upy.pardir(__file__),
}
PATH["APP"] = upy.join2(PATH["BASE"], "app", path = True)

class MetaStack(Stack):
    def __init__(self, *args, **kwargs):
        super_ = super(MetaStack, self)
        super_.__init__(*args, **kwargs)

        prefix = CONST["PREFIX"]

        self.handler = _lambda.DockerImageFunction(
            self, f"{prefix}Handler",
            code = _lambda.DockerImageCode.from_image_asset(
                PATH["APP"],
            )
        )

app = App()
MetaStack(app, "MetaStack")
app.synth()