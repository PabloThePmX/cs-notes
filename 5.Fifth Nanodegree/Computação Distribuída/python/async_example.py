import asyncio
import time

async def task_one_async():
    print("Iniciando primeira tarefa")
    await asyncio.sleep(2)
    print("Primeira tarefa concluida")
    return "Resultado da primeira tarefa"

async def task_two_async():
    print("Iniciando segunda tarefa")
    await asyncio.sleep(3)
    print("Segunda tarefa concluida")
    return "Resultado da segunda tarefa"

async def main_async():
    start_time = time.time()

    results = await asyncio.gather(
        task_one_async(),
        task_two_async()
    )

    end_time = time.time()
    print(f"Tempo total: {end_time - start_time:.2f}s")
    return results

asyncio.run(main_async())