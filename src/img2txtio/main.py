import requests
from typing import Final
import os
import time
import json

class Img2TxtClient:
    def __init__(self, api_key: str):
        self._base_url: Final[str] = "https://img2txt.io/api/"
        self._headers = {"Authorization": f"Bearer {api_key}"}

    def _get_upload_url(self, file_path: str) -> dict:
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        url = f"{self._base_url}get-upload-url?name={file_name}&size={file_size}"
        resp = requests.get(url, headers=self._headers)
        resp.raise_for_status()
        data = resp.json()
        if "url" not in data or "key" not in data:
            raise RuntimeError(f"Invalid upload-url response: {resp.text}")
        return data

    def _upload_file(self, upload_url: str, file_path: str) -> str:
        file_name = os.path.basename(file_path)
        with open(file_path, "rb") as f:
            files = {"file": (file_name, f)}
            resp = requests.put(upload_url, files=files)
        resp.raise_for_status()
        data = resp.json()
        if "ufsUrl" not in data:
            raise RuntimeError(f"Invalid upload response: {resp.text}")
        return data["ufsUrl"]

    def _image_to_text(self, image_url: str, output_type: str = "raw", description: str = "", outputStructure: str = "") -> dict:
        url = f"{self._base_url}image-to-text"
        payload = {"imageUrl": image_url, "outputType": output_type}
        if description:
            payload["description"] = description
        if outputStructure:
            try:
                parsed = json.loads(outputStructure)
            except json.JSONDecodeError as e:
                raise ValueError(f"outputStructure must be valid JSON: {e}")
            payload["outputStructure"] = parsed
        headers = {**self._headers, "Content-Type": "application/json"}
        resp = requests.post(url, headers=headers, json=payload)
        resp.raise_for_status()
        data = resp.json()
        if not data.get("success", True):
            raise RuntimeError(f"Processing failed: {data}")
        return data

    def process(self, image_path: str, output_type: str = "raw", description: str = "", outputStructure: str = "") -> dict:
        """
        Access img2txt.io's API to process an image file to text.
        """
        if not os.path.isfile(image_path):
            raise FileNotFoundError(f"File not found: {image_path}")

        upload_info = self._get_upload_url(image_path)
        upload_url = upload_info["url"]
        ufs_url = self._upload_file(upload_url, image_path)
        time.sleep(0.2)
        return self._image_to_text(ufs_url, output_type, description, outputStructure)
