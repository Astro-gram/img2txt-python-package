from img2txtio import Img2TxtClient


client = Img2TxtClient(api_key="API_KEY_HERE")

import concurrent.futures

def call_process():
    return client.process(
        output_type="raw",
        image_path="C:\\Users\\benwe\\Downloads\\plane2.png"
    )

with concurrent.futures.ThreadPoolExecutor() as executor:
    future1 = executor.submit(call_process)
    future2 = executor.submit(call_process)

    result1 = future1.result()
    result2 = future2.result()

print("1:", result1)
print("2:", result2)