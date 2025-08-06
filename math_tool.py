from agents import FunctionTool, RunContextWrapper
from math_tool_schema import PlusSchema, SubtractSchema, MultilpicationSchema, DivisionSchema

async def check_is_teacher(ctx: RunContextWrapper, agent):
    return ctx.context.get('role') == 'teacher'

async def plus_function(ctx:RunContextWrapper, arg):
    obj = PlusSchema.model_validate_json(arg)
    return f"Your Answer is {obj.n1 + obj.n2}"

async def subtract_function(ctx: RunContextWrapper, arg):
    obj = SubtractSchema.model_validate_json(arg)
    return f"Answer: {obj.n1 - obj.n2}"

async def multiplication_function(ctx: RunContextWrapper, arg):
    obj = MultilpicationSchema.model_validate_json(arg)
    return f"Answer: {obj.n1 * obj.n2}"

async def division_function(ctx: RunContextWrapper, arg):
    obj = DivisionSchema.model_validate_json(arg)
    return f"Answer: {obj.n1 / obj.n2}"

plus_tool = FunctionTool(
    name="plus",
    description="Adds two numbers",
    params_json_schema=PlusSchema.model_json_schema(),
    on_invoke_tool=plus_function,
    is_enabled=check_is_teacher
)

subtract_tool = FunctionTool(
    name="subtract",
    description="Subtracts second number from first",
    params_json_schema=SubtractSchema.model_json_schema(),
    on_invoke_tool=subtract_function,
    is_enabled=check_is_teacher
)

multiplication_tool = FunctionTool(
    name="multiply",
    description="Multiplies two numbers",
    params_json_schema=MultilpicationSchema.model_json_schema(),
    on_invoke_tool=multiplication_function,
    is_enabled=check_is_teacher
)

division_tool = FunctionTool(
    name="divide",
    description="Divides first number by second",
    params_json_schema=DivisionSchema.model_json_schema(),
    on_invoke_tool=division_function,
    is_enabled=check_is_teacher
)

