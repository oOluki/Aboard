import os

os.system("mkdir build")


IP_address: str = input(
    "Enter the ip adress you want to create the server on "
    "(preferably choose one you can access through external devices such as your phone): "
)

PORT: int = int(
    input(
        "Enter the serving port (for example example '8888'): "
    )
)


in_file = open("src/page.html", "r")
out_file = open("build/page.html", "w")

out_file.write(
    in_file.read().replace(
        '<enter your server address here>',
        "http://" + IP_address + ":" + str(PORT),
        2
    )
)
in_file.close()
out_file.close()



in_file = open("src/base.py", "r")
out_file = open("build/main.py", "w")

out_file.write(
    in_file.read().replace(
        '\'<enter your server address here>\'',
        "(\'" + IP_address + "\', " + str(PORT) + ")",
        1
    )
)

os.system("cp src/buttons.py build/")
os.system("cp src/key_input.py build/")
os.system("cp src/run.sh build/")


in_file.close()
out_file.close()

