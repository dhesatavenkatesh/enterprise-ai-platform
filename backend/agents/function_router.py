import time


class FunctionRouter:

    def __init__(self):
        self.functions = {}

    # -------------------------
    # Register Function
    # -------------------------
    def register(self, name, func):
        self.functions[name] = func

    # -------------------------
    # Execute Function
    # -------------------------
    def execute(self, function_name, **kwargs):

        if function_name not in self.functions:
            return {
                "status": "Failed",
                "message": f"{function_name} not registered"
            }

        start = time.time()

        try:
            result = self.functions[function_name](**kwargs)

            execution_time = round(time.time() - start, 4)

            return {
                "status": "Success",
                "function": function_name,
                "execution_time": execution_time,
                "result": result
            }

        except Exception as e:
            return {
                "status": "Failed",
                "error": str(e)
            }