from flask import Flask, render_template, jsonify
import random
import os

app = Flask(__name__)


@app.route('/')
def index():
    image_name, name_without_ext, real_name = get_random_image()
    return render_template('index.html', image_name=image_name, name=name_without_ext, real_name=real_name)


@app.route('/next_quiz', methods=['POST'])
def next_quiz():
    image_name, name_without_ext, real_name = get_random_image()
    return jsonify({'image_name': image_name, 'name': name_without_ext, 'real_name': real_name})


def replace_randomly_unique(input_str, percent):
    input_list = list(input_str)
    num_to_replace = int(len(input_list) * percent)
    indices_to_replace = random.sample(range(len(input_list)), num_to_replace)
    for idx in indices_to_replace:
        input_list[idx] = '*'
    return ''.join(input_list)


def get_random_image():
    image_folder = './static/icon'
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]
    selected_image = random.choice(image_files)
    name_without_ext = selected_image.rsplit('.', 1)[0].split("_")[
        1].replace("-", " ")
    name_to_display = replace_randomly_unique(name_without_ext, 0.7)
    return os.path.join('icon', selected_image), name_to_display, name_without_ext


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
