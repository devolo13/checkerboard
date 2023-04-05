from flask import Flask, render_template
app = Flask(__name__)


# WORKS
@app.route('/')
def basic_board():
    return render_template('index.html', rows=8, columns=8, light='#556b2f', dark='#ffffe0')


# WORKS
@app.route('/<int:rows>')
def board_with_custom_rows(rows):
    print('working')
    return render_template('index.html', rows=rows, columns=8, light='#556b2f', dark='#ffffe0')


# BROKEN AF
@app.route('/<int:rows>/<int:columns>')
def board_with_custom_cols(rows, columns):
    print(f"columns, {columns}")
    print("hello")
    return render_template('index.html', rows=rows, columns=columns, light='#556b2f', dark='#ffffe0')


# COLORS WORK SAME PROBLEM AS ABOVE
@app.route('/<rows>/<columns>/<dark>')
def board_with_custom_dark(rows, columns, dark):
    return render_template('index.html', rows=int(rows), columns=int(columns), light='#556b2f', dark=dark)


# COLORS WORK SAME PROBLEM AS ABOVE
@app.route('/<rows>/<columns>/<dark>/<light>')
def board_with_custom_light(rows, columns, dark, light):
    return render_template('index.html', rows=int(rows), columns=int(columns), light=light, dark=dark)


if __name__ == "__main__":
    app.run(debug=True)
