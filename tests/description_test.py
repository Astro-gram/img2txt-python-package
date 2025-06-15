from img2txtio import Img2TxtClient

client = Img2TxtClient(api_key="API_KEY_HERE")

result = client.process(
    output_type="description",
    description="give me a list of the destinations as strings",
    image_path="C:\\Users\\benwe\\Downloads\\plane2.png"
)

print("Result:", result)