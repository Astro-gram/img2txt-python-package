from img2txtio import Img2TxtClient

client = Img2TxtClient(api_key="uki9iz0jvxaqp5uatxtri4jyvffxgorw")

result = client.process(
    output_type="structured",
    outputStructure='''
{
    "destinations": [
        ""
    ]
}
''',
    image_path="C:\\Users\\benwe\\Downloads\\plane2.png"
)

print("Result:", result)