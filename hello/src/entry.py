from js import Response
import json

async def on_fetch(request, env):
    txt = await request.text()
    if not txt:
        return Response.new("body is empty!")
    
    try:
        data = json.loads(txt)
        
        if data.get("name"):
            return Response.new(f"Hello {data['name']}!")
        
        if data.get("left") and data.get("right"):
            return Response.new(f"{data['left']} + {data['right']} = {int(data['left']) + int(data['right'])}!")
    
    except:
        return Response.new("invalid value", status=00)

    return Response.new(data)
