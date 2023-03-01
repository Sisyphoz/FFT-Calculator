from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fft', methods=['POST'])
def fft():
    # Get input data from request
    input_data = request.get_json()

    # Extract the x and y values from the input data
    x = np.array(input_data['x'])
    y = np.array(input_data['y'])

    # Compute the FFT of the data
    fft_y = np.fft.fft(y)

    # Compute the power spectrum
    power_spectrum = np.abs(fft_y)**2

    # Compute the frequencies corresponding to the FFT coefficients
    freqs = np.fft.fftfreq(len(y), x[1]-x[0])

    # Return the result as a JSON response
    return {
        'freqs': freqs.tolist(),
        'power_spectrum': power_spectrum.tolist()}

if __name__ == '__main__':
    app.run()
