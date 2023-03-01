# FFT-Calculator
A simple FFT (Fast Fourier Transform) calculator with Web UI.

To run the app, you need to have Python 3.+ installed. Then, install the required packages by running:

pip install -r requirements.txt

To start the app, run:

python app.py

The app will be available at http://localhost:5000.

Usage

To use the app: 
- navigate to the homepage at http://localhost:5000. Enter the x, y values for your data 
- click the "Compute FFT" button. 

The app will perform the FFT on the input data and display the corresponding frequency and power spectra.

API:
- The app provides a single API endpoint at /fft, which expects a POST request with JSON data containing the x and y values for the input data. 
- The endpoint returns a JSON response containing the frequency and power spectra for the input data.
