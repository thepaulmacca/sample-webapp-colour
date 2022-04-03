from flask import Flask
from flask import render_template
import socket
import random
import os
import argparse

app = Flask(__name__)

colour_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

SUPPORTED_COLOURS = ",".join(colour_codes.keys())

# Get colour from Environment variable
COLOUR_FROM_ENV = os.environ.get('APP_COLOUR')
# Generate a random colour
COLOUR = random.choice(["red", "green", "blue", "blue2", "darkblue", "pink"])


@app.route("/")
def main():
    # return 'Hello'
    return render_template('hello.html', name=socket.gethostname(), color=colour_codes[COLOUR])


if __name__ == "__main__":

    print(" This is a sample web application that displays a coloured background. \n"
          " A colour can be specified in two ways. \n"
          "\n"
          " 1. As a command line argument with --colour as the argument. Accepts one of " + SUPPORTED_COLOURS + " \n"
          " 2. As an Environment variable APP_COLOUR. Accepts one of " + SUPPORTED_COLOURS + " \n"
          " 3. If none of the above then a random colour is picked from the above list. \n"
          " Note: Command line argument precedes over environment variable.\n"
          "\n"
          "")

    # Check for Command Line Parameters for colour
    parser = argparse.ArgumentParser()
    parser.add_argument('--colour', required=False)
    args = parser.parse_args()

    if args.colour:
        print("Colour from command line argument =" + args.colour)
        COLOUR = args.colour
        if COLOUR_FROM_ENV:
            print("A colour was set through environment variable -" + COLOUR_FROM_ENV + ". However, colour from command line argument takes precendence.")
    elif COLOUR_FROM_ENV:
        print("No Command line argument. Colour from environment variable =" + COLOUR_FROM_ENV)
        COLOUR = COLOUR_FROM_ENV
    else:
        print("No command line argument or environment variable. Picking a Random Colour =" + COLOUR)

    # Check if input colour is a supported one
    if COLOUR not in colour_codes:
        print("Colour not supported. Received '" + COLOUR + "' expected one of " + SUPPORTED_COLOURS)
        exit(1)

    # Run Flask Application
    app.run(host="0.0.0.0", port=8080)
