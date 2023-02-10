{\rtf1\ansi\ansicpg1252\cocoartf2706
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import random\
import string\
import os\
import sys\
\
def generate_password(length):\
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))\
    return password\
\
def save_password(filename, password):\
    with open(filename, "w") as f:\
        f.write(password)\
    print(f"Password saved to \{filename\}")\
\
def read_password(filename):\
    if not os.path.exists(filename):\
        print(f"Error: file \{filename\} does not exist.")\
        sys.exit(1)\
    with open(filename, "r") as f:\
        password = f.read().strip()\
    return password\
\
if __name__ == "__main__":\
    filename = "generated_password.txt"\
    length = 16\
    if os.path.exists(filename):\
        password = read_password(filename)\
        print(f"Password from file: \{password\}")\
    else:\
        password = generate_password(length)\
        save_password(filename, password)\
        print(f"Generated password: \{password\}")\
}