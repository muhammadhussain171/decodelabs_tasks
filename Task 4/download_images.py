import os
from pathlib import Path
from urllib.request import urlretrieve


IMAGE_FOLDER = "images"

IMAGE_URLS = [
    "https://images.unsplash.com/photo-1552053831-71594a27632d",
    "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba",
    "https://images.unsplash.com/photo-1502877338535-766e1452684a",
    "https://images.unsplash.com/photo-1449824913935-59a10b8d2000",
    "https://images.unsplash.com/photo-1470770841072-f978cf4d019e",
    "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",
    "https://images.unsplash.com/photo-1494526585095-c41746248156",
    "https://images.unsplash.com/photo-1482192505345-5655af888cc4",
]


def download_images():
    """Download sample images automatically."""

    image_folder = Path(IMAGE_FOLDER)
    image_folder.mkdir(exist_ok=True)

    print("=" * 60)
    print("DOWNLOADING SAMPLE IMAGES")
    print("=" * 60)

    successful = 0

    for index, url in enumerate(IMAGE_URLS, start=1):

        filename = image_folder / f"image_{index}.jpg"

        try:
            print(f"\nDownloading image {index}...")

            urlretrieve(
                url,
                filename
            )

            print(
                f"Saved: {filename}"
            )

            successful += 1

        except Exception as error:

            print(
                f"Failed to download image {index}: "
                f"{error}"
            )

    print("\n" + "=" * 60)
    print("DOWNLOAD SUMMARY")
    print("=" * 60)

    print(
        f"Successfully downloaded: "
        f"{successful}/{len(IMAGE_URLS)}"
    )


if __name__ == "__main__":
    download_images()