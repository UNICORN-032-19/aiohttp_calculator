from typing import Dict

import aiohttp_jinja2
import markdown2
from aiohttp import web
import json
from aiohttp_calculator.main.db_utils import save_result


@aiohttp_jinja2.template('index.html')
async def index(request: web.Request) -> Dict[str, str]:
    return {}


def get_result(string):
    result = "0"
    error = ""
    # elements = calc.prepare_data(string)
    try:
        # result = calc.calc(elements)
        result = eval(string)
    except ZeroDivisionError:
        error = "На ноль делить нельзя!"
    except UnknownOperation as error:
        error = "UnknownOperation"
    except UnknownError:
        error = "UnknownError!"
    return str(result), str(error)


async def compute(request: web.Request) -> web.Response:
    return_result = dict(
        string="0",
        error="",
    )
    post = await request.post()
    string = post.get("string", "").strip()
    if string.endswith("="):
        string = string.replace("=", "")
        result, error = get_result(string)
        if error:
            return_result.update({"error": error})
        else:
            return_result.update({"string": result})
    elif string.endswith("X^2"):
        string = string[:-3]
        error = ""
        try:
            float(string)
            result1 = string
        except ValueError:
            result1, error = get_result(string)

        try:
            if error:
                raise ValueError(error)
            result, error = get_result(result1 + "^2")
            if error:
               raise ValueError(error)
            return_result.update({"string": result})
        except ValueError as error:
            return_result.update({"error": error})
    else:
        return_result.update({"string": string})
    async with request.app["db"].acquire() as conn:
        await save_result(conn, string=string, res=return_result.get("string"), error=return_result.get("error"))
    return web.Response(text=json.dumps(return_result))


async def results(request):
    results = Result.objects.all()
    return render(request, 'results.html', context={"results": results})
