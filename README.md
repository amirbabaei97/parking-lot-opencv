
<h1>Parking Lot Empty Space Detection</h1>
<p>This project is a simple demonstration of how to use OpenCV to detect empty spaces in a parking lot.</p>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>
<ul>
  <li>Python 3.6 or later</li>
  <li>OpenCV</li>
  <li>numpy</li>
  <li>json</li>
</ul>
<p>You can install the necessary packages using pip:</p>
<pre>
pip install opencv-python numpy
</pre>

<h3>Usage</h3>
<ol>
  <li>Clone the repository to your local machine:
  <pre>git clone https://github.com/amirbabaei97/parking-lot-opencv</pre>
  </li>
  <li>Navigate to the cloned repository:
  <pre>cd parking-lot</pre>
  </li>
  <li>Define the parking spaces in your parking lot image by running <code>define_parking_spaces.py</code>:
  <pre>python define_parking_spaces.py</pre>
  <ul>
    <li>Left-click to start putting a rectangle around a parking space.</li>
    <li>Repeat this process for all the parking spaces in the image.</li>
    <li>Press 'c' to finish and save the parking spaces to <code>parking_spaces.json</code>.</li>
    <li>Press 'r' to reset all rectangles.</li>
  </ul>
  </li>
  <li>Now, you can detect the empty spaces by running <code>detect_empty_spaces.py</code>:
  <pre>python detect_empty_spaces.py</pre>
  This will load the image and the parking spaces from the JSON file, and display the image with the empty parking spaces highlighted. It will also show the number of free and total parking spaces.
  </li>
</ol>

<h2>How It Works</h2>
<p>The script works by loading a predefined set of parking spaces (each represented as a rectangle in the image) and the current image of the parking lot. It then iterates over each parking space, and checks whether it is occupied or not.</p>
<p>The occupancy check is performed by cropping the parking lot image to the current parking space, converting this cropped image to grayscale, and then applying a binary threshold. If more than a certain proportion of the pixels in the thresholded image are white, the parking space is considered as occupied.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE.md">LICENSE.md</a> file for details</p>


