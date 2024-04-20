import asyncio
import httpx
from django.http import HttpResponse

async def http_call_async():
  
  #imprimindo números de 1 a 5 um por segundo para simular async
  for num in range(1,6):
    await asyncio.sleep(1)
    print(num)
  async with httpx.AsyncClient() as client:
    r = await client.get("https://httpbin.org")
    print(r)

async def async_view(request):
  
  #chama o event loop
  loop = asyncio.get_event_loop()
  
  #cria a task 
  loop.create_task(http_call_async())
  return HttpResponse("Non blocking http request")

def http_call_sync():
  for num in range(1,6):
    asyncio.sleep(1)
    print(num)
  r = httpx.get("https://httpbin.org")
  print(r)

def sync_view(request):
  http_call_sync()
  return HttpResponse("Blocking http request")