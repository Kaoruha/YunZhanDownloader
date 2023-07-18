from PIL import Image

out_dir = "output"

# Gen PDF
l = []
index = 1
while True:
    try:
        path = f"{out_dir}/{index}.jpg"
        print(f"Reading {path}", end="\r")
        o = Image.open(path)
        l.append(o)
        # o.save("./Halo.pdf", "pdf", save_all=True, append_images=l[1:])
        index += 1
    except Exception as e:
        break
l[0].save("./Halo.pdf", "pdf", save_all=True, append_images=l[1:])
