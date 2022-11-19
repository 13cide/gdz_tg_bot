import zipfile


def create_zip(images, out):
    with zipfile.ZipFile(f'zip/{out}.zip', mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in images:
            zf.write(file)
    print(f'zip/{out}.zip')
