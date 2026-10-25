import os
from flask import Flask, jsonify
import redis

app = Flask(__name__)

PRICES = {"laptop": 55000, "headphones": 2500, "keyboard": 1200}
