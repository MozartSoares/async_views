import asyncio
import httpx
from django.http import JsonResponse

async def http_call_async():
  async with httpx.AsyncClient() as client:
    response = await client.get(url='https://fake-api-tau.vercel.app/api/efood/restaurantes')
    restaurant_list = [restaurant for restaurant in response.json()]

    for restaurant in restaurant_list:
      await asyncio.sleep(1)
      print(restaurant['titulo'])

    
      r = await client.get("https://httpbin.org")
      print(r)

  return restaurant_list

async def async_view(request):
  
  #chama o event loop
  loop = asyncio.get_event_loop()
  
  restaurant_list = await loop.create_task(http_call_async())
  
  #cria a task 
  loop.create_task(http_call_async())
  return JsonResponse(restaurant_list, safe=False)