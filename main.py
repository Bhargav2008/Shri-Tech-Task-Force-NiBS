from flask import Flask, jsonify, send_file
import random
import os

app = Flask(__name__)

# Assume we have a directory called 'dishes' with images of dishes
DISHES_DIR = 'dishes'

@app.route('/random-dish', methods=['GET'])
def random_dish():
    try:
        dishes=[f for f in os.listdir(DISHES_DIR) if f.endswith(('jpg', 'jpeg', 'png', 'gif'))]

        if not dishes:
            return jsonify({"error": "no dish images found"}), 404

        selectdish=random.choice(dishes)

        return send_file(os.path.join(DISHES_DIR, selectdish))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/list-of-dish', methods =['GET'])
def lists():
    try:
        lists = ['Tomato Soup','Chicken Biryani','Custard','Ice Cream','Palak Paneer','Pizza','Salad','Breadstick']

        if not lists:
            return jsonify({"error": "no dish images found"}), 404

        return lists
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/types', methods =['GET'])
def types():
    try:
        maincourse = [f for f in os.listdir(DISHES_DIR) if f.startswith(('biryani','chicken','paneer','pizza'))]
        starter = [f for f in os.listdir(DISHES_DIR) if f.startswith(('breadsticks','salad','tomato soup'))]
        dessert = [f for f in os.listdir(DISHES_DIR) if f.startswith(('ice cream','custard'))]
        i = 0
        n = int(input("Enter '1' for Main Courses, '2' for starters and '3' for desserts."))
        if n == 1:
            return send_file(os.path.join(DISHES_DIR, maincourse,'.jpeg'))
        elif n == 2:
            return send_file(os.path.join(DISHES_DIR, starter,'jpeg'))
        if not lists:
            return jsonify({"error": "no dish images found"}), 404

        return lists
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)