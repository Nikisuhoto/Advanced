import os
from PIL import Image, ImageTk
import json
import tkinter as tk
from helpers import clean_screen
from canvas import app

base_dir = os.path.dirname(__name__)


def update_current_user(username, p_id):
    with open("users.txt", "r+", newline="\n") as file:
        users = [json.loads(u.strip()) for u in file]
        for user in users:
            if user["username"] == username:
                user["products"].append(p_id)
                file.seek(0)
                file.truncate()
                file.writelines([json.dumps(user) + "\n" for user in users])
                return


def purchase_product(p_id):
    with open("products.txt", "r+") as f:
        products = [json.loads(p.strip()) for p in f]
        for p in products:
            if p["id"] == p_id:
                p["count"] -= 1
                f.seek(0)
                f.truncate()
                f.writelines([json.dumps(pr) + "\n" for pr in products])
                return


def buy_product(p_id):
    clean_screen()

    with open("current_user.txt") as file:
        username = file.read()

    if username:
        update_current_user(username, p_id)
        purchase_product(p_id)

    render_products_screen()


def render_products_screen():
    clean_screen()

    with open("products.txt", "r") as file:
        products = [json.loads(p.strip()) for p in file]
        products = [p for p in products if p["count"] > 0]
        products_per_line = 4
        rows_per_product = len(products[0])

        for i, p in enumerate(products):
            row = i // products_per_line * rows_per_product
            column = i % products_per_line

            tk.Label(app, text=p["name"]).grid(row=row, column=column)

            img = Image.open(os.path.join(base_dir, "images", p["img_path"])).resize((125, 125))
            photo_img = ImageTk.PhotoImage(img)
            image_label = tk.Label(image=photo_img)
            image_label.image = photo_img
            image_label.grid(row=row + 1, column=column)

            tk.Label(app, text=p["count"]).grid(row=row + 2, column=column)
            tk.Button(app,
                      text=f"Buy {p['id']}",
                      command=lambda pr=p["id"]: buy_product(pr)
                      ).grid(row=row + 3, column=column)
